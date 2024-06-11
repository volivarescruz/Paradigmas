import os

class SaldoEfectivoInsuficiente(Exception):
    pass

class SaldoCuentaInsuficiente(Exception):
    pass

class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        if monto > self.saldo:
            raise SaldoCuentaInsuficiente("Saldo insuficiente para realizar el retiro")
        self.saldo -= monto

    def transferir(self, monto, otra_cuenta):
        if monto > self.saldo:
            raise SaldoCuentaInsuficiente("Saldo insuficiente para realizar la transferencia")
        self.saldo -= monto
        otra_cuenta.depositar(monto)

class CajeroAutomatico:
    def __init__(self):
        self.efectivo_disponible = 100000
        self.cuentas = {}
        self.usuario_actual = None

    def autenticar_cuentahabiente(self, nombre, pin):
        # Aquí podrías implementar la autenticación del titular de la cuenta
        return nombre in self.cuentas and self.cuentas[nombre]["pin"] == pin

    def crear_cuenta(self, nombre, pin, saldo_inicial):
        if nombre in self.cuentas:
            print("El titular ya tiene una cuenta.")
            return
        self.cuentas[nombre] = {"pin": pin, "cuenta": Cuenta(nombre, saldo_inicial)}
        print("Cuenta creada exitosamente.")

    def desplegar_datos_cuenta(self, nombre):
        cuenta = self.cuentas.get(nombre, None)
        if cuenta:
            print(f"Titular de la cuenta: {nombre}")
            print(f"Saldo disponible: ${cuenta['cuenta'].saldo}")
        else:
            print("No se encontró la cuenta.")

    def depositar_efectivo_propio(self, nombre, monto):
        cuenta = self.cuentas.get(nombre, None)
        if cuenta:
            cuenta['cuenta'].depositar(monto)
            print("Depósito exitoso.")
        else:
            print("No se encontró la cuenta.")

    def depositar_efectivo_otra_cuenta(self, nombre_origen, nombre_destino, monto):
        cuenta_origen = self.cuentas.get(nombre_origen, None)
        cuenta_destino = self.cuentas.get(nombre_destino, None)
        if cuenta_origen and cuenta_destino:
            cuenta_origen['cuenta'].retirar(monto)
            cuenta_destino['cuenta'].depositar(monto)
            print("Depósito a otra cuenta exitoso.")
        else:
            print("No se encontró alguna de las cuentas.")

    def transferir(self, nombre_origen, nombre_destino, monto):
        cuenta_origen = self.cuentas.get(nombre_origen, None)
        cuenta_destino = self.cuentas.get(nombre_destino, None)
        if cuenta_origen and cuenta_destino:
            cuenta_origen['cuenta'].transferir(monto, cuenta_destino['cuenta'])
            print("Transferencia exitosa.")
        else:
            print("No se encontró alguna de las cuentas.")

    def retirar_efectivo(self, nombre, monto):
        cuenta = self.cuentas.get(nombre, None)
        if cuenta:
            if monto > self.efectivo_disponible:
                raise SaldoEfectivoInsuficiente("No hay suficiente efectivo en el cajero")
            if monto > cuenta['cuenta'].saldo:
                raise SaldoCuentaInsuficiente("Saldo insuficiente para realizar el retiro")
            cuenta['cuenta'].retirar(monto)
            self.efectivo_disponible -= monto
            print("Retiro exitoso.")
        else:
            print("No se encontró la cuenta.")

def mostrar_menu():
    print("Bienvenido al Cajero Automático")
    print("1. Crear cuenta")
    print("2. Iniciar sesión")
    print("3. Salir")

def menu_crear_cuenta(cajero):
    nombre = input("Ingrese su nombre: ")
    pin = input("Ingrese su PIN: ")
    saldo_inicial = float(input("Ingrese el saldo inicial: "))
    cajero.crear_cuenta(nombre, pin, saldo_inicial)

def menu_iniciar_sesion(cajero):
    nombre = input("Ingrese su nombre: ")
    pin = input("Ingrese su PIN: ")
    if cajero.autenticar_cuentahabiente(nombre, pin):
        cajero.usuario_actual = nombre
        mostrar_menu_operaciones(cajero)
    else:
        print("Nombre de usuario o PIN incorrecto.")

def mostrar_menu_operaciones(cajero):
    while True:
        
        print(f"Bienvenido, {cajero.usuario_actual}")
        print("1. Ver saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Transferir")
        print("5. Cerrar sesión")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            cajero.desplegar_datos_cuenta(cajero.usuario_actual)
        elif opcion == "2":
            monto = float(input("Ingrese el monto a depositar: "))
            cajero.depositar_efectivo_propio(cajero.usuario_actual, monto)
        elif opcion == "3":
            monto = float(input("Ingrese el monto a retirar: "))
            cajero.retirar_efectivo(cajero.usuario_actual, monto)
        elif opcion == "4":
            nombre_destino = input("Ingrese el nombre del destinatario: ")
            monto = float(input("Ingrese el monto a transferir: "))
            cajero.transferir(cajero.usuario_actual, nombre_destino, monto)
        elif opcion == "5":
            cajero.usuario_actual = None
            break
        else:
            print("Opción no válida.")

def main():
    cajero = CajeroAutomatico()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            menu_crear_cuenta(cajero)
        elif opcion == "2":
            menu_iniciar_sesion(cajero)
        elif opcion == "3":
            print("Gracias por utilizar el Cajero Automático.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()

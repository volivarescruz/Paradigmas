class Persona:
    def __init__(self, nombre, edad, genero, direccion, telefono, ciudad, profesion, estado_civil, nacionalidad, email):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.direccion = direccion
        self.telefono = telefono
        self.ciudad = ciudad
        self.profesion = profesion
        self.estado_civil = estado_civil
        self.nacionalidad = nacionalidad
        self.email = email

    # Getters y Setters
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_edad(self):
        return self.edad

    def set_edad(self, edad):
        self.edad = edad

    def get_genero(self):
        return self.genero

    def set_genero(self, genero):
        self.genero = genero

    def get_direccion(self):
        return self.direccion

    def set_direccion(self, direccion):
        self.direccion = direccion

    def get_telefono(self):
        return self.telefono

    def set_telefono(self, telefono):
        self.telefono = telefono

    def get_ciudad(self):
        return self.ciudad

    def set_ciudad(self, ciudad):
        self.ciudad = ciudad

    def get_profesion(self):
        return self.profesion

    def set_profesion(self, profesion):
        self.profesion = profesion

    def get_estado_civil(self):
        return self.estado_civil

    def set_estado_civil(self, estado_civil):
        self.estado_civil = estado_civil

    def get_nacionalidad(self):
        return self.nacionalidad

    def set_nacionalidad(self, nacionalidad):
        self.nacionalidad = nacionalidad

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

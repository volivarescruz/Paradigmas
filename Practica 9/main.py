from robot import Robot

def main():
    grid = [
        [0, 0, 1],
        [0, 1, 0],
        [0, 0, 0]
    ]

    robot = Robot(grid)
    path = robot.find_path()

    if path:
        print("Ruta encontrada:", path)
    else:
        print("No hay ruta disponible.")

if __name__ == "__main__":
    main()

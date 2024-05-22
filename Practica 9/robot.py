class Robot:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.path = []
        self.visited = [[False] * self.cols for _ in range(self.rows)]

    def is_valid(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols and not self.grid[x][y] and not self.visited[x][y]

    def find_path(self):
        if self.dfs(0, 0):
            return self.path
        else:
            return None

    def dfs(self, x, y):
        if x == self.rows - 1 and y == self.cols - 1:
            self.path.append((x, y))
            return True

        if self.is_valid(x, y):
            self.visited[x][y] = True
            self.path.append((x, y))

            # Moverse a la derecha
            if self.dfs(x, y + 1):
                return True

            # Moverse hacia abajo
            if self.dfs(x + 1, y):
                return True

            # Si no se encuentra una ruta, hacer backtrack
            self.path.pop()
            self.visited[x][y] = False

        return False

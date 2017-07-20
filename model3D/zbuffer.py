from math import inf

class ZBuffer:
    def __init__(self, width, height):
        # Inicializar a matriz
        self.matrix = [[inf]*width for _ in range(height)]

    def read_z(self, x, y):
        return self.matrix[y][x]

    def set_z(self, x, y, z):
        self.matrix[y][x] = z

    def compare(self, px, py, pz):
        return True if pz < self.read_z(px, py) else False

    def compare_and_set(self, px, py, pz):
        if pz < self.read_z(px, py):
            self.set_z(px, py, pz)
            return True
        else:
            return False

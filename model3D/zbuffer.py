from math import inf

class ZBuffer:
    def __init__(self, width, height):
        # Inicializar a matriz
        self.matrix = [[inf]*width for _ in range(height)]

    def read_z(self, x, y):
        try:
            return self.matrix[y][x]
        except:
            return -1

    def set_z(self, x, y, z):
        try:
            self.matrix[y][x] = z
        except:
            pass

    def compare(self, px, py, pz):
        return True if pz < self.read_z(px, py) else False

    def compare_and_set(self, px, py, pz):
        z_value = self.read_z(px, py)
        if z_value == -1:
            return False
        elif pz < z_value:
            self.set_z(px, py, pz)
            return True
        else:
            return False

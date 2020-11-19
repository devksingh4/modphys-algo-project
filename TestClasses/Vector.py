import math

class Vector:
    """A simple three-dimensional vector"""

    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self,other):
        return Vector(self.x * other, self.y * other, self.z * other)

    def __sub__(self, other):
        return self + (other * (-1))

    def magnitude_squared(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2

    def magnitude(self):
        return math.sqrt(self.magnitude_squared())

    def azimuthal(self):
        return math.atan2(self.y, self.x);

    def polar(self):
        return math.acos(self.z / self.magnitude())
import math


class Vector3d:

    def __init__(self, x=0, y=0, z=0) -> None:
        self.x = x
        self.y = y
        self.z = z

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def normalize(self):
        magnitude = self.magnitude()
        return Vector3d(self.x / magnitude, self.y / magnitude, self.z / magnitude)

    def dot(self, vector):
        return (self.x * vector.x + self.y * vector.y + self.z * vector.z)

    def cross(self, vector):
        x = self.y * vector.z - self.z * vector.y
        y = self.z * vector.x - self.x * vector.z
        z = self.x * vector.y - self.y * vector.x
        return Vector3d(x, y, z)


class Vector2d:

    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y
        self.z = 0

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        magnitude = self.magnitude()
        return Vector2d(self.x / magnitude, self.y / magnitude)

    def dot(self, vector):
        return (self.x * vector.x + self.y * vector.y)

    def cross(self, vector):
        i = self.y * vector.z - self.z * vector.y
        y = self.z * vector.x - self.x * vector.z
        z = self.x * vector.y - self.y * vector.x
        return Vector3d(i, y, z)

    def __sub__(self, other):
        return Vector2d(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Vector2d(self.x + other.x, self.y + other.y)
    
    def __mul__(self, other:float):
        return Vector2d(self.x * other, self.y * other)

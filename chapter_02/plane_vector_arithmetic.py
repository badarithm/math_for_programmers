from __future__ import  annotations

dino_vetctors  = [(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4), (-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0), (0,-3), (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1)]
triangle = [(2.3,1.1,0.9), (4.5,3.3,2.0), (1.0,3.5,3.9)]

class Vector():
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self) -> str:
        return '<Vector({}, {})>'.format(self.x, self.y)

    def __mul__(self, other: Vector) -> Vector:
        pass

    def dot(self, other: Vector) -> float:
        pass

    def translate(self, other: Vector) -> Vector:
        return self + other
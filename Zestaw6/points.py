from math import sqrt
class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):         # zwraca string "(x, y)"
        return f"({self.x}, {self.y})"
    def __repr__(self):        # zwraca string "Point(x, y)"
        return f"Point({self.x}, {self.y})"
    def __eq__(self, other):   # obsługa point1 == point2
        return self.x == other.x and self.y == other.y
    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        return Point(self.x + other.x, self.y + other.y)
    def __sub__(self, other):  # v1 - v2
        return Point(self.x - other.x, self.y - other.y)
    def __mul__(self, other):  # v1 * v2, iloczyn skalarny, zwraca liczbę
        return self.x * (other.x + other.y) + self.y * (other.x + other.y)
    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self): # długość wektora
        return sqrt((self.x ** 2) + (self.y ** 2))
    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points

# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase):
    def setUp(self):
        self.p1 = Point(1, 2)
        self.p2 = Point(0, 4)
    def test_str(self):
        self.assertEqual(str(self.p1), "(1, 2)")
    def test_repr(self):
        self.assertEqual(repr(self.p1), "Point(1, 2)")
    def test_eq(self):
        self.assertEqual(self.p1 == Point(1, 2), True)
    def test_ne(self):
        self.assertEqual(self.p1 != self.p2, True)
    def test_add(self):
        self.assertEqual(self.p1 + self.p2, Point(1, 6))
    def test_sub(self):
        self.assertEqual(self.p1 - self.p2, Point(1, -2))
    def test_mul(self):
        self.assertEqual(self.p1 * self.p2, 12)
    def test_cross(self):
        self.assertEqual(self.p1.cross(self.p2), 4)
    def test_len(self):
        self.assertEqual(self.p2.length(), 4)
    def test_hash(self):
        self.assertEqual(hash(self.p1), hash((self.p1.x, self.p1.y)))
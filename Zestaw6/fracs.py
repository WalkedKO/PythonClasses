from math import gcd   # Py3


class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y
        if y == 0:
            self.y = 1
            print(f"Nie mozna dzielic przez 0, ulamek ustawiono na {x}")
    @staticmethod
    def short(x, y):
        tempgcd = gcd(x, y)
        return x / tempgcd, y / tempgcd
    def __str__(self): # zwraca "x/y" lub "x" dla y=1
        if self.y == 0:
            return str(self.x)
        else:
            return f"{self.x} / {self.y}"

    def __repr__(self):        # zwraca "Frac(x, y)"
        return f"Frac({self.x}, {self.y})"
    #def __cmp__(self, other): pass  # cmp(frac1, frac2)    # Py2

    def __eq__(self, other):    # Py2.7 i Py3
        return self.x * other.y == other.x * self.y
    def __ne__(self, other):
        return not self.__eq__(other)
    def __lt__(self, other):
        return self.x * other.y < other.x * self.y
    def __le__(self, other):
        return self.x * other.y <= other.x * self.y
    #def __gt__(self, other): pass

    #def __ge__(self, other): pass

    def __add__(self, other):  # frac1 + frac2
        new_x = self.x * other.y + other.x * self.y
        new_y = self.y * other.y
        new_x, new_y = self.short(new_x, new_y)
        return Frac(new_x, new_y)
    def __sub__(self, other):  # frac1 - frac2
        new_x = self.x * other.y - other.x * self.y
        new_y = self.y * other.y
        new_x, new_y = self.short(new_x, new_y)
        return Frac(new_x, new_y)
    def __mul__(self, other):  # frac1 * frac2
        return Frac(self.x *  other.x, self.y * other.y)
    def __div__(self, other):  # frac1 / frac2, Py2
        return self.__mul__(other.__invert__())
    def __truediv__(self, other):  # frac1 / frac2, Py3
        return self.__mul__(other.__invert__())
    def __floordiv__(self, other):  # frac1 // frac2, opcjonalnie
        new_x, new_y = self.x * other.y, self.y * other.x
        return new_x // new_y
    def __mod__(self, other):  # frac1 % frac2, opcjonalnie
        new_x, new_y = self.x *  other.y, self.y * other.x
        return Frac(new_x % new_y, new_y)

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __float__(self):       # float(frac)
        return float(self.x / self.y)
    def __hash__(self):
        return hash(float(self))   # immutable fracs
        # w Pythonie set([2]) == set([2.0])
        # chcemy set([2]) == set([Frac(2)])

# Kod testujący moduł.

import unittest

class TestFrac(unittest.TestCase):
    def setUp(self):
        self.p1 = Frac(2,6)
        self.p2 = Frac(1,2)
        self.p3 = Frac(1, 3)
        self.p4 = Frac(1, 4)
    def test_str(self):
        self.assertEqual(str(self.p1), "2 / 6")
    def test_repr(self):
        self.assertEqual(repr(self.p1), "Frac(2, 6)")
    def test_eq(self):
        self.assertEqual(self.p1 == self.p3, True)
    def test_ne(self):
        self.assertEqual(self.p1 == self.p2, False)
    def test_lt(self):
        self.assertEqual(self.p1 < self.p2, True)
    def test_le(self):
        self.assertEqual(self.p1 <= self.p3, True)
    def test_add(self):
        self.assertEqual(self.p1 + self.p2, Frac(5, 6))
    def test_sub(self):
        self.assertEqual(self.p1 - self.p2, Frac(-1, 6))
    def test_mul(self):
        self.assertEqual(self.p1 * self.p2, Frac(1, 6))
    def test_div(self):
        self.assertEqual(self.p1 / self.p2, Frac(2, 3))
    def test_floordiv(self):
        self.assertEqual(self.p1 // self.p4, 1)
    def test_mod(self):
        self.assertEqual(self.p1 % self.p4, Frac(2, 6))
    def test_pos(self):
        self.assertEqual(self.p1, self.p1)
    def test_neg(self):
        self.assertEqual(-self.p1, Frac(-2, 6))
    def test_inv(self):
        self.assertEqual(~self.p1, Frac(6, 2))
    def test_flt(self):
        self.assertEqual(float(self.p2), 0.5)
    def test_hash(self):
        self.assertEqual(hash(self.p2), hash(0.5))
if __name__ == '__main__':
    unittest.main()
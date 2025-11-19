from Zestaw6.points import Point

class Triangle:
    """Klasa reprezentująca trójkąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        # Należy zabezpieczyć przed sytuacją, gdy punkty są współliniowe.
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)
        if self.pt1.cross(self.pt2) == 0 and self.pt2.cross(self.pt3) == 0 and self.pt1.cross(self.pt3) == 0:
            raise ValueError

    def __str__(self):         # "[(x1, y1), (x2, y2), (x3, y3)]"
        return f"[{self.pt1}, {self.pt2}, {self.pt3}]"
    def __repr__(self):        # "Triangle(x1, y1, x2, y2, x3, y3)"
        return f"Triangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y}, {self.pt3.x}, {self.pt3.y})"
    def __eq__(self, other):   # obsługa tr1 == tr2
        # Trójkąty powinny być równe, jeżeli mają ten sam zbiór wierzchołków,
        # niezależnie od kolejności pt1, pt2, pt3.
        return {self.pt1, self.pt2, self.pt3} == {other.pt1, other.pt2, other.pt3}

    def __ne__(self, other):        # obsługa tr1 != tr2
        return not self == other

    def center(self):         # zwraca środek trójkąta
        return Point((self.pt1.x + self.pt2.x + self.pt3.x) / 3, (self.pt1.y + self.pt2.y + self.pt3.y) / 3)
    def area(self):           # pole powierzchni
        return 1/2 * abs(self.pt1.x * (self.pt2.y - self.pt3.y) + self.pt2.x *(self.pt3.y - self.pt1.y) + self.pt3.x * (self.pt1.y - self.pt2.y))
    def move(self, x, y):      # przesunięcie o (x, y)
        moving = Point(x,y)
        self.pt1 += moving
        self.pt2 += moving
        self.pt3 += moving
    def make4(self):          # zwraca krotkę czterech mniejszych
        new_pt = lambda p, q: ((p.x + q.x) / 2, (p.y + q.y) / 2)
        ax, ay = new_pt(self.pt1, self.pt2)
        bx, by = new_pt(self.pt2, self.pt3)
        cx, cy = new_pt(self.pt3, self.pt1)
        return (Triangle(self.pt1.x, self.pt1.y, ax, ay, cx, cy),
                Triangle(self.pt2.x, self.pt2.y, ax, ay, bx, by),
                Triangle(self.pt3.x, self.pt3.y, bx, by, cx, cy))


import unittest

class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.tr1 = Triangle(0, 0, 1, 0, .5, 1)
        self.tr2 = Triangle(1, 0, 0, 0, .5, 1)
        self.tr3 = Triangle(0,2,2,2,0,1)
    def test_str(self):
        self.assertEqual(str(self.tr1), "[(0, 0), (1, 0), (0.5, 1)]")
    def test_repr(self):
        self.assertEqual(repr(self.tr1), "Triangle(0, 0, 1, 0, 0.5, 1)")
    def test_eq(self):
        self.assertEqual(self.tr1 == self.tr2, True)
    def test_neg(self):
        self.assertEqual(self.tr1 != self.tr3, True)
    def test_center(self):
        self.assertEqual(self.tr1.center(), Point(0.5, 1/3))
    def test_area(self):
        self.assertEqual(self.tr1.area(), 0.5)
    def test_move(self):
        self.tr1.move(1, 2)
        self.assertEqual(self.tr1, Triangle(1,2,2,2,1.5,3))
    def test_make(self):
        self.tr1 = Triangle(0, 0, 1, 0, .5, 1)
        self.assertEqual(self.tr1.make4(), (Triangle(0, 0, 0.5, 0, 0.25,0.5),
                                                 Triangle(0.5, 0, 1, 0, 0.75, 0.5),
                                                 Triangle(0.25,0.5, 0.75, 0.5, 0.5, 1)))
if __name__ == '__main__':
    unittest.main()
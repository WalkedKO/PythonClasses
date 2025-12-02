from Zestaw6.points import Point

class Triangle:
    """Klasa reprezentująca trójkąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        # Należy zabezpieczyć przed sytuacją, gdy punkty są współliniowe.
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)
        a = self.pt2 - self.pt1
        b = self.pt3 - self.pt1
        if a.cross(b) == 0:
            raise ValueError

    @staticmethod
    def from_points(points):
        return Triangle(points[0].x, points[0].y, points[1].x, points[1].y, points[2].x, points[2].y)

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
                Triangle(self.pt3.x, self.pt3.y, bx, by, cx, cy),
                Triangle(ax, ay, bx,by,cx,cy))
    # added for 8th set of exercises
    @property
    def top(self):
        return max((self.pt1.y, self.pt2.y, self.pt3.y))

    @property
    def left(self):
        return min((self.pt1.x, self.pt2.x, self.pt3.x))

    @property
    def bottom(self):
        return min((self.pt1.y, self.pt2.y, self.pt3.y))

    @property
    def right(self):
        return max((self.pt1.x, self.pt2.x, self.pt3.x))

    @property
    def topleft(self):
        return Point(self.left, self.top)

    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)

    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)
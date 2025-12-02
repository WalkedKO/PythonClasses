# zmodyfikowano klase triangle wedlug polecenia, zmodyfikowany plik w folderze Zestaw7
import pytest
from Zestaw7.triangles import Triangle
from Zestaw6.points import Point


triangle = Triangle(0, 0, 2, 0, 1, 2)
def test_from_points():
    assert Triangle.from_points((Point(0, 0), Point(2, 0), Point(1, 2)))
def test_str():
    assert str(triangle) == "[(0, 0), (2, 0), (1, 2)]"
def test_repr():
    assert repr(triangle) == "Triangle(0, 0, 2, 0, 1, 2)"
def test_eq():
    assert Triangle(2, 0, 1, 2, 0, 0) == triangle
def test_neg():
    assert Triangle(1,1,2,1,1.5,-10) != triangle
def test_center():
    assert triangle.center() == Point(1, 2 / 3)
def test_area():
    assert triangle.area() == 2
def test_move():
    x = 2
    y = 1
    copy_tr = Triangle(0, 0, 2, 0, 1, 2)
    copy_tr.move(1, 2)
    assert copy_tr == Triangle(1, 2, 3, 2, 2, 4)
def test_top():
    assert triangle.top == 2
def test_left():
    assert triangle.left == 0
def test_right():
    assert triangle.right == 2
def test_bottom():
    assert triangle.bottom == 0
def test_topleft():
    assert triangle.topleft == Point(0, 2)
def test_topright():
    assert triangle.topright == Point(2, 2)
def test_bottomright():
    assert triangle.bottomright == Point(2, 0)
def test_bottomleft():
    assert triangle.bottomleft == Point(0, 0)
def test_make4():
    assert triangle.make4() == (Triangle(0, 0, 1, 0, .5,1),
                                Triangle(2, 0,1, 0, 1.5,1),
                                Triangle(.5,1,1.5,1, 1,2),
                                Triangle(.5,1,1.5,1,1,0))
if __name__ == "__main__":
    pytest.main()
from functools import reduce

# ZADANIE 5.3
def add_poly(poly1, poly2):
    result = [sum(i) for i in zip(poly1, poly2)]
    if len(poly1) > len(poly2):
        result += poly1[len(poly2):]
    else:
        result += poly2[len(poly1):]
    return result
def sub_poly(poly1, poly2):      # poly1(x) - poly2(x)
    return add_poly(poly1, [-i for i in poly2])
def mul_poly(poly1, poly2):        # poly1(x) * poly2(x)
    result = []
    for i, element in enumerate(poly1):
        for j, second in enumerate(poly2):
            ready = second * element
            if i + j < len(result):
                result[i + j] += ready
            else:
                result.append(ready)
    return result
def is_zero(poly):
    for i in poly:
        if i != 0:
            return False
    return True
def eq_poly(poly1, poly2):        # bool, porównywanie poly1(x) == poly2(x)
    return poly1 == poly2
def eval_poly(poly, x0):          # poly(x0), algorytm Hornera
    if len(poly) <= 1:
        return poly[0]
    return x0 * eval_poly(poly[1:], x0) + poly[0]

def pow_poly(poly, n):  # poly(x) ** n
    if n == 0:
        return 1
    if n == 1:
        return poly
    return mul_poly(poly, pow_poly(poly, n - 1))
def combine_poly(poly1, poly2):    # poly1(poly2(x)), trudne!
    polynomials = []
    for i, element in enumerate(poly1):
        if i == 0:
            polynomials.append([poly1[0]])
            continue
        polynomials.append([element * j for j in pow_poly(poly2, i)])
    return reduce(add_poly, polynomials)
def diff_poly(poly):              # pochodna wielomianu
    result = poly.copy()
    for i, element in enumerate(result):
        result[i] *= i
    return result[1:]


import unittest
class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.p1 = [0, 1]
        self.p2 = [0, 0, 1]

    def test_add_poly(self):
        self.assertEqual(add_poly(self.p1, self.p2), [0, 1, 1])
    def test_sub_poly(self):
        self.assertEqual(sub_poly(self.p1, self.p2), [0, 1, -1])
    def test_mul_poly(self):
        self.assertEqual(mul_poly(self.p1, self.p2), [0, 0, 0, 1])
    def test_is_zero(self):
        self.assertEqual(is_zero(self.p1), False)
    def test_eq_poly(self):
        self.assertEqual(eq_poly(self.p1, self.p2), False)
    def test_eval_poly(self):
        self.assertEqual(eval_poly(self.p1, 4), 4)
    def test_combine_poly(self):
        self.assertEqual(combine_poly(self.p1, self.p2), [0, 0, 1])
    def test_pow_poly(self):
        self.assertEqual(pow_poly(self.p1, 4), [0, 0, 0, 0, 1])
    def test_diff_poly(self):
        self.assertEqual(diff_poly(self.p1), [1])
    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
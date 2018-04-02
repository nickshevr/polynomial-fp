import unittest
from polynomial import Polynomial


class TestPolynomial(unittest.TestCase):

    def test_init_correct_args(self):
        p = Polynomial([1, 2, 3])
        self.assertEqual(p.coeffs, [3, 2, 1])
        self.assertEqual(p.degree, 2)

    def test_init_empty_list(self):
        self.assertRaises(TypeError, Polynomial, [])

    def test_init_incorrect_list(self):
        self.assertRaises(TypeError, Polynomial, ["1", 2])

    def test_init_by_zero(self):
        p = Polynomial([0])
        self.assertEqual(p.coeffs, [0])
        self.assertEqual(p.degree, 0)

    def test_init_by_number(self):
        p = Polynomial([1])
        self.assertEqual(p.coeffs, [1])
        self.assertEqual(p.degree, 0)

    def test_init_senior_values_is_zero(self):
        p = Polynomial([1, 2, 0])
        self.assertEqual(p.coeffs, [0, 2, 1])
        self.assertEqual(p.degree, 2)

    def test_init_float_values(self):
        p = Polynomial([1.0, 2.0, 3.0])
        self.assertEqual(p.coeffs, [3.0, 2.0, 1.0])
        self.assertEqual(p.degree, 2)

    def test_eq_true(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([1, 2, 3])
        self.assertTrue(p1 == p2)
    
    def test_eq_number(self):
        p1 = Polynomial([1])
        p2 = 1
        self.assertTrue(p1 == p2)

    def test_eq_raise(self):
        p1 = Polynomial([1])
        p2 = '2'
        self.assertRaises(TypeError, p1.__eq__, p2)

    def test_eq_false(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([1, 2])
        self.assertFalse(p1 == p2)

    def test_neq_true(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([1, 2, 4])
        self.assertTrue(p1 != p2)

    def test_neq_false(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([1, 2, 3])
        self.assertFalse(p1 != p2)

    def test_add_constant(self):
        p1 = Polynomial([1, 2])
        p2 = 2
        p3 = p1 + p2
        self.assertEqual(p3.coeffs, [1, 4])
        self.assertEqual(p3.degree, 1)

    def test_add_negative_constant(self):
        p1 = Polynomial([1, 2])
        p2 = -1
        p3 = p1 + p2
        self.assertEqual(p3.coeffs, [1, 1])
        self.assertEqual(p3.degree, 1)

    def test_add_different_degrees(self):
        self.assertTrue(Polynomial([1, 0]) + Polynomial([5]) == Polynomial([1, 5]))

    def test_mul_string_constant(self):
        p1 = Polynomial([1, 2])
        self.assertRaises(TypeError, p1.__mul__, "asd")
    
    def test_add_same_polyn_size(self):
        p1 = Polynomial([1, 2])
        p2 = Polynomial([1, 2])
        p3 = p1 + p2
        self.assertEqual(p3, Polynomial([2, 4]))
        self.assertEqual(p3.degree, 1)

    def test_add_different_polyn_size(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([1, 2])
        p3 = p1 + p2
        self.assertEqual(p3, Polynomial([1, 3, 5]))
        self.assertEqual(p3.degree, 2)

    def test_add_negative_values(self):
        p1 = Polynomial([1, -1])
        p2 = Polynomial([-1, 2])
        p3 = p1 + p2
        self.assertEqual(p3, Polynomial([0, 1]))
        self.assertEqual(p3.degree, 0)

    def test_add_zero_values(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([0, 0])
        p3 = p1 + p2
        self.assertEqual(p3, p1)
        self.assertEqual(p3.degree, 2)

    def test_remove_highest_monome(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([-1, 0, 0])

        p3 = p1 + p2
        self.assertEqual(p3, Polynomial([2, 3]))
        self.assertEqual(p3.degree, 1)

    def test_mul_zero(self):
        p1 = Polynomial([1, 2, 3])
        p2 = 0
        p3 = p1 * p2
        self.assertEqual(p3, Polynomial([0]))

    def test_mul_constant(self):
        p1 = Polynomial([1, 2, 3])
        p2 = 2
        p3 = p1 * p2
        self.assertEqual(p3, Polynomial([2, 4, 6]))

    def test_mul_negative_constant(self):
        p1 = Polynomial([1, 2, 3])
        p2 = -2
        p3 = p1 * p2
        self.assertEqual(p3, Polynomial([-2, -4, -6]))

    def test_mul_poly(self):
        p1 = Polynomial([1, 0])
        p2 = Polynomial([1, 2, 3])
        p3 = p1 * p2
        self.assertEqual(p3, Polynomial([1, 2, 3, 0]))

    def test_hard_mul_poly(self):
        p1 = Polynomial([1, 1])
        p2 = Polynomial([1, 2, 3])
        p3 = p1 * p2
        self.assertEqual(p3, Polynomial([1, 3, 5, 3]))

    def test_mul_negative_poly(self):
        p1 = Polynomial([-1, 0])
        p2 = Polynomial([1, 2, 3])
        p3 = p1 * p2
        self.assertEqual(p3, Polynomial([-1, -2, -3, 0]))

    def test_str(self):
        p1 = Polynomial([1, 2])
        self.assertEqual(str(p1), 'x+2')

    def test_str_zero_values(self):
        p1 = Polynomial([0, 0, 0])
        self.assertEqual(str(p1), '0')

    def test_str_first_float_zero_values(self):
        p1 = Polynomial([0.0, 0.0, 0.0])
        self.assertEqual(str(p1), '0')

    def test_str_first_value_is_zero(self):
        p1 = Polynomial([0, 2, 3])
        self.assertEqual(str(p1), '2x+3')

    def test_str_first_value_is_one(self):
        p1 = Polynomial([1, 2, 3])
        self.assertEqual(str(p1), 'x2+2x+3')

    def test_str_all_values_are_one(self):
        p1 = Polynomial([1, 1, 1])
        self.assertEqual(str(p1), 'x2+x+1')

    def test_str_last_value_is_zero(self):
        p1 = Polynomial([1, 2, 0])
        self.assertEqual(str(p1), 'x2+2x')

    def test_str_big_polynom(self):
        p1 = Polynomial([1, 0, 7, 9, 10, 12])
        self.assertEqual(str(p1), 'x5+7x3+9x2+10x+12')

    def test_str_first_two_value_is_zero(self):
        p1 = Polynomial([0, 0, 3])
        self.assertEqual(str(p1), '3')

    def test_str_one_value_is_zero(self):
        p1 = Polynomial([0, 1, 0])
        self.assertEqual(str(p1), 'x')

    def test_str_one_value_is_minus_zero(self):
        p1 = Polynomial([0, -1, 0])
        self.assertEqual(str(p1), '-x')

    def test_str_first_value_is_negative(self):
        p1 = Polynomial([-1, 1, 0])
        self.assertEqual(str(p1), '-x2+x')

if __name__ == "__main__":
    unittest.main()
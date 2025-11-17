# https://github.com/anishpat26-commits/lab10-AP-JJ.git
# Partner 1: Anish Patel
# Partner 2: James Jiang

from calculator import *
import unittest



class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1,1), 2)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(1,1), 0)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(6,7),42)
        self.assertEqual(mul(-6, 9), -54)
        self.assertEqual(mul(0, 100), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(6, 54), 9)
        self.assertEqual(div(-7, 42), -6)
        self.assertAlmostEqual(div(8, 20), 2.5)

    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0,5)
    # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(2, 64), 6)
        self.assertAlmostEqual(logarithm(4, 32), 2.5)
        self.assertAlmostEqual(logarithm(4, 1), 0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 64)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)
    #     fill in code

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(-3, 4), 5)
        self.assertAlmostEqual(hypotenuse(8, 15), 17)
        self.assertAlmostEqual(hypotenuse(0, 0), 0)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-41)

        self.assertAlmostEqual(square_root(0), 0)
        self.assertAlmostEqual(square_root(64), 8)

    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
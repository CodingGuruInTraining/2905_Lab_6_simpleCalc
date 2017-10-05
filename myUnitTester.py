import unittest
import Calc

newCalculator = Calc.Calculator

class TestCalculator(unittest.TestCase):
    def testAddition(self):
        self.assertEqual(newCalculator.addition(1, 2), 3)
        self.assertEqual(newCalculator.addition(18, 7), 25)
        self.assertEqual(newCalculator.addition(3, 9), 12)
        self.assertEqual(newCalculator.addition(1, 19), 20)

    def testSubtraction(self):
        self.assertEqual(newCalculator.subtraction(654, 2), 652)
        self.assertEqual(newCalculator.subtraction(5, 1), 4)
        self.assertEqual(newCalculator.subtraction(100, 99), 1)

    def testMultiply(self):
        self.assertEqual(newCalculator.multiply(5, 5), 25)
        self.assertEqual(newCalculator.multiply(2, 1), 2)
        self.assertEqual(newCalculator.multiply(4, 3), 12)

    def testDivision(self):
        self.assertEqual(newCalculator.division(64, 8), 8)
        self.assertEqual(newCalculator.division(18, 3), 6)
        self.assertEqual(newCalculator.division(42, 0), 0)

if __name__ == '__main__':
    unittest.main()
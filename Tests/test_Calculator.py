import unittest

from Calculator.Calculator import Calc

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calc()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calc)

if __name__ == '__main__':
    unittest.main()
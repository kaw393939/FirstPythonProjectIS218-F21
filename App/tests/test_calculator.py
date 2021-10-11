"""Testing calc"""
import unittest
from calc.base import Base

class CalculatorTestCase(unittest.TestCase):
    """Calculator Module tests"""
    def setUp(self) -> None:
        """Setup the Test runs before each test method calc"""
        self.calculator = Base()
    def test_instantiate_calculator(self):
        """Tests Object Instantiation"""
        self.assertIsInstance(self.calculator, Base)
if __name__ == '__main__':
    unittest.main()

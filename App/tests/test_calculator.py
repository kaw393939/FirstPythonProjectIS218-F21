"""Testing calc_mod"""
import unittest
from calc_mod.calculator import Simple

class CalculatorTestCase(unittest.TestCase):
    """Calculator Module tests"""
    def setUp(self) -> None:
        """Setup the Test runs before each test method calc_mod"""
        self.calculator = Simple()
    def test_instantiate_calculator(self):
        """Tests Object Instantiation"""
        self.assertIsInstance(self.calculator, Simple)
if __name__ == '__main__':
    unittest.main()

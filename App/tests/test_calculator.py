import pytest
from calc_mod.calculator import Simple

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_simple_instance():
    calculator = Simple()
    isinstance(calculator,Simple)

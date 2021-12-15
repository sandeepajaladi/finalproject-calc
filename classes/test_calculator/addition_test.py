"""Testing Addition"""
from classes.Addition import addition

    from calculator.main import Calculator

    def test_calculator_add_result():
        """testing calculator result is 0"""
        calc = Calculator()
        result = calc.add(1, 2)
        assert result == 3
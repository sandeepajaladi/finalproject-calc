from classes.main import Calculator

def test_calculator_multiply_result():
    """testing calculator result is 0"""
    calc = Calculator()
    result = calc.multiply(1,2)
    assert result == 2
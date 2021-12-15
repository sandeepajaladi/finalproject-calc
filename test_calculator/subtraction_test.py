from calculator.main import Calculator

def test_calculator_subtract_result():
    """testing calculator result is 0"""
    calc = Calculator()
    result = calc.subtract(1,2)
    assert result == -1

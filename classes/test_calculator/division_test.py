from calculator.main import Calculator
def test_calculator_divide_result():
    """testing calculator result is 0"""
    calc = Calculator()
    result = calc.divide(1,2)
    assert result == 0.5

def test_calculator_divide_fail_result():
    """testing calculator result is 0"""
    calc = Calculator()
    result = calc.divide(1,0)
    assert result == "Error: A number cannot be divided by 0"

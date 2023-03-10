import pytest 
from calculator import Calculator

calculator = Calculator()


@pytest.mark.parametrize('num1, num2, result', [(1, 4, 5), (-6, -10, -16), (-1, 4, 3), (1.22, 4.22, 5.44), (0, 1, 1),])
def test_sum_positif_num(num1, num2, result):
    calculator = Calculator()
    c = calculator.sum(num1, num2)
    c = round(c, 2)
    assert c == result

def test_div_positive():
    calculator = Calculator()
    c = calculator.div(10, 2)
    assert c == 5

def test_div_by_zero():
    calculator = Calculator()
    
    with pytest.raises(ArithmeticError):
        calculator.div(10, 0)
    
@pytest.mark.parametrize('nums, result', [([], 0), ([1,2,3], 2)])
def test_avg_zero(nums, result):
    calculator = Calculator()
    c = calculator.avg(nums)
    assert c == result

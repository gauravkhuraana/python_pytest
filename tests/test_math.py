# Basic test s
import pytest

def test_addition():
    assert 1+2==3

def test_differnce():
    a=1
    b=2
    c=3
    assert a+b==c    

def test_exception_Zero():
    with pytest.raises(ZeroDivisionError) as e:
      a = 1/0
    assert 'division by zero' in str(e.value)

products = [

(2,3,6),
(1,99,99),
(22,0,0),
(3,-4,-12),
(-4,-5,20),
(2.5, 6.7,16.75)
]

# Parameterisation

@pytest.mark.parametrize('x,y,prod', products)
def test_mult(x,y,prod):
    assert x*y==prod

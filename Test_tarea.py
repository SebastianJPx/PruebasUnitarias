import pytest
from Tarea import Calculadora

@pytest.fixture
def calculadora():
    return Calculadora()

def test_add(calculadora):
    assert calculadora.add(2, 3) == 5
    assert calculadora.add(-1, -3) == -4

def test_subtract(calculadora):
    assert calculadora.subtract(7, 3) == 4
    assert calculadora.subtract(-5, 5) == -10

def test_multiply(calculadora):
    assert calculadora.multiply(4, 3) == 12
    assert calculadora.multiply(-4, -5) == 20

def test_divide(calculadora):
    assert calculadora.divide(6, 3) == 2
    assert calculadora.divide(-6, -2) == 3

# Prueba para división por cero con validación del mensaje
    with pytest.raises(ValueError) as exc_info:
        calculadora.divide(6, 0)
    assert str(exc_info.value) == "No se puede dividir entre cero."
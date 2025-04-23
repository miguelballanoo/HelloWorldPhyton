# test_mimodulo.py

import pytest
from mimodulo import suma

def test_suma_enteros():
    assert suma(2, 3) == 5

def test_suma_negativos():
    assert suma(-1, -1) == -2

@pytest.mark.parametrize("a, b, esperado", [
    (0, 0, 0),
    (10, -5, 5),
    (2.5, 0.5, 3.0),
])
def test_suma_parametrizada(a, b, esperado):
    assert suma(a, b) == esperado

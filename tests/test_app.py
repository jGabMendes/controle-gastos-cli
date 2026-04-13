import pytest
from src.app import adicionar, listar, total, gastos

def setup_function():
    gastos.clear()

def test_adicionar_gasto():
    adicionar(50, "mercado")
    assert len(listar()) == 1

def test_valor_negativo():
    with pytest.raises(ValueError):
        adicionar(-10, "erro")

def test_total():
    adicionar(10, "a")
    adicionar(20, "b")
    assert total() == 30
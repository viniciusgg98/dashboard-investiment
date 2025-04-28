import pytest
from src.investimento import calcular_taxa_mensal, atualizar_patrimonio, calcular_patrimonio_final


def test_calcular_taxa_mensal():
    assert round(calcular_taxa_mensal(12), 5) == 0.01  # 12% ao ano vira 1% ao mês

def test_atualizar_patrimonio_sem_rendimento():
    patrimonio = atualizar_patrimonio(1000, 500, 0) # 0% de rendimento mensal
    assert patrimonio == 1500

def test_atualizar_patrimonio_com_rendimento():
    patrimonio = atualizar_patrimonio(1000, 500, 0.01)  # 1% de rendimento mensal
    assert round(patrimonio, 2) == 1515.00

def test_calcular_patrimonio_final_sem_aporte():
    resultado = calcular_patrimonio_final(0, 1, 12, 1000)
    assert round(resultado, 2) == 1126.83  # 1 ano a 12% ao ano

def test_calcular_patrimonio_final_com_aportes():
    resultado = calcular_patrimonio_final(100, 2, 6, 1000)
    assert resultado > 1000  # Crescimento esperado

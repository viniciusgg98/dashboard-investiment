#funçao 1.9

def calcular_taxa_mensal(taxa_anual: float) -> float:
    return (taxa_anual / 100) / 12

def atualizar_patrimonio(patrimonio: float, aporte: float, taxa_mensal: float) -> float:
    return (patrimonio + aporte) * (1 + taxa_mensal)

def calcular_patrimonio_final(aporte_mensal: float, anos: int, taxa_anual: float, patrimonio_inicial: float) -> float:
    taxa_mensal = calcular_taxa_mensal(taxa_anual)
    patrimonio = patrimonio_inicial
    for _ in range(anos * 12):
        patrimonio = atualizar_patrimonio(patrimonio, aporte_mensal, taxa_mensal)
    return patrimonio

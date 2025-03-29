#Variaveis iniciais
aporte_mensal = float(input("Quanto você vai aportar por mês R$: "))
anos = int(input("Quantos anos você vai investir: "))
taxa_de_rendimento_anual = float(input("Qual sua taxa de rendimento anual: "))
taxa_de_rendimento_mensal = (taxa_de_rendimento_anual / 100) / 12
patrimonio = float(input("Quanto dinheiro você já tem investido R$: "))

for mes in range(anos *12):
    patrimonio = (patrimonio + aporte_mensal) * (1+taxa_de_rendimento_mensal)

patrimonio_formatado = "{:,.2f}".format(patrimonio)
print(f"saldo final após {anos} anos: R$ {patrimonio_formatado}")
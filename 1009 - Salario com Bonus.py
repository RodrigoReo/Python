nome = str(input())
fixo = float(input())
vendas = float(input())
salario = (vendas*15)/100 + fixo
print("TOTAL = R$", '{:.2f}'.format(salario))

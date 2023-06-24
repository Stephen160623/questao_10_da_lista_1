# Atribuição de variáveis

# Entrada de dados

cap = float(input("Valor do capital: "))
t = float(input("Prazo do investimento em anos: "))
r = float(input("Taxa de juros em percentagem: "))

# Processamento de dados

v = cap*(1+(r/100))**t

# Saída de dados

print("O valor capitalizado é R$%.2f" % v)
senha = 1234
while senha == 1234:
    tentativa = int(input(f"Digite a senha: "))
    if tentativa != senha:
        print(f"|acesso negado| tente denovo...")
    else:
        print(f"|acesso liberado|")
        break
# Exercicio de soma 
i = 0
soma = 0
while i < 150:
    i = i + 1
    soma = soma + i
print(f"{soma}")
    
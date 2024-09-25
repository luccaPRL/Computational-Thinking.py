# i = 0
# pares = 0
# impar = 0
# while i < 10:
#     num = int(input(f"Digite o seu numero:\n-->"))
#     if num%2==0:
#         pares = pares + 1
#         i = i + 1
#     else:
#         impar = impar + 1
#         i = i + 1
#     print(f"os seguintes numeros são pares {pares} e os seguintes são impares {impar}")

# Exercicio senha limite repetição

# tentativa = 1
# maxt = 4
# senha_cadastrada = 1234
# senha_tentativa = int(input("Digite sua senha"))
# while senha_cadastrada != senha_tentativa and tentativa < maxt:
#     print(f"vc é hacker só mais {maxt - tentativa}!!!")
#     senha_tentativa = int(input("Digite sua senha"))
#     tentativa += 1
# if senha_cadastrada == senha_tentativa:
#     print(f"acesso liberado")
# else:
#     print("vasco")

vinho1 = 'chapinha'
vinho2 = 'pérgola'
vinho3 = 'catuaba'

opcao = input(f"Digite qual opção vc deseja:\n-->")

while not (opcao == vinho1 or opcao == vinho2 or opcao == vinho3):
    print("invalido")
    opcao = input(f"Digite qual opção vc deseja:\n-->")
print(opcao)
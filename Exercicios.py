# # # ================================================================================================
# EXERCICIO 1

a = float(input(f"digite um numero"))
b = float(input(f"digite um numero"))


if a > b:
     print(f"{a}")
else:#     b > a
     print(f"{b}")


# # # ================================================================================================
# EXERCICIO 2

data = int(input("digite o ano de nascimento:"))

if data < 2006:
    print(f"pode votar e dirigir")
else:
    data >= 2006
    print(f"não pode votar e nem dirigir")


# # # ================================================================================================
# EXERCICIO 3
tentativa = int(input(f"Digite a senha:"))

senha = 1234

if tentativa == senha:
    print(f"...Acesso Permitido...")
else:
    print(f"...Acesso Negado...")
    
    
# # # ================================================================================================
# EXERCICIO 4
qtd = int(input(f"digite quantas maças quer comprar"))
preco = 0.30
if qtd >= 12:
    preco = 0.25
total = preco*qtd
print(f"você gastou R${total:.2f} em {qtd} maçãs a R${preco:.2f} cada")


# # ================================================================================================
# EXERCICIO 5

a = int(input(f"Digite o primeiro valor:"))
b = int(input(f"Digite o segundo valor:"))
c = int(input(f"Digite o terceiro valor:"))

if a <= b and a <= c:
    if b <= c:
        print(f"{a},{b},{c}")
    else:
        print(f"{a},{c},{b}")
elif b <= a and b <= c:
        if a <= c:
            print(f"{b}, {a}, {c}") 
        else:
             print(f"{b}, {c}, {a}") 
else:
        if a <= b:
            print(f"{c}, {a}, {b}") 
        else:
             print(f"{c}, {b}, {a}") 


# # ================================================================================================
# EXERCICIO 6
Sexo = str(input(f"Escolha seu Sexo:"))
altura = float(input(f"Digite sua altura:"))

if Sexo == "Masculino":
    print(f"seu peso é: {altura * 72.7 -58:.2f}")
else:
    Sexo == "feminino"
    print(f"seu peso ideal é: {altura * 62.1 -44.7:.2f}")

# # ================================================================================================
# EXERCICIO 7 E 8
lados = int(input(f"DIGITE A QUANTIDADE DE LADOS:"))
if lados < 3:
    print(f"não é um poligono!")
elif lados < 5:
    print(f"não é um poligono!")
else:
    comprimento = float(input(f"Diga o tamanho do lado"))
    area = lados*comprimento
    if lados == 3:
        forma = 'triangulo'
    elif lados == 4:
        forma = 'quadrado'
    else:
        forma = 'Pentagono'
print(f"O poligono é um {forma} e tem {area}cm")
# # ================================================================================================
# EXERCICIO 9

a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))

if a > b and c:
    print(f"{a}")
elif b > a and c:
    print(f"{b}")
else:
    print(f"{c}")

    
# # ================================================================================================
# EXERCICIO EXTRA

x = (input(f"Digite sua letra"))

if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
    print(f"Vogal")
else:
    print(f"consoante")


# # ================================================================================================
# EXERCICIO 10
while True:
    Lado_a = float(input(f"Digite o valor do Primeiro lado:"))
    Lado_b = float(input(f"Digite o valor do segundo lado:"))
    Lado_c = float(input(f"Digite o valor do terceiro lado:"))

    print(f'='*26)

    if (Lado_a + Lado_b > Lado_c) and (Lado_a + Lado_c > Lado_b) and (Lado_b + Lado_c > Lado_a):
        if Lado_a == Lado_b == Lado_c:
            print(f"isso é um Triângulo Equilátero")
        elif Lado_a == Lado_b or Lado_b == Lado_c or Lado_a == Lado_c:
            print(f"isso é um Triângulo Isósceles")
        else:
            print(f"isso é um Triângulo Escaleno")
    else:
        print("Os valores fornecidos não formam um triângulo válido.")

    print(f'='*26)

    repetir = int(input(f"Deseja fazer outra verificação. \n1)Sim \n2)Não"))

    print(f'='*26)

    if repetir != 1:
        print(f"Encerrando...")
        break
    else:
        print(f"Recomeçando")

    print(f'='*26)

# # ================================================================================================
# EXERCICIO 11

# Versão feita sozinho apenas consultando ajuda em alguns site

anguloa = float(input(f"Digite o primeiro angulo:"))
angulob = float(input(f"Digite o segundo angulo:"))
anguloc = float(input(f"Digite o terceiro angulo:"))

if anguloa + angulob + anguloc == 180:
    if anguloa == 90 or angulob == 90 or anguloc ==90:
        print(f"é um Triângulo Retângulo")
    elif anguloa > 90 or angulob > 90 or anguloc > 90:
        print(f"é um Triângulo Obtusângulo")
    else:
        print(f"é um Triângulo Acutângulo")
else:
    print(f"Os valores não formam um triangulo")

#Versão aprimorada pelo GPT

# Recebe os ângulos do usuário

anguloa = float(input("Digite o primeiro ângulo: "))
angulob = float(input("Digite o segundo ângulo: "))
anguloc = float(input("Digite o terceiro ângulo: "))

# Verifica se os ângulos são válidos
if anguloa <= 0 or angulob <= 0 or anguloc <= 0:
    print("Os ângulos devem ser positivos.")
elif anguloa + angulob + anguloc != 180:
    print("Os valores não formam um triângulo.")
else:
    # Determina o tipo do triângulo
    if anguloa == 90 or angulob == 90 or anguloc == 90:
        print("É um triângulo retângulo.")
    elif anguloa > 90 or angulob > 90 or anguloc > 90:
        print("É um triângulo obtusângulo.")
    else:
        print("É um triângulo acutângulo.")

# # ================================================================================================


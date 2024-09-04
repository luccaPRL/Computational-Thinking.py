# # #  a = float(input(f"digite um numero"))
# # #  b = float(input(f"digite um numero"))


# # #  if a > b:
# # #      print(f"{a}")
# # #  else:#     b > a
# # #      print(f"{b}")


# # # ================================================================================================


# # data = int(input("digite o ano de nascimento:"))

# # if data < 2006:
# #     print(f"pode votar e dirigir")
# # else:
# #     data >= 2006
# #     print(f"não pode votar e nem dirigir")


# # # ================================================================================================

# # senha = float(input(f"Digite a senha:"))

# # if senha == 1234:
# #     print(f"ACESSO PERMITIDO")
# # else:
# #     senha != 1234
# #     print(f"ACESSO NEGADO")
    
    
# # # ================================================================================================

# maças = int(input(f"Quantas Maças Você Deseja:"))

# if maças <= 12:
#     (print(f"{maças*0.30}"))
# else:
#     (print(f"{maças*0.25}"))


# # ================================================================================================


#  def ordenar_tres_valores(a, b, c):
#    if a <= b and a <= c:
#          if b <= c:
#              return a, b, c
#         else:
#              return a, c, b
#      elif b <= a and b <= c:
#          if a <= c:
#             return b, a, c
#         else:
#              return b, c, a
#      else:
#         if a <= b:
#             return c, a, b
#         else:
#             return c, b, a


#  try:
#      a = float(input("Digite o primeiro valor: "))
#      b = float(input("Digite o segundo valor: "))
#      c = float(input("Digite o terceiro valor: "))
    
    
#     ordem = ordenar_tres_valores(a, b, c)
#     print(f"Os valores em ordem crescente são: {ordem[0]}, {ordem[1]}, {ordem[2]}")
# except ValueError:
#     print("Por favor, insira apenas números válidos.")

# # ================================================================================================

# Sexo = str(input(f"Escolha seu Sexo:"))
# altura = float(input(f"Digite sua altura:"))

# if Sexo == "Masculino":
#     print(f"seu peso é: {altura * 72.7 -58}")
# else:
#     Sexo == "feminino"
#     print(f"seu peso é: {altura * 62.1 -44.7}")



# lados = int(input(f"DIGITE A QUANTIDADE DE LADOS:"))
# medida = float(input(f"DIGITE OS CENTIMETROS DOS LADOS"))

# if lados == 3:
#     print(F"Triangulo")
#     print(f"O valor da área é: {medida*medida/2}")
    
# elif lados == 4:
#     print(f"Quadrado")
#     print(f"O valor da área é: {medida**2}")
    
# elif lados < 3:
#     print(f"não é n poligono")
    
# elif lados > 5:
#     print(f"poligono não encontrado")
    
# else:
#     lados == 5
#     print(f"Pentagono")
#     print(f"vai ter area n zé")
    
# # ================================================================================================

# a = float(input("Digite o primeiro valor: "))
# b = float(input("Digite o segundo valor: "))
# c = float(input("Digite o terceiro valor: "))

# if a > b and c:
#     print(f"{a}")
# elif b > a and c:
#     print(f"{b}")
# else:
#     print(f"{c}")a

    
# # ================================================================================================


x = (input(f"Digite sua letra"))

if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
    print(f"Vogal")
else:
    print(f"consoante")
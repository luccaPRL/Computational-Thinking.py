######## Exercicios 1 ########

# nota = int(input(f"Digite uma nota entre 1 a 10:\n-->"))
# while not (1 <= nota <= 10):
#     print("Nota inválida. A nota deve estar entre 1 e 10.")
#     nota = int(input("Digite uma nota entre 1 a 10:\n--> "))
# print(f"A nota informada foi: {nota}")

######## Exercicios 2 ########

# nome = str(input(f"Digite seu nome: \n-->"))
# while len(nome) <= 2:
#     print(f"o nome: {nome} é muito pequeno e não é considerado um nome")
#     nome = str(input(f"Digite seu nome: \n-->"))
# idade = int(input(f"Digite sua idade:\n -->"))
# while not (0 <= idade <= 150):
#     print(f"a idade: {idade} é invalida.")
#     idade = int(input(f"Digite sua idade:\n -->"))
# salario = float(input(f"Digite seu salario: \n-->"))
# while salario <= 0:
#     print(f"o salario: {salario} não é valido")
#     salario = float(input(f"Digite seu salario: \n-->"))
# sexo = input("Qual é o seu sexo: \n F = Feminino \n M = Masculino \n--> ")
# while sexo != 'F' and sexo != 'M':
#     print(f"O sexo: {sexo} não é válido.")
#     sexo = input("Qual é o seu sexo: \n F = Feminino \n M = Masculino \n--> ")
# if sexo == 'F':
#     sexo = 'Feminino'
# else:
#     sexo = 'Masculino'
# ec = input(f"Digite o seu Estado Civil:\nS = Solteiro\nC = Casado\nV = Viúvo\nD = Divorciado\n--> ")
# while ec not in ['S', 'C', 'V', 'D']:
#     print(f"O estado civil: {ec} não é válido.")
#     ec = input(f"Digite o seu Estado Civil:\nS = Solteiro\nC = Casado\nV = Viúvo\nD = Divorciado\n--> ")
# if ec == 'S':
#     ec = 'Solteiro'
# elif ec == 'C':
#     ec = 'Casado'
# elif ec == 'V':
#     ec = 'Viúvo'
# else:
#     ec = 'Divorciado'
# print(f"Seu Nome é: {nome} \nSua idade é: {idade}anos \nSeu salario é:R$ {salario:.2f} \nSeu sexo é: {sexo} \nSeu Estado Civil é:{ec}")

######## Exercicio 4 ########

# soma = 0
# i = 0
# while i < 5:
#     num = input(f"Digite o {i+1} numero: \n-->")
#     while not num.isnumeric():
#         num = input(f"Digite {i+1} numero: \n-->")
#     num = int(num)
#     soma += num
#     i  += 1
# media = soma/i
# print(f"a soma dos valores foi {soma} e a media foi {media}")



######## Exercicio 5 ########

# num1 = int(input("Digite o primeiro número inteiro: "))
# num2 = int(input("Digite o segundo número inteiro: "))
# if num1 > num2:
#     num1, num2 = num2, num1
# i = num1 + 1
# while i < num2:
#     print(i)
#     i += 1

######## Exercicio 6 ########


# user = (input("Digite o seu usuario: \n-->"))
# senha = input("digite sua senha: \n -->")
# while user == senha:
#     senha = input("digite sua senha diferente de seu usuario: \n -->")
# print(f"O usuario foi definido como {user} e a senha como {senha}")

######## Exercicio 7 ########


#  i = 1
# num = (int(input(f"Digite o numero que deseja ver a tabuada: \n-->")))

# while i < 11:
#     numb = num * i
#     print(f"{num} x {i} = {numb}")
#     i+=1


######## Exercicio 8 ########
# a=1
# b=1
# qtd = 10
# n=0
# print(a,b,end = ' ')
# while n < qtd:
#         c=a+b
#         a=b
#         b=c
#         print(c,end = ' ')
#         n+=1


######## Exercicio 9 ########
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
# print(f"os seguintes numeros são pares {pares} e os seguintes são impares {impar}")

######## Exercicio 10 ########
#### Def #####
# def calcular_fatorial(numero):
#     resultado = 1
#     for i in range(1, numero + 1):
#         resultado *= i
#     return resultado

# numero = int(input(f"Qual valor vc deseja saber o fatorial:\n--->"))
# resultado = calcular_fatorial(numero)
# print("O fatorial de", numero, "é", resultado)

# i = 1
# mult = 1
# qtd = int(input(f"Qual valor vc deseja saber o fatorial:\n--->"))
# while i < qtd:
#     i = i + 1
#     mult=mult*i
# print(f"{mult}")



######## Exercicio 11 ########
# i=1
# num = int(input("digite um valor"))
# while True:
#     i+=1
#     if num % i == 0:
#         print("Não é primo")
#     elif i >= num**(1/2):
#         print("é primo")
#         break




######## Exercicio 12 ########
# soma = 0
# i = 0
# media = 0
# while i < 3:
#     num = input(f"Digite o {i+1} numero: \n-->")
#     while not num.isnumeric():
#         num = input(f"Digite {i+1} numero: \n-->")
#     num = int(num)
#     soma += num
#     i+=1
# media=soma/i
# print(media)
######## Exercicio 12 ########

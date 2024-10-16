'''lista = [ 'André', 'Caio Oliveira', 'Luciano', 'Yan','Danilo', 'Caio Figueiredo']
for prof in lista:
    if prof == 'Danilo':
        print('Achei')

for i in range(len(lista)):
    print(f"Vou ver se o {lista[i]} é o Danilo")
    if lista[i] == 'danilo':
        print(f"Achei")
        print(f"O {lista[i]} esta no indice {i}")

lista = [ 'André', 'Caio Oliveira', 'Luciano', 'Yan','Danilo', 'Caio Figueiredo']
subt = ['maluco', 'um', 'maromba', 'pica', 'Thor', 'dois',]
for i in range(len(lista)):
    print(f"O prof {lista[i]} é {subt[i]}.")















valores = [50, 70 ,1000000, 10 ,20]
carros = ['up', 'kombi', 'celtinha brabo', 'gol', 'uno',]
local_maior = 0
maior = valores[local_maior]
for i in range(len(valores)):
    print(f"vou testar se o {valores[i]} > {maior}")
    if valores[i] > maior:
        print(f"Deu certo, então agora o maior será {valores[i]}")
        maior = valores[i]
        local_maior = i
print(f"O carro mais caro é o {carros[local_maior]} e custa R${valores[local_maior]}")




















lista = []
for i in range(10):
    lista.append(i)
    print(lista)






def checa_numero(msg,msg_erro):
    num = input(msg)
    while not num.isnumeric():
        print(msg_erro)
        num = input(msg)
    return int(num)


def forca_opcao(lista_opcoes,msg,msg_erro):
    opcao =input(msg)
    while opcao not in lista:
        print(msg_erro)
        opcao = input(msg)
    return opcao

lista = ['chapinha', 'Sangue de Boi', 'Pérgola',]
escolha = forca_opcao(lista, "qual vinho vc quer?", "vinho não existe!!!!")
sim_ou_nao = ['sim', 'nao',]
escolha = forca_opcao(sim_ou_nao, "vc deseja continuar comprando", "Invalido!!!")
print(escolha)


ano = checa_numero("digite seu ano de nascimento:", "Deve ser ano!")
print(f"vc digitou o ano:{ano}")
qtd = checa_numero("digite a qtd de garrafas:", "Deve ser qtd!")
print(f"vc quer {qtd} garrafas.")











def media_notas(notas):
    soma = 0
    for num in notas:
        soma+= num
    media = soma/len(notas)
    return media

lista=[0, 8, 5, 9, 10, 7, 2]
media =media_notas(lista)
print(media)
lista=[9, 5, 5, 7, 10, 9, 4]
media =media_notas(lista)
print(media)


Exercicios da lista
Exercicio 1
'''
def soma_numeros():
    soma = 0
    for num in lista:
        soma += num
    return soma
lista=[10, 6, 7 , 8, 9]
valor = soma_numeros()
print(valor)
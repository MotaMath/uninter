# -------------------------- Shortcut to add/remove comments: Ctrl + / -----------------------

#triangulo
# a = int(input('Digite o lado A do triangulo: '))
# b = int(input('Digite o lado B do triangulo: '))
# c = int(input('Digite o lado C do triangulo: '))
#
# if a > 0 and b > 0 and c > 0:
#     if a + b > c and a + c > b and b + c > a:
#         if a != b and a != c and b != c:
#             print('Triangulo escaleono')
#         else:
#             if a == b and b == c:
#                 print('Triangulo equilatero')
#             else:
#                 print('Triangulo isosceles')
#     else:
#         print('Ao menos um dos valores indicados nao servem para  formar um triangulo')
# else:
#     print('Ao menos um dos valores indicados nao servem para  formar um triangulo')

#calculadora
# valor1 = float(input('Qual valor: '))
# valor2 = float(input('Qual o valor: '))
#
# adicao = valor1 + valor2
# subt = valor1 - valor2
# mult = valor1 * valor2
# div = valor1 / valor2
#
# res = input('Voce quer [1] somar, [2] subtrair, [3] multiplicar ou [4] dividir? ')
#
# if res == '1':
#     print(adicao)
# elif res == '2':
#     print(subt)
# elif res == '3':
#     print(mult)
# elif res == '4':
#     print(div)
# else:
#     print('Opcao invalida')

# desconto
# valor = int(input('Qual o valor total da compra? '))
# tipo = input('Voce quer pagar a [1]vista, [3]3X, [5]5X ou [10]10X? ')
#
# if tipo == '1':
#     vista = valor * 0.95
#     print('Voce obteve um desconto de 5%, total a pagar R$ {}.'.format(vista))
# elif tipo == '3':
#     em3 = valor / 3
#     print('Voce vai pagar R$ {} em 3 vezes de R$ {} por mes.'.format(valor, em3))
# elif tipo == '5':
#     em5 = valor * 1.02 / 5
#     print('Voce vai pagar R$ {} em 5 vezes de R$ {} por mes. Adicionado 2% de juros.'.format(valor, em5))
# elif tipo == '10':
#     em10 = valor * 1.08 / 10
#     print('Voce vai pagar R$ {} em 10 vezes de R$ {} por mes. Adicionado 8% de juros.'.format(valor, em10))
# else:
#     print('Operacao inexistente.')

#expressoes booleanas
# x=  1 +2<4
# print(x)
#
# y = 7 // 3 == 1 + 1
# print(y)
#
# xx = 3**2 + 4**2 == 25
# print(xx)
#
# yy = 2 + 4 + 6 > 12
# print(yy)
#
# xxx = 1387 % 19 == 0
# print(xxx)
#
# yyy = 31 % 2  == 0
# print(yyy)
#
# z = 29 < 30
# print(z)

#login
# print('Crie sua conta')
# user = input('Nome do usuario: ')
# password = input('Nova senha: ')
#
# print('Conta criada com sucesso!')
#
# while True:
#     login = input('Usuario: ')
#     senha = input('Senha: ')
#     if user == login and password == senha:
#         print('Bem-vindo!')
#         break
#     else:
#         print('Usuario e senha errados! Tente novamente!')
#         continue

# #kill a rat
# print('Kill the rat')
# hp = 40
# while hp >= 1:
#     question = input('Press a to attack and b to defend: ')
#     if question == 'a':
#         print('You hit 10.')
#         hp -= 10
#     elif question == 'b':
#         print('You defend.')
#         print('{} HP left.'.format(hp))
#     else:
#         print('Wrong selection.')
#         continue
#
# print('Rat 0 HP, you killed the rat.')

#foguete
# x = 10
# while x > 0:
#   print(x)
#   x -= 1
# print('Fogo')

#foguete with for
# for i in range(10,0, -1):
#     print(i)
# print('Fogo!')

#tabuada
# print('Tabuada -- Multiplicação')
# x = int(input('Qual numero voce quer? '))
#
#
# while x <= 10:
#   print('Tabuada do numero {}.'.format(x))
#   y = 1
#   while y <= 10:
#     print('{} x {} = {}'.format(x, y, x * y))
#     y += 1
#   break

#taboada with for
# tabuada = int(input('Digite um valor: '))
# n = int(input('Digite um valor: '))
#
# for i in range(1, n + 1, 1):
#     print('{} x {} = {}'.format(tabuada, i, tabuada * i))

#descubra a media
# media = 0
# count = 1
#
# while count <= 6:
#     nota = float(input('Digite a nota da materia {}:. '.format(count)))
#     media += nota
#     count += 1
# print('Sua media é {}.'.format(media / 6))

#custo ticket disney. menor que 4 anos paga 100, menor que 16 paga 150, resto 200
# print('Welcome to Disney World!')
# print('-')
# member = 0
# ticket = 0
# total = 0
#
# while True:
#     age = input('What is the age of each members of the party?(Press [0] to exit) > ')
#     if age == '0':
#         print('Good Bye.')
#         break
#     age = int(age)
#     member += 1
#     if age <= 4:
#         ticket += 100
#     else:
#         if age <= 16:
#             ticket += 150
#         else:
#             ticket += 200
#
# print('You purchased {} tickets to Disney World.'.format(member))
# print('Total : ${}'.format(ticket))
# print('Enjoy your day.')

#parametros e funcoes criando bordas
# def board(x):
#     size = len(x)
#     if size:
#         print('|' , '-' * size , '|')
#         print('|' , x , '|')
#         print('|' , '-' * size , '|')
#
# board('Hello, World!')
# board('Name:')
# board('My name is Matheus Chaves Mota Ribeiro!')

#Dica: para realizar o print sem quebrar a linha, utilize um parâmetro
#opcional end='' da função print. Exemplo: print(x, end='').
# x = 2
# y = 3
# print(x, y, end='')

#Variavel global e local
# x e y foi definido na variavel global, y teve outra variavel criada localmente
# quando chamado x usa a variavel global, y definiu uma variavel local,
# dentro da função z foi definido como global
# def bota():
#     global z
#     y = 2
#     z = 3
#     print(x)
#     print(y)
#     print(z)
#
# x = 1
# y = 'mae'
# z = 4
# bota()

# #try except
# while True:
# 	try:
# 		x = int(input('Por favor digite um número: '))
# 		break
# 	except ValueError:
# 		print('Oops! Número inválido. Tente Novamente...')

#Para pegar um nomero do usuario
# def idade():
#     while True:
#         try:
#             int(input('Digite sua idade: '))
#             print('Correct')
#             break
#         except:
#             print('Invalido, digite um numero')
#         finally: #sempre repete
#             print(' ')
#
# idade()

#validar numero
# while True:
#     num = input("Please enter a number ")
#     try:
#         val = int(num)
#         print("Input is an integer number.")
#         print("Input number is: ", val)
#         break;
#     except ValueError:
#         try:
#             float(num)
#             print("Input is an float number.")
#             print("Input number is: ", val)
#             break;
#         except ValueError:
#             print("This is not a number. Please enter a valid number")

#list print
# a = [1, 2, 3, 4, 5]
#
# for x in range(len(a)):
#     print(a[x], end=' ')
#
# #Outro
#
# a = ['Mae', 'Pai', 1, 2, 3]
#
# print(*a)

#criando um [S/N] input
# while True:
#     pergunta = input('Quer contuniar? [S/N]: ')
#     if pergunta in 'Nn':
#         break
#     if pergunta not in 'Ss':
#         print('Escolha S ou N')
#         continue
#     print('Continuando')
# print('Adeus')


#Calculator
# def calculate(n1,n2,op):
#     if op == '+':
#         result = n1+n2
#     elif op == '-':
#         result = n1-n2
#     elif op == '*':
#         result =  n1*n2
#     elif op == '/':
#         result = n1/n2
#     elif op=='^':
#         result =  n1**n2
#     else:
#         raise ValueError('Invalid operator')
#
#     if result.is_integer():
#         result = int(result)
#
#     return result
#
# continue_calculating = True
# while continue_calculating is True:
#     number1 = float(input('Enter first number: '))
#     op = input('Enter operator (+,-,*,/,^): ')
#     number2 = float(input('Enter second number: '))
#     print(number1,op,number2)
#     result=calculate(number1,number2,op)
#     print('=',result)
#     yes_or_no = input('Continue? (y/n): ')
#     if yes_or_no == 'n':
#         continue_calculating = False


#F1 car
# class Car:
#
#     def __init__(self, speed=0):
#         self.speed = speed
#         self.odometer = 0
#         self.time = 0
#
#
#     def accelerate(self):
#         self.speed += 5
#
#     def brake(self):
#         self.speed -= 5
#
#     def step(self):
#         self.odometer += self.speed
#         self.time += 1
#
#     def average_speed(self):
#         return self.odometer / self.time
#
#
# if __name__ == '__main__':
#
#     my_car = Car()
#     print("I'm a car!")
#     while True:
#         action = input("What should I do? [A]ccelerate, [B]rake, "
#                         "show [O]dometer, or show average [S]peed?").upper()
#         if action not in "ABOS" or len(action) != 1:
#             print("I don't know how to do that")
#             continue
#         if action == 'A':
#             my_car.accelerate()
#             print("Accelerating...")
#         elif action == 'B':
#             my_car.brake()
#             print("Braking...")
#         elif action == 'O':
#             print("The car has driven {} kilometers".format(my_car.odometer))
#         elif action == 'S':
#             print("The car's average speed was {} kph".format(my_car.average_speed()))
#         my_car.step()
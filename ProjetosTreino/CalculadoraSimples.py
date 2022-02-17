#----------Import----------
#import biblioteca(completo)
#from biblioteca import livro(especifico)
import os
from math import sqrt,pow,factorial
#----------Funcoes----------
def titulo(msg):
    print('-'*30)
    print(msg)
    print('-'*30)
#----------Programa----------
titulo('CALCULADORA SIMPLES')
#Menu
print('1 Para SOMA')
print('2 Para SUBTRACAO')
print('3 Para MULTIPLICACAO')
print('4 Para DIVISAO')
print('5 Para POTENCIA')
print('6 Para FATORIAL')
print('7 Para RAIZ QUADRADA')
#Variaveis
op = input('Qual operaçao deseja executar? ')
p1 = input('\nQual p1? ')
p2 = input('Qual p2? ')
#Controle
if op == '1':
    r=int(p1+p2)
    print('{} + {} = {}'.format(p1,p2,r))
elif op == '2':
    print('{} - {} = {}'.format(p1,p2,p1-p2))
elif op == '3':
    print('{} x {} = {}'.format(p1,p2,p1*p2))
elif op == '4':
    print('{} ÷ {} = {}'.format(p1,p2,p1/p2))
elif op == '5':
    print('{} ^ {} = {}'.format(p1,p2,pow(p1,p2)))
elif op == '6':
    print('{}!  = {}'.format(p1,factorial(p1)))
    print('{}! = {}'.format(p2,factorial(p2)))
elif op == '7':
    print('√{} = {}'.format(p1,sqrt(p1)))
    print('√{} = {}'.format(p2,sqrt(p2)))
else :
    print ('Valor  invalido')
print('fim')
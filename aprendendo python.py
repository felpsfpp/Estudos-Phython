# -*- coding: utf-8 -*-
print("olá mundo!")

#operadores matematicos

# + adiçao
# - subtraçao
# * multiplicaçao
# / divisao
# ** exponenciaçao
# % modulo
print (2 + 2)
print(2 - 2)
print(2 * 2)
print(2 ** 3) #2 elevado a 3
print(10 / 3)
print(10 % 3) #ver o resto da operação


#variaveis

minha_variavel = "olá mundo"
print(minha_variavel)

#como funcionam as variaveis
var1 = 1 #v ariavel inteira
var2 = 1.1 # variavel float
var3 = "eu sou uma string" # variavel string
var4 = True #verdadeiro variave booleana
var4 = False #falso variavel booleana

print(var1)
print(var2)
print(var3)
print(var4)

#operadores relacionais
# == igual
# != diferente
# > maior
# < menor
# >= maior ou igual
# <= menor igual

x = 2
y = 3
print(x == y)
print(x < y)
print(x > y)
print(x <= y)
print(x >= y)

#operador de modulo

# se eu quero dividir 10 por 3, o resultado seria 3.3333333
print(10/3)
# 3.33333333

# se quiséssemos apenas os números inteiros, 10 / 3 seria igual a 3 e teríamos o resto 1

# resto da divisao de 10 por 3
print(10%3)
# 1 

x = 10
if(x % 2 == 1):
    print("numero par")
else:
    print("numero impar")

#operadores logicos
# AND duas condiçoes sejam verdadeiras
# OR pelo menos uma condiçao seja verdadeira
# NOT inverte o valor

x = 2
y = 3
z = 3

print(x == y and x == z)
print(x == y or y == z)

#comandos condicionais

x = 1
y = 100000000

if x > y:
    print("x é maior que y")

if y > x:
    print("y é maior que x")

x = 1
y = 2
if x < y and x < 0:
    print("x eh negativo e menor que y")
if x > y and x > 0:
    print("x eh positivo e maior que y")
if x < y and x > 0:
   print("x eh positivo e menor que y")


x = 1
y = 2

if x > y:
    print("x maior que y")
else:
    print("x nao é maior que y")



x = 1
y = 2

if x == y:
    print("numeros iguais")
elif x < y:
    print("x menor que y")
elif y > x:
    print("y maior que x")
else:
    print("numeros diferentes")

#laços de reptição

x = 1

while x < 10:
    print(x)
    x = x + 1

#laço for

lista1 = [1,2,3,4,5]
lista2 = ["ola","mundo","!"]
lista3 = [0,"ola","biscoito","bolacha",9.99]

for i in lista3:
    print(i)

#range

for i in range(10,20,2):
    print(i)

#imput

numero = input("digite um numero: ")
print("o numero digitado é:")
print(numero)

nome = input("digite seu nome: ")
print("bem=vindo "+nome)

#listas 
frutas = ["morango","uva","pera","tomate"]
frutas.append("abacaxi")
for f in frutas:
    print(f)
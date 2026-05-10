# -*- coding: utf-8 -*-
"""
Calculadora
Autor: Felipe Pinheiro
Função fazer contas: soma, divisão, multiplicaçao, subtração
"""

print("Calculadora V1.0")

sair = False

while sair == False:

    num1 =  input("digite o primeiro número: ")
    num1 = int(num1)
    operador = input("digite o operador (+ - / *): ")
    num2 = input("digite o segundo número: ")
    num2 = int(num2)

    # + soma
    if operador == "+":
        operaçao = num1 + num2
    # - subtração
    if operador == "-":
        operaçao = num1 - num2
    # / divisão
    if operador == "/":
        operaçao = num1 / num2
    # * multiplicação
    if operador == "*":
        operaçao = num1 * num2

    print("Resultado: ", operaçao)

    saidacalc = input("deseja sair? (n/s): ")
    if saidacalc == "s":
        sair =  True
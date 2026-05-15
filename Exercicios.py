# EXERCICIOS DE PYTHON PROF FALABELA

# EX1
# Um aluno tem 10 anos. Armazene essa idade em uma variável
# e exiba seu tipo.

idade = 10
print("Tipo:", type(idade))

# EX2
# A temperatura medida é 23.5°C.
# Armazene esse valor e mostre seu tipo.

temperatura = 23.5
print('\n' "Tipo:", type(temperatura))

# EX3
# Crie um número complexo representando uma impedância elétrica
# de 5 + 8j e mostre sua parte real.

impedancia = 5 + 8j
print('\n' "Parte Real:", impedancia.real)

# EX4
# Mostre a parte imaginária do número complexo
# criado no exercício anterior.

print('\n' "Parte Imaginária:", impedancia.imag)

# EX5
# Declare uma variável chamada "populacao"
# com o valor 8_000_000_000 (8 bilhões)
# e mostre seu tipo.

população = 8000000000
print('\n' "Tipo:", type(população))

# EX6
# Verifique se o número 7 é do tipo int
# usando a função type().

numero = 7
print('\n' "Tipo:", type(numero))

# EX7
# Crie uma variável chamada "aprovado"
# com o valor booleano True e mostre seu tipo.

aprovado = True
print('\n' "Tipo:", type(aprovado))

# EX8
# Some True e False e mostre o resultado
# e também o tipo do resultado.

Verdade = True
Falsa = False
resultado = Verdade + Falsa
print('\n' "Resultado foi de:", resultado)
print("Tipo:", resultado , '\n')

# EX9
# Pesquise e mostre qual é o valor máximo
# que um número inteiro pode ter em Python.

import sys
print(sys.maxsize , '\n')

# EX10
# Mostre a representação em binário
# do número 10 usando uma função do Python.

num = 10
Binario = bin(10)
print(Binario , '\n')
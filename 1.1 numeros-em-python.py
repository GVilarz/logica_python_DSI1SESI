# AULA COMPLETA: NUMEROS EM PYTHON

"""
Vamos aprender:
1- Tipos numericos
2- Conversões de tipos
3- Hierarquia númerica
4- Operações matemáticas
5- Coerção de tipos
6- Verificação de tipos
7- Entrada de dados
"""
# PASSO 01 - TIPOS NUMERICOS

# int -> Inteiros
# float -> números com casas decimais
# complex -> números complexos (usado em matemática/engenharia)

print("===== TIPOS NUMÉRICOS =====")

# EXEMPLO 01 - NUMERO INTEIRO

# criamos uma variavel chamada "numero_inteiro"
numero_inteiro = 10
print ("Valor:", numero_inteiro)
# type() mostra qual é o tipo da variável  
print("Tipo:", type(numero_inteiro))
print ("------------------")

# EXEMPLO 02 - NUMERO DECIMAL

numero_decimal = 3.14

print ("Valor:", numero_decimal)

print ("Tipo:", type(numero_decimal))
print ("------------------")

"""
 EXEMPLO 03 - NUMEROS COMPLEXOS
 Um número complexo possui duas partes:
 Parte real (Número normal)
 Parte imaginária (Multiplicada por j)

 Estrutura geral:
 numero = a + bj

 a = parte real
 b parte imaginária
 j = unidade imaginária
"""

numero_complexo = 2 + 3j

print ("Valor:", numero_complexo)
print ("Tipo", type(numero_complexo))

print ("------------------")

# EXEMPLO 03 - ACESSANDO CADA PARTE DO NÚMERO

# .real retorna a parte real
print ("Parte Real:", numero_complexo.real)
print ("------------------")

# .imag retorna a parte imaginaria
print ("Parte imaginaria:", numero_complexo.imag)
print("\n\n")

"""
===================
PASSO 02 - CONVERSÃO TIPOS
===================

Exemplo Clássico:
Dados vindos do usuário são texto (string), muitas vezes é necessario converter eles.
"""

print("=========== Conversões ==============")

# float -> int

valor = int(3.9)

print("int(3.9):", valor)
print("Tipo:", type(valor))


#string -> int
valor1 = "10"
print(type(valor1))


valor2 = int("10")
print('int("10"):', valor)
print("tipo:", type(valor2))

#int --> float
valor3 = float(10)
print("float(10):", valor3)
print("Tipo:", type(valor3))
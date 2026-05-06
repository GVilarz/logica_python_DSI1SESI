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
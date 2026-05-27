# Aula Completa - Strings em Python

"""
- Criação de strings
- strings multilinha
- indices e slices
- Operações com strings
- Imutabilidade
- Métodos úteis
- Formatação de texto
- Unicode e bytes

-------------------------------------------
(1) Criação de Strings
-------------------------------------------
Strings são texto em python
Podem ser criadas usando aspas simples ou duplas

"""
texto1 = "Python"
texto2 = 'Curso de Python'
texto3 = "Copa 'padrao fifa'"
texto4 = 'copa "padrao fifa"'

print(texto1, texto2, texto3, texto4)

# Python permite misturar aspas simples e duplas, dentro das strings sem precisar escapar caracteres

#-----------------------------------------------
# (2) Strings Multilinha
#-----------------------------------------------
# Usando tres aspas (""" ou ''') para criar textos que ocupam varias linhas

menu = """\
Uso: programa [OPÇÕES]
-h Exibe ajuda
-U Url do dataset
"""
print(menu)

# Esse formato é muito usado para:
# - Menus
# - Documentação
# - textos longos

#-----------------------------------------------
# (3) Concatenação Automática
#-----------------------------------------------
# Quando duas strings aparecem lado a lado, o python junta automaticamente

texto = ("copa" " 2026 " "Neymar é show mesmo?")
print(texto)

#-----------------------------------------------
# (4) Strings Como Sequências
#-----------------------------------------------
# Uma string funciona como uma sequência de caracteres, cada caractere possui um indice

st = "maracana"
print("Primeira letra:", st[0])
# só exibir a letra M

print ("Ultima Letra:", st[-1])

print ("Trecho 1:4", st[1:4])

print ("Do inicio até 3:", st[:3])

print ("Do 2 até o fim:", st[2:])

print ("tamanho", len(st))

#-----------------------------------------------
# (5) Operações com Strings
#-----------------------------------------------
# Python permite várias operações com strings

print("m" in st)
# Significa que a letra "m" existe dentro da string

print("x" not in st)
# Significa que "x" não existe na string

print("m" * 3)
# Multiplicação repete a string

print("m" + "aracana " + texto1)
# Operador + concatena strings

#-----------------------------------------------
# (6) Strings são Imutáveis
#-----------------------------------------------
# Strings não podem ser alternadas diretamentes!!!
# Isso significa que o conteúdo original não muda.
# O que acontece é a criação de uma nova string.

texto5 = "python 3"

# Méteodo replace cria uma nova string
texto5 = texto5.replace("3", "2")

print(texto5)

#-----------------------------------------------
# (7) Méteodos Importantes
#-----------------------------------------------
# Strings possuem vários méteodos úteis.

cidade = "maracana"
# Coloca a primeira letra em maiúscula.
print(cidade.capitalize())

# Conta quantas vezes "a" aparece
print(cidade.count("a"))

# Verificar se começa "m"
print(cidade.startswith("m"))

# Verifica se termina com "z"
print(cidade.endswith("z"))

frase = "copa de 2002"

print(frase.split(" "))

#-----------------------------------------------
# (8) Formatação de Strings
#-----------------------------------------------
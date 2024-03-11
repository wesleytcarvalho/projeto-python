"""
ATENÇÃO: Você pode estudar List Comprehenshion, quando você entender Listas

List Comprehenshion

A compreensão de lista oferece uma sintaxe mais curta quando você deseja criar uma nova lista com base nos valores de
uma lista existente.

# Sintaxe da List Comprehenshion
[ dado for dado in interável ]

# Exemplos
lista = [1, 2, 3, 4, 5]
res = [numero * 10 for numero in lista]
print(res)

Para entender melhor o que esta acontecendo devemos dividir a expressão em duas partes:
- A primeira parte: for numero in lista
- A segunda parte: numero * 10

def funcao(valor):
    return valor * valor
res = [funcao(numero) for numero in lista ]
print(res)

# Loop com FOR normal
numero_dobrado = []
for numero in range(1, 5):
    numero_dobrado.append(numero * 2)
print(numero_dobrado)

# Loop com FOR e List comprehension
print([numero * 2 for numero in range(1, 5)])

# NOTA: Quando você aprende List comprehension e alguém olha seu código isso
# que dizer que você aprendeu python avançado.

# Outros exemplos
# (1)
# nome = 'UdayTC'
# print([letras.upper() for letras in nome])

# (2)
def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome
amigos = ['maria', 'larissa', 'fernanda']
print([caixa_alta(amigo) for amigo in amigos])

# (3)
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])
# Obs:
# - 0 no python é considerado como False
# - [] colchetes vazio é considerado como False
# - "", '' aspas simples/duplas fazias sao consideradas como false
# - True e True mesmo
# - 1 e 3.14 é True porque é um valores
"""


"""
Listas aninhadas
- Em algumas aninhadas de programação (C/Java) possuem uma estrutura de dados chamadas de arreys:
    - Unidimensionais (Arrays/Vetores);
    - Multidimensionais (Matrizes);

- Em Python nós temos as Listas
numero = [1, 'b', 3.23, True, 5]

# Exemplo
01_lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz de 3 x 3

print(type(01_lista))
print(01_lista)
print(01_lista[0][2])  # pegando o 3
print(01_lista[-1][-2]) # pegando o 8

# Iterando com loops em uma 01_lista aninhada
for 01_lista in Listas:
    for num in 01_lista:
        print(num)

# List comprehenshion
print([num for 01_lista in Listas for num in 01_lista])

# Outros exemplos

# Gerando um tabuleiro/matrix 3x3
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogo para o jogo da velha
velha = [["X" if numero % 2 == 0 else "O" for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valor inicial
print([['*' for i in range(1, 4)] for j in range(1, 4)])
"""



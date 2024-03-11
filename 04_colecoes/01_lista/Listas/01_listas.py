"""
Python

—————————————
exercicios
—————————————

Uma 01_lista aceita qualquer tipo de dado, ele inicia com colchetes [ ]
Exemplo 01_lista: comida=['Arroz', 'Feijao', 'Ovo', 'Cebola']
                  numero=[1, 45, 3, 56, 4, 3]

Comandos que pode ser utilizado em 01_lista

Exemplo: o primeiro comando pode ser dir(comida), este comando estou verificando qual o método que posso usar com o
tipo de dados 01_lista:

- comida.append('Tomate') = ira adiciona na final da 01_lista Tomate
- comida.count('Arroz') = ele vai encontrar 1 ocorrência com o nome Arroz
- comida.extend([12,45,34]) = adicionando elementos no final da 01_lista,
- comida.insert(2, 'Novo valor') = Inserir um novo elemento na 01_lista informando a posição do indice, lembre-se que ele vai adicionar a direita não vai subistitui nada.
- numero.sort() = ordenar a 01_lista seja strings ou numero
- numero.reverse() = ordenação reversa
- lista6 = numero.copy() = Copiando 01_lista

comida = ['Arroz', 'Feijao', 'Ovo', 'Cebola']
numero = [1,45,3,56,4,3]

print(comida)

# Como ler este comando (if 8 in lista4:)
if 8 in lista4: # Se 8 estiver na lista4

# Podemos facilmente checar se determinado valor esta contido na 01_lista
num = 8
if num in lista4:
    print(f'Encontrei o nuemro {num}')
else:
    print(f'Nao encontrei o numero {num}')


# Podemos Ordenar uma 01_lista
lista1.sort()
print(lista1)

# Podemos facilmente contar uma ocorrencia na 01_lista seja numero ou letras
print(lista5.count('e'))

# Adicionando elementos na 01_lista
# Obs:. Com o append só conseguimos adicionar um elemento por vez, mas podemos colocar 01_lista dentro de 01_lista
print(lista1)
lista1.append(42)
print(lista1)

lista1.append([1, 3, 4])  # Coloca um elemento unico dentro de outra 01_lista
print(lista1)

if [1, 3, 5] in lista1:
    print('Em contrei a 01_lista')
else:
    print('Nao encontrei a 01_lista')

lista1.extend([11, 11, 11])  # Adiciona elementos na lsita
print(lista1)

# Quando usamos o extend ou append ele adiciona sempre no final da LISTA
# Mas podemos escolher a posição onde queremos adicionar!
lista2.insert(4, 10)
print(lista2)

# Podemos facilmente juntar duas Listas
Listas = lista1 + lista2
print(Listas)

lista1.extend(lista2)
print(lista1)

# Podemos reverter as Listas
# Forma1
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

# Forma 2
# slawse
print(lista1[::-1])
print(lista2[::-1])

# Copiar uma 01_lista
Listas = lista1.copy()
print(Listas)

# Podemos contar quantos elementos tem na 01_lista
print(len(lista5))

# Podemos remover o ultimo elemento de uma 01_lista
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um alemento apenas pelo o indice
# Os elementos a direita deste indice sao deslocados para a esquerda quando estamos usando o pop para deletar por indice
# Se n
lista5.pop()
print(lista5)

# Podemos remover todos os elementos da 01_lista (zera a 01_lista)
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elemento em uma 01_lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Podemos facilmente converter uma string para uma lista
# Exemplo 1
curso = 'Programacao em python: essencial'
print(curso)
curso = curso.split()
print(curso)
# OBS: Por padrao, o split separa os elementos da 01_lista pelo espaco entre elas.

# Exemplo 1
curso = 'Programacao,em,python:,essencial'
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo uma 01_lista em uma string
# Exemplo 1
lista6 = ['Programacao', 'em', 'python:', 'essencial']
print(lista6)

# Abaixo estamos falando pega a lista6, coloca espaco em cada elemento, e transforma em uma string
curso = ' '.join(lista6)
print(curso)

# Exemplo 2
# Abaixo estamos falando pega a lista6, coloca cifrao em cada elemento, e transforma em uma string
curso = '$'.join(lista6)
print(curso)

# Reforcando; podemos colocar qualquer tipo de dado em uma 01_lista
exemplo = [1, 2.04, True, 'Uday', 'd', [1, 2, 3], ('w', 'e', 'e'), '23456789sdfghj']
# Ou seja, podemos colocar numeros float, normal bolean, Listas dentro de Listas, tupula dentro de 01_lista, numeros grandes etc.
print(type(exemplo))
print(exemplo)

# iterando sobre Listas;
# Exemplo 1 - utilizando for
soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 - utlizando while
carrinho = []
produto = ''
# A condicao deste while e: quanto o produto for diferente de sair ele continua
while produto != 'sair':
    print('Adicione  um produto na 01_lista ou digite "sair" para sair: ')
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Fazemos acesso a elemnto de forma indexada
cores = ['verde', 'amarelo', 'vermelhor', 'Laranja']

print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])

# Podemos ver o inveso ao inves de ser verde quero ver o vermelho primeiro
print(cores[-1])
print(cores[-2])
print(cores[-3])


cores = ['verde', 'amarelo', 'vermelhor', 'Laranja']
for cor in cores:
    print(cor)


indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

# Copiando uma 01_lista para outra (Shallow Copy e Deep Copy)
# Forma 1 - (Deep Copy)
01_lista = [1, 2, 3]
print(01_lista)

nova = 01_lista.copy()
print(nova)

nova.append(4)
print(nova)
# Obs: quando usamos o metodo copu() ele copiar uma 01_lista para outra 01_lista ficando totalmente idependente
# Se eu alterar uma nao altera a outra isso se chama (Deep copy) copia profunda


"""
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', '', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('Uday Academy')

# Forma 2 - Shellow copy
lista = [1, 2, 3]
print(lista)

nova = lista  # Veja que isso tambem e uma copia, porem, tem diferencas
nova.append(4)

print(lista)
print(nova)

# Veja que utlizamos a copia via atribuição, mas veja que apos atribuir um valor a 01_lista nova ele
# automáticamente fez nas duas Listas


















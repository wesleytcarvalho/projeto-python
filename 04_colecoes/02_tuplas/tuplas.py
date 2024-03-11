"""
Tuplas (tuple)
Tuplas são bastante parecidas com Listas:
Existem basicamente duas diferenças básicas:

1 - As 02_tuplas são representadas por parênteses ()
2 - As 02_tuplas são imutáveis, Isso siguinifica que ao ser criar uma tupla ela não muda.
Toda operação em uma tupla gera uma nova tupla.

#CUIDADO 1 - As 02_tuplas são representadas por parenteses (), mas veja:
#isso e uma tupla
tupla = (1, 2, 4, 5, 6)
print(tupla)
print(type(tupla))
print('-----------------')

isso tambem e uma tupla
tupla2 = 1, 2, 4, 5, 6
print(tupla2)
print(type(tupla2))
print('------------------------')

# CUIDADO 2 - Tupla com 1 elemento
print('Isso NAO e uma tupla')
tupla3 = (4)
print(tupla3)
print(type(tupla3))
print('-------------------')

print('Isso e uma tupla')
tupla4 = (4,)
print(tupla4)
print(type(tupla4))

Isso e uma tupla
tupla5 = 4,
print(tupla5)
print(type(tupla5))
# CONCLUSAO: Podemos concluir que 02_tuplas sao definidas pela virgula e nao pelo uso do parenteses

# Legenda:
(4) -> Não é tupla
(4,) -> É tupla
4, -> É tupla

# Podemos gerar uma tupla dinamicamente com range(inicio,fim,passo)
tupla = tuple(range(11))
print(tupla)

# Desenpacotamento de tupla
tupla = ('Uday Academy', 'Programação em python: Essencial')
escola, curso = tupla
print(escola)
print(curso)
# Obs: Gera erro (ValueError) se colocarmos um número diferente de elementos para desenpacotar.

# Metodos para adição e remoção nas 02_tuplas não existem, dado o fato das 02_tuplas serem imutáveis.
# Com as funções sum(), Valor máximo, Valor minimo e Tamnho conseguimos fazer normal com as 02_tuplas
# Mas se os valores forem inteiros ou rais, string não funciona com sum, max, min
tupla = (1, 2, 3.4, 5, 6)
print(sum(tupla))
print(min(tupla))
print(max(tupla))
print(len(tupla))

# Concatenação de 02_tuplas
tupla1 = (1, 2, 3.4, 5, 6)
tupla2 = ('b', 'a', 'g')

print(tupla1 + tupla2)

# Podemos verificar se um valor está na tupla de forma facil
print(3.4 in tupla1)

# interando com uma 01_lista
tupla1 = (1, 2, 3.4, 5, 6)
for n in tupla1:
    print(n)
for indice, valor in enumerate(tupla1):
    print(indice, valor)

# Contando elemento dentro de uma uma tupla
tupla = ('a', 'b', 'b', 'c', 'd', 'e', 'f')
print(tupla.count('b'))
escola = tuple('Uday Academy')
print(escola)
print(escola.count('e'))

# O acesso a elementos de uma tupla também é semelhante a de uma 01_lista
print(meses[3])
# interar com o while
i = 0
while i < len(meses):
    print(i)
    i += 1

# Dicas na utilização de 02_tuplas
# Devemos ultilizar 02_tuplas SEMPRE que não precisamos modificar os dados contidos em uma coleção
# Exemplo 1
meses = ('Janeiro', 'Fevereiro', 'Março', 'Maio')

# Verificando em qual indice um elemento esta na tupla
print(meses.index('Fevereiro'))

# Slicing
# tupla[meses[5:]]
print(meses[:-1])
print(meses[-2:-1])
print(meses[3:])

# Porque utlizar 02_tuplas?
# - Tuplas e mais rapido
# - Tuplas deixa seu codigo mais seguro
# * Isso porque trabalhar com elementos imutaveis trazem mais seguranca para o codigo

# Copiar uma uma tupla para outra
tupla = (1, 2, 4, 5)
print(tupla)

nova = tupla # Na tupla nao temos o problema de shellow copy

print(nova)
print(tupla)

outra = (4, 5, 6)
nova = nova + outra

print(nova)
print(tupla)
"""





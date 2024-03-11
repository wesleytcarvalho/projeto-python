"""
Loop FOR
- Loop -> Estrutra de repetição
- For -> Uma dessas estruturas

Estrutura do FOR
for item in interavel:
    ;;execução do loop

Utilizamos o loops para iterar sobre sequênvias ou sobre valores iteráveis

Exemplo de iterável
- String
    nome = 'Uday Academy'
- exercicios
    01_lista = [1, 2, 3, 4, 5, 6]
- Range
    numeros = range(1, 10)

nome = 'Uday Academy'
lista = [1, 2, 3, 4, 5, 6]
numeros = range(1, 10)  # Temmos que transforma em 01_lista

# Exemplo de for 1 (Iterando sobre um string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando sobre um 01_lista)
for numero in 01_lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)
for numero in range(1, 10):
    print(numero)

OBs: O valor final não é inclusive, exemplo; se eu usei o range de 1 a 10 então 10 não é inclusivo, ele só vai
de 1 a 9.

Funcionamento do enumerate():
(0, seq[0]), (1, seq[1]), (2, seq[2]), ...

for i, v in enumerate(nome):
    print(nome[i])


# Voce pode trabalhar com o indice, mas voce tambem pode trabalhar com a letra somente
for indice, letra in enumerate(nome):
    print(letra)

# Quando temos dois valores sendo atribuido em duas variaveis, mas não vamos usar o outro podemos usar o anderlaine para
# descartar
for i, _ in enumerate(nome):
    print(nome[i])

qtd = int(input('Quantas vezes este loop deve rodar? '))
soma = 0
for i in range(1,  qtd+1):
    num = int(input(f'Informe o {i}/{qtd} valor: '))
    soma += num
print(f'A soma é {soma}')

# Não quero pular linha, usar o end=''
site = 'curso.uday.com.br'
for i in site:
    print(i, end='')

Tabela de emogis: https://apps.timwhitlock.info/emoji/tables/unicode
# Original: U+1F60D
# Modificado: U0001F60D
for num in range(1, 11):
    print('\U0001F60D' * num)
"""

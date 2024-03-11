"""
Loop while

Como eu sei a hora certa de utilizar o while do for?
Resposta é muito simples se focão não sober quantos passos ele vai dar usa o while, se você sabe até onde ele
vai usa o for.

Forma geral
while expressão_booleana:
    //execução do loop

- O bloco while será repetido enquanto a expressão booleana for verdadeira
- Expressão Boleana é toda expressão onde o resultado é verdadeiro ou falso

Exemplo:
num = 5
num < 5

# Exemplo 1
numero = 1
while numero < 10:
    print(numero)
    numero += 1

# Obs: Em um loop while, é importante que cuidemos do critério de parada para não causar um loop infinito.

# Exemplo 2
resposta = ''
while resposta != 'sim':
    resposta = input('Já terminou? ')
"""

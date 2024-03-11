"""
Len, Abs, Sum, Round

# Len
# len() -> Retorna o tamanho (ou seja, o número de itens) de um iterável
# só pra revisar
print(len([1, 2, 3, 4, 5]))
print(len((1, 2, 3, 4, 5)))
print(len({1, 2, 3, 4, 5}))
print(len('Uday Tecnologia'))
print(len({'a': 1, 'b': 2}))

# Por debaixo dos panos, quando utlizamos a função len() o python faz o seguinte:
# Dunder len
print('Uday Academy'.__len__())

# Abs
# abs() -> Retorna o valor absoluto de um número inteiro ou real. De forma basica, seria o seu valo real sem o sinal.
#Exemplo ABS
print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))

# Sum
sum() -> Recebe como parametro um iteravel, podendo receber um valor inicial, e retorna a soma total dos elementos,
incluindo o valor inicial
# só pra revisar
print(sum([1, 2, 3, 4, 5]))
print(sum((1, 2, 3, 4, 5)))
print(sum({1, 2, 3, 4, 5}))
print(sum({'a': 1, 'b': 2}.values()))

# Round
round() -> Retorna um número arredondado para não digito de precisão após a casa decimal. Se a precisão for
informada retorna o inteiro mais próximo da entrada.
# Exemplo Round
print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(1.21212121, 2))
print(round(1.219999, 2))
"""

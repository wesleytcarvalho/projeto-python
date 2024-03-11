"""
Conjunto(Set) Comprehension

exercicios = [1, 2, 3, 5]
Set = [1, 2, 3, 5]

numeros = {num for num in range(1, 7)}
print(numeros)

# Outro exemplo
print({x ** 2 for x in range(10)})

# Desafio! faça uma alteração na estrutura acima para gerar um dicionario ao invés de set
print({x: x ** 2 for x in range(10)})

# Para finalizar
letras = {letra for letra in 'Uday TC'}
print(letras)
"""

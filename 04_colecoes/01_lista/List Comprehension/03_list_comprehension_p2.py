"""
List Comprehension
Nós podemos adicionar estruturas condicionais lógica as nossas "List Comprehension"

numeros = [1, 2, 3, 4, 5, 6, 7]

# Exemplo1 = Verificando se é par ou impar
# FOR COMUM ------------------
for numero in numeros:
    if numero % 2 == 0:
        print(f'Número par: {numero}')
    elif numero % 2 == 1:
        print(f'Número impar: {numero}')
    else:
        print('Não entendo que foi digitado')

# LIST COMPREHENSION
# Qualquer número par módulo de 2 é 0 em python é False. not False = True
pares = [numero for numero in numeros if not numero % 2]
# Qual quer número impar módulo de 2 é 1, e 1 em python é True
impares = [numero for numero in numeros if numero % 2]
print(f'Numeros pares: {pares}')
print(f'Numeros impares: {impares}')

# Refatorando o código
print(f'Número PAR: {[numero for numero in numeros if numero % 2 == 0]}')
print(f'Número IMPAR: {[numero for numero in numeros if numero % 2 != 0]}')

# Exemplo 2
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)
"""

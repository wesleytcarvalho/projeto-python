# Write a Python function to sum all the numbers in a list.

def soma_lista(lista):
    soma = 0
    for i in lista:
        soma = soma + i
    return soma


lista = [12, 35, 46, 46]


print(soma_lista(lista))



""" 
1. Escreva um programa Python para criar um decorador que registre os argumentos e o valor de
retorno de uma função.
""" 
import os
os.system('clear')



def decorator(funcao):
    def enrolar(*args, **kwargs):
        print(f'Chamado a função {funcao.__name__} com args: {args} e kwargs: {kwargs}')

        result = funcao(*args, **kwargs)

        print(f"Chamado a função {funcao.__name__} com retorno: {result}")

        return result
    return 



@decorator
def mult_numero(x, y):
    return x * y



result = mult_numero(10, 34)
print("Result", result)
"""
Try / Except / Else / Finally

Dica de quando e onde tratar codigo:

TODA ENTRADA DO USUARIO DEVE SER TRATADA

OBS: A funcao do seu usuario é DESTRUIR seu sistema

# Este codigo abaixo o usuario vai ter uma entrada para digitar,
# - Veja que eu coloquei um tipo na variavel de int, se o usuario digitar letras vai da erro
# - Entao, podemos tratar este erro!

num = int(input('Informe um número: '))
print(f'Valor digitado é: {num}')

# Else -> é execultado somente se não ocorrer o erro
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor errado')
else:
    print(f'Valor digitado é: {num}')

# Finally

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor com errado')
else:
    print(f'Valor digitado é: {num}')
finally:
    print('---- Final da execução ---- ')


# outro Exemplo
try:
    num = int(input('Digite um numero: '))
    print(f'O numero digitado foi: {num}')
except SyntaxError as erro:
    print(f'Você digitou algo errado: {erro}')
except ValueError as erro:
    print(f'Você digitou algo errado: {erro}')
else:
    print('Programa executado com sucesso, sem erros!')
finally:
    print('Este programa foi finalizado')


# Obs: O bloco finally é SEMPRE executado, independente se houve exceção ou não
# o Finally, geralmente é utlizado para fechar ou desalocar recursos

# Exemplo mais complexos ERRADO
def dividir(a, b):
    return a + b

num1 = int(input('Informe o primeiro número: '))

try:
    num2 = int(input('Informe o segundo número: '))
except ValueError:
    print('O valor precisa ser número: ')

try:
    print(dividir(num1, num2))
except NameError:
    print('Valor incorreto')

# Exemplo mais complexos CERTO
# Obs: Você é responsável pelas entradas das suas funções. Então, trate-as!
def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num2, num1))

# Exemplo mais complexos CERTO Generico
# Obs: Você é responsável pelas entradas das suas funções. Então, trate-as!
def dividir(a, b):
    try:
        return int(a) / int(b)
    except:
        return 'Ocorreu um problema'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num2, num1))

# Exemplo mais complexos CERTO Semi-Generico
# Obs: Você é responsável pelas entradas das suas funções. Então, trate-as!
def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError):
        return 'Ocorreu um problema'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num2, num1))
"""


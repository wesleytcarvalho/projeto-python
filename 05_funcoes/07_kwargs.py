"""
**kwargs
poderíamos chamar este parâmetro de **xis, mas por convenção de é chamado pela comunidade de **kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras em uma tupla,
o **kwargs exige que utilizemos parâmetros nomeados, e transforma esses parâmetros extras em dicionário.

# Exemplo simples
def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')

cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul')

# OBS: Os parâmetros *args e **kwargs não são obrigatório.
cores_favoritas()
cores_favoritas(uday='tc')

# Exemplo mais complexo

def cuprimento_especial(**kwargs):
    if 'Uday' in kwargs and kwargs['Uday'] == 'Python':
        return 'Você recebeu um cuprimento Pythonico Uday!'
    elif 'Uday' in kwargs:
        return f"{kwargs['Uday']} Uday!"
    return 'Não tenho certeza quem é você...'

print(cuprimento_especial())
print(cuprimento_especial(Uday='Python'))
print(cuprimento_especial(Uday='Oi'))
print(cuprimento_especial(Uday='Especial'))

# Se você precisar declarar todos este parâmetros nas funções, a ordem é igual está abaixo

- Parâmetro obrigatórios =  parâmetros obrigatório são aqueles que não tem valor, ou seja, na hora da execução eles
ser declarados exemplo "def calculadora(num1, operador, num2)"
- *args =  pode ser qualquer coisa que você quer passar para a função, ele será criado em uma tupla
exemplo: "def calculadora(*args)"
- Parâmetros default (não obrigatório) = A função já é criada com argumentos definidos nos parâmetros
exemplo: def soma(num1=1, operador=+, num2=2)
- **kwargs = no caso do  **kwargs será definido uma função como um dicionario exemplo: "def soma(**kwargs)"
ai no caso ficaria tipo assim resultado = {fernando='masculindo', rquel=feminio} ai eu passo como argumento
"soma(resultado)

# Exemplo 1

def minha_funcao(nome, *args, solteiro=False, **kwargs):
    print(f'{nome} seja bem-vindo')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)

minha_funcao('Julia')
minha_funcao('Felicia', 4, 5, 7, solteiro=True)
minha_funcao('Felipe', eu='Não', voce='vai')

# Desempacotar com kwargs
Exemplo1
def mostrar_nome(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nome = {'nome': 'Andre', 'sobrenome': 'tibucio'}

print(mostrar_nome(**nome))




# Exemplo 2
def soma(a, b, c):
    print(a + b + c)

01_lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}
dicionario = dict(a=1, b=2, c=3)

soma(*01_lista)
soma(*tupla)
soma(*conjunto)
soma(**dicionario)

# Veja que conseguimos desempacotar com todos os tipos de dados
# ATENÇÃO: no caso do 03_dicionarios os valores tem que ser os mesmos da função
"""

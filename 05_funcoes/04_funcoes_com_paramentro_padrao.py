"""
Funções com parâmetro padrão (Default paramters)
- Funções onde a passagem de parâmetro é opcional;

# Exemplo de função onde a passagem do parâmetro seja opicional e não tem erro na execução
print('uday.com.br')
print()

# Exemplo de função onde a passagem de parâmetro é obrigatório
def quadrado(numero):
    return numero ** 2

print(quadrado(3))
print(quadrado()) # TypeError

def exponecial(numero, potencia=2):
    return numero ** potencia

print(exponecial(2, 3))  # 2*2*2 = 8
print(exponecial(3, 2))  # 3*3 = 9

# Vamos imagina que queremos passar somente um número ou qualquer número, vai funciona sem problema, porque 
definimos que o parametro é já tem um valor default
print(exponecial(3))
print(exponecial(3, 5))

# Obs:
- Se o usuário passar somente 1 argumento, este será atribuído ao parâmetro numero, e será calculado o quadrado deste número.
- Se o usuário passar 2 argumentos, o primeiro sera atribuído ao parâmetro número e o segundo ao parâmetro potencia.
Então será calculado esta potência.

# Obs: em funções python, os parâmetros com valores default (padrão) DEVEM sempre estar ao final da declaração.
# ERRO!
def teste(num=2, potencia):
    return num ** potencia

# CERTO!
def teste(potencia, num=2):
    return num ** potencia

# Outros exemplos
def soma(num1=0, num2=0):
    return num1 + num2

print(soma(4, 3))
print(soma(4)) 
print(soma())

Obs: Você pode inicializar os parâmetros da função como zero ai você não precisa não precisa ser obrigatório os números
da erro de syntax.

# Exemplo mais complexo
def mostra_informacao(nome='Uday', instrutor=False):
    if nome == 'Uday' and instrutor:
        return 'Bem-vindo instrutor Uday!'
    elif nome == 'Uday':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print('Ozzy')
print(mostra_informacao(nome='Jose'))

# Por quê utilizar parâmetros com valor default?
- Nos permite ser mais flexíveis nas funções;
- Evita erros com parâmetros incorretos;
- Nos permite trabalhar com exemplos mais legíveis

# Quais tipos de dados podemos utilizar como valor default para parâmetros?
- Qualquer tipo de dado:
   - Numeros, strings, floats, booleanos, Listas, tuplas, dicionario, funcoes e etc.

# Exemplo de funcao dentro de funcao
def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num1)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 2, subtracao))

# Escopo - Evitar problemas e confusoes
# Variaveis globais
# variaveis locais

instrutor = 'Uday' # variavel global
def diz_oi():
    return f'Oi {instrutor}'

print(diz_oi())


# Obs: Se tivermos uma variavel local com o mesmo nome da variavel global, o local tera preferencia
# Outra observacao e, se voce usar uma variável de uma funcao que e local, voce nao consegue usar fora da funcao

instrutor = 'Uday' # variavel global
def diz_oi():
    instrutor = 'Python'  # variavel locais
    return f'Oi {instrutor}'

print(diz_oi())

#ATENÇÃO: Com variaveis globabais (Se poder evitar, evite!)
# Para que uma variável dentro de uma funcão seja global você precisa inserir na função o GLOBAL, veja p exemplo a baixo

total = 0
def incremento():
    global total # Avisando que queremos utilizar a variavel global

    total = total + 1
    return total

print(incremento())

# Podemos ter fuções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável

def fora():
    contator = 0

    def dentro():
        nonlocal contator

        contator = contator + 1
        return contator
    return dentro()

print(fora())
print(fora())
print(fora())
"""

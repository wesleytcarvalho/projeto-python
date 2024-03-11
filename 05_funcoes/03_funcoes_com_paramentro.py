"""
Funções com parametro (de entrada)
- Funções que recebem dados para serem processador dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:
# Entrada -> Processamento -> Saida

Se a gente pensar em uma função, já sabemos que temos funções que
- Não possuem entrada;
- Não possuem saida;
- Possuem entrada, mas não possuem saida;
- Não possuem entrada, mas possuem saida;
- Possuem entrada e saida;

Exemplo(1) de função
def quadrado(numero):
    return numero * numero
print(quadrado(2))

# Funções podem ter quantos parâmetros você quiser de entrada, Ou seja, podemos receber como entrada
# em uma função quantos parâmetros forem necessário. Eles são separados por (,) virgula.

# Exemplos
def soma(a, b):
    return a + b

def mult(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 + b) * msg

# Usando os parâmetros acima
print(soma(20, 45))
print(mult(20, 35))
print(outra(2, 3, 'Ola mundo!'))


# Obs: Se agente informa um número errado de parâmetro ou argumentos, teremos TypeError

# Nomeando parâmetro
def nome_completo(nome, sobrenome):  # isso é um Parâmetro
    return f'Seu nome completo é {nome} {sobrenome}'

print(nome_completo('Andre', 'Carvalho'))  # Isso é agurmentos

# Diferença entre Parâmetro e Argumento
## Parâmntro são variáveis declaradas na definição de uma função;
## Argumento são dados passados durante a execução de uma função;

## A ordem dos parâmtros importa
nome = 'Felicity'
sobrenome = 'Jones'

print(nome_completo(sobrenome, nome))

# Argumentos nomeados conhecidos na programação como (Keyword Arguments)
print(nome_completo(nome='Angelina', sobrenome='Jolie'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(nome='Marques', sobrenome='Marcias'))

# Erro comum na utilização de return
def soma_impar(numero):
    total = 0
    for num in numero:
        if num % 2 != 0:
            total = total + num
    return total

# Obs: o "return" finaliza a função, então tome muito cuidado neste caso acima não podemos
# colocar a função no IF porque o resultado vai sair errado ele tem que ser junto com
# as operações iniciais como por exemplo o FOR

lista = [1, 2, 3, 4, 5]
print(soma_impar(lista))

tupla = (1, 2, 3, 4, 5)
print(soma_impar(01_lista))
"""
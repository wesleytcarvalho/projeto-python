"""
https://docs.python.org/3/library/exceptions.html
Erros mais comuns em Python
ATENÇÃO: É importante prestar atenção e apreder a ler as saídas de erros gerados pela execução do código.

Erros mais comuns
1) SyntaxError -> Ocorre quando o Python encontra um erro de sintexe, Ou seja, você escreve algo que o Python não reconhece
 como parte da linguagem.

a)
def funcao:
    print('Uday')

b)
def = 1

c)
return

2) NameError -> Ocorre quando uma variável ou funçõo não foi definida.

Exemplos NameError
a)
print(Uday)

b)
Uday()

c)
a = 18
if a < 10:
    msg = 'E maior que 10'
print(msg)

3) TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado.

Exemplos TypeError
a)
print(len(3))

b)
print('Uday' + [])

c)
print('Uday' + [])

4) IndexErro -> Ocorre quando tentamos acessar um elemento em uma 01_lista ou outro tipo de dado indexado utlizado
um índice inválido.

Exemplos IndexError
a)
01_lista = ['Uday']
print(01_lista[3])

b)
tupla = ('Uday')
print(tupla[3][4])

5) ValueError -> ocorre quando uma função/operação built-in (integrada) recebe um argumento com tipo correto, mas
valor errado inapropriado.

Exemplo ValueError
a)
print(float('Uday'))

6) KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe.

Exemplo KeyError
a)
dic = {'Python': 'University'}
print(dic['Uday'])

7 AttributeError -> Ocorre quando uma variavel não tem um atributo/funcao.

Exemplo AttributeError
a)
tupla = (11, 33, 66)
print(tupla.sort())

8 IndentationError -> Ocorre quando nao respeitamos a identacao do python que e de 4 espacos

Exemplo IndentationError
a)
def nova():
print('Uday')

b)
for i in range(10)
i + 1

OBs: Exceptions e Error sao sinonimos na programacao
OBS: Importante ler e prestar atencao na saida de erro
"""






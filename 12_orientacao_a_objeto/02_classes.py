"""
POO - Classes

Em POO, Classes nada mais são do que modelos dos objetos do mundo real sendo representados
computacionalmente.

Imagine que você queira fazer um sistema para automatizar o controle das lâmpadas da sua casa.

Classes podem conter:
    - Atributos -> Representam as caraterísticas do objeto, Ou seja, pelos atributos conseguimos
    representar computacionalmente o estado de um objeto. no caso da lâmpada, possivelmente iriamos
    querer saber se a lâmpada é 110 ou 220 volts, se ela é branca, amarela, vermelha ou outra cor, qual é
    a luminosidade dela etc.

    - Métodos (funções) -> Representa os comportamentos do objeto, Ou seja, as ações que este objeto pode
    realizar no seu sistema. No caso da lâmpada, por exemplo, um comportamento comum que muito provavelmente
    iríamos querer representar no nosso sistema é o de ligar e desligar a mesma.

Em python, para definir uma classe utilizamos a palavra reservada class.

OBS:
- Utilizamos a palavra 'pass' em Python quando temos um bloco de código que ainda não está
implementado.
- Quando nomeamos nosso classes em Python, utilizamos por convenção o nome com inicial em maiúsculo.
Se o nome for composto, utiliza-se as iniciais de ambas as palavras em maiúsculas, todas juntas!
- Em computação não utilizamos: acentuação, caratres especiais, espaçõs ou similares para nomes
de classes, atributos, métodos, arquivos, diretorios etc.
- Quando estamos planejando um software e definimos quais classes teremos que ter no sistema, chamamos estes objetos
que serão mpaeados para classes de entidade.

"""

class Lampada:
    pass

class ContaCorrente:
    pass

class Produto:
    pass

class Usuario:
    pass

lamp = Lampada()
print(type(lamp))


# Nos já tinhamos utilizado algumas classes sem perceber
# Exemplo:
valor = int('24')  # Isso é um cast, ou sejam estamos convertendo uma string para um inteiro
print(help(int))  # Veja que o método INT é uma classe

# Veja que acima eu falei que toda classe tem que ter as primeiras letras em maiúscula, mas aqui no int
# é minusculo, você deve está se perguntando porque?
# Respondendo: é porque as classes interna do python e minúscula para diferença das classes dos programadores,
# que estão utilizando o python.



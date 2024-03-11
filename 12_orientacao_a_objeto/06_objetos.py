"""
POO - Objeto

Objetos -> são instâncias da classe. Ou seja, após o mapeamento do objeto do mundo real para sua representação computacional, devemos poder criar quantos forem necessários, Podemos pensar nos objetos/instância de uma classe como variáveis do tipo definido na classe.

# Aqui é a definição da classe
class Lampada:

    # Aqui é o construtor do objeto
    def __init__(self, cor, voltagem, luminosidade):
        # Aqui é os atributos do objetos
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligado = True

    # Isso é um método (métodos são a funções usando objetos)
    def checa_lampada(self):
        if self.__ligado == True:
            return '+ Lampada ligada +'
        elif self.__ligado == False:
            return '+ Lampada desligada + '
        else:
            return 'Acho que a lampada esta queimada'

# Aqui é a definição da classe
class ContaCorrente:

    # Atributo de classe
    contador = 4999

    # Aqui é o construtor do objeto
    def __init__(self, limite, saldo):
        # Aqui é os objetos
        self.__id = ContaCorrente.contador + 1
        self.__limete = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__id

# Aqui é a definição da classe
class Usuario:

    # Aqui é o construtor do objeto
    def __init__(self, nome, sobrenome, email, senha):
        # Aqui é os objetos
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha

# Instância / Objetos
lamp1 = Lampada('Amarelo', 220, 60)
print(f'A lampada está ligada? {lamp1.checa_lampada()}')

cc1 = ContaCorrente(5000, 2000)

user1 = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '124456')
"""
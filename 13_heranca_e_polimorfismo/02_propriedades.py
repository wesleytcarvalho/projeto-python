"""
POO - Propriedades - Properties

Vamos criar nossos modelo

# Aqui e nosso construtor
Conta
 - contador
 - numero
 - titular
 - saldo
 - limite

    Atributos
        - extrato
        - depositar
        - sacar
        - transferir


class Conta:

    contador = 1

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador = self.__numero

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def deposito(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferencia(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite


conta1 = Conta('Felicity', 3000, 5000)
conta2 = Conta('Angelina', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

# Se eu quisesse fazer o calculo das duas conta (Não pode ser criado assim)
# Se você precisa que isso seja possivel, criar metodos dentro da classe com estas condições
# Até porque os parametros são privado,
soma = conta1._Conta__saldo + conta2._Conta__saldo
print(f'O calculo das conta foi {soma}')

#  O certo de se trabalhar e expondo os metodos de uma classe, agora aqui é o certo
soma = conta1.get_saldo() + conta2.get_saldo()
print(soma)

NOTA +=+=++=+=++=+=++=+=++=+=++=+=+
Pessoal existe um termo chamado getter e setter, que seria igual abaixo

# Getter

def get_saldo(self):
    return self.__saldo

OBS: veja que podemos acessar este metodo de fora da classe, esse é um meio bom de se usar
ou seja, eu estou disponibilizando meu atributo que é privado para ser consultado.

#Setter

def set_saldo(self, saldo)
    return self.__saldo = saldo

OBS: TOME MUITO CUIDADO AO USER O SETTER, veja que ele altera o valor.
+=+=++=+=++=+=++=+=++=+=++=+=++=+=+

Agora uma maneira melhor ainda de se utilizar o getter e o setter é usando um generator que seria uma
propriedade.

# Esse é nosso getter
@property
    def numero(self):
        return self.__numero

# Esse é nosso setter
 @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

Veja nosso codigo refatoracao, abaixo


"""
# Rafatorando o codigo para trabalhar com propriedades

class Conta:

    contador = 1

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador = self.__numero

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def deposito(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferencia(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor


conta1 = Conta('Felicity', 3000, 5000)
conta2 = Conta('Angelina', 2000, 4000)

soma = conta1.saldo + conta2.saldo
print(soma)



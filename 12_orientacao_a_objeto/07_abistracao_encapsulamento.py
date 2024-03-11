"""
POO Abstração e Encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e hierarquico utlizando classe.

Encapsular -> cápsula

        classe
---------------------------
|   astributos e métodos  |
---------------------------

# Relembrando Atributos/Métodos privados em Python

Imagine que temos uma classe chamada Pessoa, contendo um atributo privado chamado __nome e um método privado chamado __falar().

Esses elementos privados só deve/deveriam ser acessados dentro da classe. Mas Python não bloqueia este acesso fora da classe. Com Python acontece um fenômeno chamado Name Mangling, que faz alteração na forma de se acessar os elementos privados, conforme:

_Classe)__elemento

Exemplo - Acessando elementos privados fora da classe (forma ruim de acesssar)

instancia._Pessoa__nome

instancia._Pessoa_falar()

Abstração, em POO, é o tato de expor apenas dados relevantes de uma classe, escodendo atributos e métodos privados de usuário


class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.numero = Conta.contador
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.saldo} do titular {self.titular} com limite de {self.limite}')

    def deposito(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor
    


# Testando
conta1 = Conta('Uday', 150.00, 1500)

print(conta1.numero)
print(conta1.titular)
print(conta1.saldo)
print(conta1.limite)


conta1.numero = 42
conta1.titular = 'XUXU'
conta1.numero = 9999999999
conta1.numero = 11111111111111111111111

print(conta1.__dict__)

# Você pode notar o que está errado quando deixamos atributos sem ser privados?
# Qualquer um pode alterar os dados, claro, que isso pode ser alterados mesmo
# estando fora do fora da classe, entao, nao é uma boa praticar deixar atributos sem ser privados.

# Refatorando o código
class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def deposito(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor
    


# Testando
conta1 = Conta('Uday', 150.00, 1500)

print(conta1.__dict__)

conta1.extrato()

print(conta1._Conta__titular)  # Name mangling (Acesso errado)

conta1._Conta_titular = 'Andre'

print(conta1.__dict__)

"""


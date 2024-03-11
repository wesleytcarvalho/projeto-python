"""
POO - Métodos

- Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode realizar no seu sistema.
- Em Python, dividimos os métodos, em 2 grupos: Métodos de instância e Métodos de classe.

# Métodos de Instância

# O método dunder init __init__ é um método especial chamado de construtor, e sua função é construir o objeto a partirir da classe. 

OBS:
- Todo elemento em Python que inicia e finaliza com duplo underline é chamado de dunder (Double Underline), também conhecidos como métodos mágicos
- ATENÇÃO: Por mais que possamos criar nossas próprias funções utilizado dunder (underline no inicio e no final) não é aconselhado. Python possui vários métodos com esta forma de normeclatura e pode ser que mudemos o comportamento dessas funções mágicas internas da linguagem, Então, evite ao máximo. De preferência nunca o faça!!!!!

# Métodos são escritos em letras minúsculas. se o nome for composto, o nome terá as palavras seperadas por underline

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 4999

    def __init__(self, numero, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        # Retorna o valor do produto com desconto
        return (self.__valor * (100 - porcentagem)) / 100


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__sobrenome = sobrenome

    def nome_completo(self):
        return f'{self.__nome}, {self.__sobrenome}'


# Vamos verificar como ficaria os dados
produto1 = Produto('Nitendo oled', 'Video gamer', 2100)

# Valor real (Veja que nao consigo acessar este dado porque ele e privado e so funciona dentro da classe)
print(f'Produto: {produto1.__valor}')

# Valor com desconto
print(f'Produto: {produto1.desconto(20)}')

# Tipo de dado
print(f'Tipo de dado: {type(produto1.desconto(20))}')



usuario1  = Usuario('Leandro', 'Carvalho', 'usuario1@gmail.com', '32,3RQ3')
usuario2  = Usuario('Fernando', 'Costa', 'usuario2@gmail.com', 'adfvad')

print(usuario1.nome_completo())
print(usuario2.nome_completo())

# Algum espertinho pode acessar algum atributo de forma errada e conseguir nossa senha
print(usuario1._Usuario__senha)
print(usuario2._Usuario__senha)

# NOTA: que a senha esta aberta, vamos criptografar isso
# instalar a lib: pip3 install passlib





# Refatorando a classe usuários (Para estudos Metodos de Instância)
from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        self.__sobrenome = sobrenome

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checar_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        else:
            return False


nome = input('Informe seu nome: ')
sobrenome = input('Informe seu sobrenome: ')
email = input('Digite seu e-mail: ')
senha = input('Digitar senha: ')
confirmar_senha = input('Confirmar senha: ')

if senha == confirmar_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não conferi...')
    exit(32)
print('Usuario criado com sucesso! ')

senha = input('Informe a senha para acessa: ')

if user.checar_senha(senha):
    print('Acesso permitido!')
else:
    print('Acesso negado!')

print(f'Senha usuario {user._Usuario__senha}')  # Acesso errado


# Refatorando a classe usuários (Para estudos de Metodos de Classe)
from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:

    contador = 0

    # Metodo de classe
    @classmethod
    def conta_usuario(cls):
        print(f'Temos {cls.contador} usuário(s) no sistema')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        self.__sobrenome = sobrenome
        Usuario.contador = self.__id

    # metodo de instancia
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checar_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        else:
            return False


# Metodos de Classe

user = Usuario('Fernando', 'Nogueira', 'fernando.nogueira@gmail.com', '12343545')

Usuario.conta_usuario() # Forma correta
user.conta_usuario() # Possivel, mas incorreta

# Como saber quando usar metodo de instancia ou Metodos de classe?
# metodo de instancia = Quando precisamos trabalhar com os atributos de instancia exemplo: a linha 199 e 200 

# Metodos de classe e quando precisamos fazer igual a 187
# Metodos de classe em Python são conhecidos como metodos estaticos em outras linguagem:

# OBS:
- Os Métodos que fizemos até agora são métodos publicos, ou seja, que pode ser utilizados fora da classe, assim como temos os atributos privados iniciando com __alguma_coisa, podemos criar classes privadas também.
- Podemos criar classes privados usando duplo anderline também.


# Refatorando a classe usuários (Para estudos Metodos Privados)
from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:

    contador = 0

    # Metodo de classe
    @classmethod
    def conta_usuario(cls):
        print(f'Temos {cls.contador} usuário(s) no sistema')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        self.__sobrenome = sobrenome
        Usuario.contador = self.__id
        print(f'Usuario criado {self.__gera_usuario()}')

    # metodo de instância
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checar_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        else:
            return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]


user = Usuario('Fabiana', 'Ferreira', 'fabiana@com.br', '343d45rd')
print(user._Usuario__gera_usuario())  # Acesso ruim. NAO USE ASSIM!
"""
import os
os.system('clear')

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 4999

    def __init__(self, numero, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """ Retorna o valor do produto com desconto"""
        return (self.__valor * (100 - porcentagem)) / 100


# Refatorando a classe usuários (Metodo estatico)
from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:

    contador = 0

    # Metodo de classe
    @classmethod
    def conta_usuario(cls):
        print(f'Temos {cls.contador} usuário(s) no sistema')

    @staticmethod
    def definicao():
        return 'UXR344'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        self.__sobrenome = sobrenome
        Usuario.contador = self.__id
        print(f'Usuario criado {self.__gera_usuario()}')

    # metodo de instância
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checar_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        else:
            return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]


# NO metodo statico nos nao temos acesso a classe e nem a instancia

print(Usuario.contador)

print(Usuario.definicao())

user = Usuario('Fabiana', 'Ferreira', 'fabiana@com.br', '343d45rd')

print(user.contador)

print(user.definicao())







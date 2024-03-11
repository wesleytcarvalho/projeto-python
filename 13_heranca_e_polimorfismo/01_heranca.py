"""
POO -> Henrança (Inheritance)

A ideia de herança é a de reaproveitar código. Também extender nossas classes.

Obs: Com a herança, a partir de uma classe existente, nós extendemos outras classe que passa a herdar atributos
e métodos da classe herdada.


######## Modelo das classes ######
Cliente
    - nome;
    - sobrenome;
    - cpf;
    - renda

Funcionario
    - nome;
    - sobrenome;
    - cpf;
    - matricula;

################################


##### Criando as classes conforme acima ######
class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Funcionando:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


cliente1 = Cliente('Andre', 'Carvalho', '134.224.535.32', 1343)
funcionario1 = Funcionando('Ricardo', 'Soares', '123.142.134.23', 3456)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

################################################
Aqui termina as classes criadas, vamos analisar
################################################

Obs : veja que tem muitos campos na classe que se repete como (nome, sobrenome, cpf) e também temos uma função
que se repete (nome_completo())

---> Neste sentido poderiamos economizar alguns caracteres, funções e deixa o código mais limpo e rápido.

Você deve sempre se PERGUNTAR: existe alguma entidade genérica o suficiente para encapsular os atributos
e métodos comuns a outras entidades?

# Como tempos campos comuns, podemos criar uma classe do tipo index com os prinicpais campos comuns
como (nome, sobrenome, cpf) --> para criar um nome legal para a classe, você deve pensar : Pinguim tem nome, sobrenome
e cpf, Não né, mas PESSOAS tem, então vamos criar como pessoas


Criando uma nova Classe:
- Aqui é onde começa a herança, se criamos esta classe podemos herda os atributos dela simplesmente adicionando nas
classe (Pessoa)

#####################

class Pessoa:

    def __index__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


####################

OBS: Quando uma classe herda de outra classe ela herda TODOS os atributos e métodos da classe herdada.

Quando uma classe herda de outra classe, a classe herdada é conhecida por:
    [Pessoa]
    - Super Classe;
    - Classe Mãe;
    - Classe Pai;
    - Classe Base;
    - Classe Genérica;

Quando uma classe herda de outra classe, ela é chamada:
    [Cliente,  Funcionario]
    - Sub Classe;
    - Classe Filha;
    - Classe Especial;

Como seria a leitura?
- Quem é nosso Super?
    - Pessoa
- Pessoa qual o construtor dela (nome, sobrenome, cpf)
Agora precisamos falar para as outra classe que iram usar os construtores da classe superior (SUPER)


# Como ficou nosso código agora:

class Pessoa:
    # Classe de herança
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    # Cliente herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionando(Pessoa):
    # Funcionário herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula


cliente1 = Cliente('Andre', 'Carvalho', '134.224.535.32', 1343)
funcionario1 = Funcionando('Ricardo', 'Soares', '123.142.134.23', 3456)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

# Sobrescrita de Métodos (Overriding)
- Sobrescrita de método, ocorre quando reescrevemos/reimplmentamos um método presente na super classe
em classes filhas
"""


class Pessoa:
    """Classe de herança"""

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    """Cliente herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionando(Pessoa):
    """Funcionário herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        return f'Funcionarios: {self.__matricula} Nome: {self._Pessoa__nome}'


cliente1 = Cliente('Andre', 'Carvalho', '134.224.535.32', 1343)
funcionario1 = Funcionando('Ricardo', 'Soares', '123.142.134.23', 3456)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())



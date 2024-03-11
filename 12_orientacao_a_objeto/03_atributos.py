"""
POO - Atributos

Atributos -> Representam as caracteristicas do objeto. Ou seja, pelos atributos
nós conseguimos representar computacionalmente os estados de um objeto.

Em Python, dividimos atributos em 2 grupos
- Atributos de instâncias;
- Atributos de Classe;
- Atributos Dinâmicos;

# Atributos de instância:

# Classes com atributos de instância publico
class Lampada:
    
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligado = False


class ContaCorrente:

    def __init__(self, numero, limite, valor):
        self.numero = numero
        self.limite = limite
        self.valor = valor


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

# Classes com atributos de instância privado
class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

# OBS: Lembre-se que isso é apenas convenção, ou seja, a linguagem Python não
# vai impedir que façamos o acesso aos atributos sinalizados como privados fora da classe.

# Exemplo:
# Veja que acima na classe Acesso nos temos dois atributos e somente o email esta publico

user = Acesso('user@gmail.com', 'womg492-1')

print(user.email)

# print(user.__senha) # Veja que seu o erro AttributeError, porque não temos acesso.

# Somente para conhecimento existe uma maneira de acessar, mas não é indicado

# print(dir(user)) # Veja que se você verificar todas as propriedade que você pode utilizar temos _Acesso__senha

print(user._Acesso__senha)  # Mais uma vez isso não é indicado! (Name Mangling)


 OBS:
- O (__init__) é um metodo construtor, ele foi feito para ajudar aconstruir o objeto quando
é instanciado.

- O (self) é uma palavra-chave utilizada no Python para referenciar a própria instância 
de uma classe. Em outras palavras, o self é utilizado para acessar os atributos e métodos de 
um objeto em particular

- O (self) pode ter outro nome no lugar, não é obrigatorio usar self, mas por convenção dos
programadores python eles preferem self.

- Em uma classe tudo que esta dentro dele é considerado um método, no caso acima, cada função
é um método e dentro destes metodos nos temos os atributos, que seria o itens que vamos trabalhar

- Em Python, por convenção, ficou estabelecido que, todo atributo de uma classe é público,
ou seja, pode ser acessado em todo projeto. Caso queiramos demostrar que determinado atributo
deve ser tratado como privado, ou seja, que deve ser acessando/utilizaodo somente dentro da
própria classe onde está declarado, utiliza-se o __ duplo underscore no inicio de seu nome.




# O que siguinifica atributos de instância?
class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha
    
    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)


# Significado, que ao criarmos instâncias/objetos de uma classe, todas as instancias
# terão estes atribuitos.

# Veja que temos dois objetos
user1 = Acesso('user1@gmail.com', 'Sevsdv34g')
user2 = Acesso('user2@gmail.com', 'sdv3v4v')

user1.mostra_email()
user2.mostra_email()

class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha
    
    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)


        


# Atributos de Classe

# Atributos de classe, são declarados diretamente na classe. Ou seja, fora do construtor. geralmente já inicializamos um valor, e este valor é compartilhado entre todas as instâncias da classe. Ou seja, ao invés de cada instância da classe ter seus próprios valores como é o caso dos atributos de instancias, com os atributos de classe todas as instancias terão o mesmo valor para este atributo.

class Produto:

    # Atributo de classe
    imposto = 1.05  # 0.05 de importo
    contador = 0

    def __init__(self, nome, descricao, valor):
        #Atributos de instância do objeto
        self.id = (Produto.contador + 1)
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


p1 = Produto('Playstation 4', 'Gamer', 2300)
p2 = Produto('Xbox 4', 'Gamer', 4500)


# Acesso possível, mas incorreto de atributo de classe.
print(p1.valor)
print(p2.valor)


# OBS: Não precisamos criar uma instância classe para fazer acesso a um atributo de classe, podemos acessar ele direto.
# Acesso correto, direto na classe.
print(Produto.imposto)


# Verificando se o incremento de ID está funcionando de contador
print(p1.id)
print(p2.id)

# OBS: em linguagens como o java, os atributos conhecidos como atributos de classe aqui em Python são chamados de atributos estáticos.


# Atributo dinâmicos ->  Um atributo de instância que pode ser criado em tempo de execução.
# OBS: O atributo dinâmico será excluido da instância que o criou.

p1 = Produto('Tênis Nike', 'Tênis', 234)
p2 = Produto('Camisa Nike', 'Camisa', 123)

# Criando um atributo dinâmico em tempo de execução
p1.peso = '0.2k'  # NOTA: que na classe Produto não existe o atributo peso!

print(f'Nome: {p1.nome}, Descrição: {p1.descricao}, Valor: {p1.valor}, Peso: {p1.peso}')
# print(f'Nome: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}') # não existe o peso aqui

# NOTA: atributos dinamicos é possivel, mas não é comum

# Este comando é muito interessante porque ele criar um dicionario mostrando todos os atributos de uma classe, como se fosse um ls
print(p1.__dict__)
print(p2.__dict__)


# Deletar um atreibuto
del p1.peso
del p1.valor


print(p1.__dict__)
print(p2.__dict__)
"""

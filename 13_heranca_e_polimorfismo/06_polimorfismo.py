"""
POO - Polimorfismo

- Poli -> Muitas
- Morfis -> Formas

Exemplos Polimorfismo
- Quando a gente reimplementa um método presenta na classe pai em classes filhas estamos realizando uma sobrescrita
uma sobrescrita de método (Overriding).
- Overriding é a melhor representação do polimorfismo

Iremos ver um método que precisamos declarar em todas as classes criadas como filhas
Exemplo;
- Vamos imagina que você criou uma classe igual abaixo

class Animal(object):

    def __init_(self, nome):
        self.__nome = nome

    def falar(self):
       raise NotImplementedError('A classe filha precisa implementar este método')

Veja que criamos o construtor da nossa classe que seria o primeiro def e também criamos um método falar que nele
tem somente uma excessão.


Agora vamos criar uma classes recebendo os métodos de outra classe chamada Animal

class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self)
        print(f'O {self._Animal__nome} fala miau')


Veja acima no método falar que estou re-escrevendo o método falar que vai ser pego da classe Animal
é isso que é o polimorfismo, veja o exemplo completo abaixo copie e cole na sua ideia para ver o resultado.



class Animal(object):

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar este método')

    def comer(self):
        print(f'{self.__nome} está comendo...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala wau wau')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala miau!')

class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala algo...')


# Testes
pluto = Cachorro('Pluto')
pluto.comer()
pluto.falar()

felix = Gato('Felix')
felix.comer()
felix.falar()

mickey = Rato('Mickey')
mickey.comer()
mickey.falar()


"""



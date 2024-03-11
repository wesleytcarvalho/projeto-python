"""
POO - MRO - Method Resolution Order

Method Resolution Order (Reslução de Ordem de Métodos), é a ordem de execução dos métodos (quem será executado primeiro)
- Conseguimos ver isso indo até o console python e executando os seguintes comandos.
    # PRIMEIRA FORMA DE VERIFICAR A ORDEM DE PRECEDÊNCIA
    - from mro import Pinguim
    - Pinguim.__mro__
        ((<class 'heranca_e_polimorfismo.mro.Pinguim'>, <class 'heranca_e_polimorfismo.mro.Terrestre'>,
        <class 'heranca_e_polimorfismo.mro.Aquatico'>, <class 'heranca_e_polimorfismo.mro.Animal'>, <class 'object'>))
    - Podemos isar também: Pinguim.mro()
        [<class 'heranca_e_polimorfismo.mro.Pinguim'>, <class 'heranca_e_polimorfismo.mro.Terrestre'>,
        <class 'heranca_e_polimorfismo.mro.Aquatico'>, <class 'heranca_e_polimorfismo.mro.Animal'>, <class 'object'>]

    # SEGUNDA FORMA
    - help(Pinguim)

Help on class Pinguim in module heranca_e_polimorfismo.mro:
class Pinguim(Terrestre, Aquatico)
 |  Pinguim(nome)
 |
 |  Method resolution order:
 |      Pinguim
 |      Terrestre
 |      Aquatico
 |      Animal
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  __init__(self, nome)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  __annotations__ = {}
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from Terrestre:
 |
 |  andar(self)
 |
 |  cumprimetar(self)
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from Aquatico:
 |
 |  nadar(self)
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Animal:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)

"""
class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimetar(self):
        return f'Eu sou {self.__nome}'
        
class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)
    
    def nadar(self):
        return f'Eu sou {self._Animal__nome} está nadando.'

    def cumprimetar(self):
        return f'Eu sou {self._Animal__nome} do mar!'
    
class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} da terra!'
    
    def cumprimetar(self):
        return f'Eu sou o {self._Animal__nome}  da terra!'

class Pinguim(Terrestre, Aquatico):

    def __init__(self, nome):
        super().__init__(nome)

# Testando
tux = Pinguim('Tux')
print(tux.cumprimetar())
print('')

"""
Ordem de herança e sua saída
: class Pinguim(Aquatico, Terrestre):
: Eu sou Tux do mar!

Mudando a ordem
class Pinguim(Terrestre, Aquatico):
Eu sou o Tux  da terra!
"""


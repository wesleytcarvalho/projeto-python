"""
POO - Henrança multipla

Herança Múltipla nada mais é do que a possibilidade de uma classe herdar de múltiplas classes, fazendo com que a classe
filha herde todos os atributos e métodos de todas as classes herdadas.


Obs: A herança múltipla pode ser de duas maneiras:
     - Por multiderivação Direta;
     - Por multidetivação indireta;


# Exemplo 1 - Multiderivação Direta

class Base1:
    pass

class Base2:
    pass

class Base3:
    pass

class MultiDerivado(Base1, Base2, Base3):
    pass


# Exemplo 2 - Multiderivado indireto

class Base1:
    pass

class Base2(Base1):
    pass

class Base3(Base2):
    pass

class MultiDetivado(Base3):
    pass
    
OBS: Não importa se a derivação é direta ou indireta. A classe que realizar a henrança herdará todos
atributos e métodos das super classes.
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

class Pinguim(Aquatico, Terrestre):

    def __init__(self, nome):
        super().__init__(nome)

# Testando

baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimetar())
print('=+='*3)
print('')

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimetar())
print('=+='*3)
print('')

tux = Pinguim('Tux')
print(tux.andar())
print(tux.nadar())
print(tux.cumprimetar()) # Ele vai executar qual comprimento? Terra! isso se chama (Method Resolution Order - MRO)
print('')

# OBS: Sempre vai valer o primeiro ocorrencia na ordem da herança.
#       class Pinguim(Aquatico, Terrestre):

# Como descobrir se uma Objeto é instancia?

print(f'Tux é instância de Pinguim: {isinstance(tux, Pinguim)}') 
print(f'Tux é instância de Aquativo: {isinstance(tux, Aquatico)}')
print(f'Tux é instância de Terrestre: {isinstance(tux, Terrestre)}')
print(f'Tux é instância de Object: {isinstance(tux, object)}')
"""
Quando executamos um código durante o desenvolvimento, geralmente é para testá-lo. Embora seja uma prática útil, ainda estamos realizando testes de forma manual. O objetivo é automatizar esse processo.

Por que devemos testar nosso código?
    - Reduzir a ocorrência de bugs no código existente.
    - Garantir que novos recursos da aplicação não interfiram nos recursos existentes.
    - Assegurar que bugs corrigidos anteriormente permaneçam corrigidos.
    - Evitar que a refatoração introduza novos bugs.
   
TDD - Desenvolvimento Guiado por Testes (Test Driven Development)
    - Inicie escrevendo os testes antes do código.
    - Em seguida, escreva o código mínimo necessário para que o teste seja bem-sucedido.
    - Refatore o código para implementar a funcionalidade e execute os testes novamente.
    - Uma vez que os testes passem, o recurso é considerado completo.
    - Dessa forma, ao adotar o TDD, é possível garantir que o código seja testado de forma abrangente e que novas     funcionalidades sejam implementadas de maneira segura e confiável.

Estes estágios de desenvolvimento do TDD são quase como um mantra que os desenvolvedores seguem, conhecidos como.
    - Red;
    - Green
    - Regactor;

Nos tesmos este codigo para testar, exemplo abaixo

class Gato:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome
    
    def miar(self):
        print(f'{self.__nome} está miando..')


# Agora vamos estanciar a classe
felix = Gato('Felix')

felix.miar()

print(felix.nome)


Executamos....tudo OK!!

Quando estamos criando nossos testes primeiro começamos pelo objeto estanciado e depois que criamos o codigo



"""

class Gato:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome
    
    def miar(self):
        print(f'{self.__nome} está miando..')


felix = Gato('Felix')

felix.miar()

print(felix.nome)




 
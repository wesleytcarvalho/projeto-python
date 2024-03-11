"""
Escrevendo iterador customizado

NOTA: Está aula não vai fazer muito sentido porque ainda não aprendemos Orientação a Objeto, mas assim que você
Estudar volta aqui!

Iremos criar aqui uma o range que temos no FOR
# Exemplo com a função range()
for i in range(10):
    print(i)

# Como poderiamos fazer para criar um range() nosso
class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration

# Testando se conseguimos iterar
con = Contador(1, 4)
# NOTA: Ele irá mostra um objeto, mas não mostra o resultado precisamos usar o iter()

# Preciso converter o dado para iterable
it = iter(con)

# Agora vou iterar com o iteravel next
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# NOTA:  Veja o que fiz aqui
# - Veja que repetir 4 vezes para ele iterar com meu contador, então
# - o contador é meu range(), podemos utilizar agora o contador no for

for i in Contador(1, 4):
    print(i)
"""

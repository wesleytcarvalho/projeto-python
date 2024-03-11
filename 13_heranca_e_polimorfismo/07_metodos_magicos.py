"""
POO - Métodos mágicos
dunder init -> __init__()
- O init é um método mágico que seria nosso construtor que cria nosso objeto e Dunder siguinifica, Double Underscore.

# Exemplo de código 1 #

class Livros:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas


livro1 = Livros('Pytonanico', 'Andre Soares', 400)
livro2 = Livros('Programacao Python', 'Fernanda Lima', 500)

print(livro1)
print(livro2)

OBS: Quando rodamos o código acima ele da os seguintes itens abaixo
<__main__.Livros object at 0x10e4f5dc0>
<__main__.Livros object at 0x10e4f5df0>

Leitura:
__main__.Livros = Classe principal
object = do tipo objeto
0x10e4f5df0 = no endereço de memória


Como podemos ler este código com uma str, int, float, não temos um método especial, ou seja, um método mágina que mostra
para nós o que temos no nosso objeto que seria:
__repr__ = dunder repr, representação do objeto

# Exemplo de código 2 #

class Livros:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas


# Geralmente utilizamos este método mágico para quando estamos desenvolvendo, Não para usuário final, mas quase não
tem diferença

    def __repr__(self):
        return f'{self.titulo} escrito por {self.autor} com {self.paginas} páginas'


livro1 = Livros('Pytonanico', 'Andre Soares', 400)
livro2 = Livros('Programacao Python', 'Fernanda Lima', 500)

print(livro1)
print(livro2)




"""

class Livros:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):
        return f'{self.titulo} escrito por {self.autor} com {self.paginas} páginas'

    def __str__(self):
        return self.titulo

    def __len__(self):
        return self.paginas

    def __del__(self):
        print('Um objeto do tipo livro foi deletado da memoria')

    def __add__(self, outro):
        return f'{self} - {outro}'

    def __mul__(self, outro):
        if isinstance(outro, int):
            msg = ''
            for n in range(outro):
                msg += ' ' + str(self)
            return msg
        return 'Não posso multiplicas'


livro1 = Livros('Pytonanico', 'Andre Soares', 400)
livro2 = Livros('Programacao Python', 'Fernanda Lima', 500)

print(livro1)
print(livro2)

print(len(livro1))
print(len(livro2))

# del livro2
# del livro1

print(livro1 + livro2)

print(livro1 * 3)

"""
Entendendo Iterators e iterables
Python | Diferença entre iterável e iterador

Iteradores (Iterators)
    - Um objeto que pode ter iterado.
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamado;

Iteráveis (Iterables)
    - Um objeto que irá retornar um iterator quando a função iter() for chamada

Exemplo:
    - nome = 'Uday'
    - numero = [1, 2, 3, 4, 5]

Veja acima que temos duas variáveis que podem ser iteraveis, mas eu ainda preciso de algo para criar este iterável
como por exemplo o FOR.

nome = 'Uday'  # É um iterável, mas não é um iterador
numero = [1, 2, 3, 4, 5]  # É um iterável, mas não é um iterador

iteravel1 = iter(nome)
iteravel2 = iter(numero)

- Listas, tuplas, dicionários e conjuntos são todos objetos iteráveis. Eles são contêineres iteráveis dos quais você
pode obter um iterador.
- Todos esses objetos possuem um iter() método que é usado para obter um iterador:

# Observe abaixo que para iterar eu preciso da função next() e o iter() é o iterador
# - Veja que para eu iterar com cada item eu preciso inserir prints ate da a quantidades de elementos, passou disso
# irá da erro.

# Variavel nome
print(next(iteravel1))
print(next(iteravel1))
print(next(iteravel1))
print(next(iteravel1))
# print(next(iteravel1))  # se eu inserir este irá da o erro StopIteration, porque não existe

# Variavel numero
print(next(iteravel2))
print(next(iteravel2))
print(next(iteravel2))
print(next(iteravel2))
print(next(iteravel2))
# print(next(iteravel2))  # se eu inserir este irá da o erro StopIteration, porque não existe

NOTA: Para você criar qualquer coisa em um iteravel, podemos usar a função iter(), quando você usa o iter() ele
transforma em um objeto do tipo iteravel, mas ele não mostrar a iteração para isso usamos a função next() para iterar.

"""

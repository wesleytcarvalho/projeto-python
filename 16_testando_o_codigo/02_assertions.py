"""
Assertions (Afirmações/Checagem/Questionamento)

Em Python utilizamos a palavra reservada 'assert' para realizar uma simples afirmação utilizadas nos testes.

Utilizamos o 'assert' em uma expressão que queremos checar se é válido ou não. Se a expressão for verdadeira, retorna None e caso seja falsa levanta um erro do tipo AssertionsError.

OBS: 
- Nós podemos especificar, opcionalmente, um segundo argumento ou mesmo uma mensagem de erro personalizada.
- A palavra 'assert' pode ser utilizada em qualquer função ou código nosso....não precisa ser exclusivamente nos testes.

Abra o console Pythone e faça o seguinte teste assert 4 == 4 se ele não aparecer nada é porque o resultado foi None, ou seja, verdadeira agora fassa assert 4 == 2 irá aparecer o erro AssertionError.

# Exemplo 1

def soma_numeros_positvos(a, b):
    assert a > 0 and b > 0, 'Ambos os numeros precisam ser positivos'
    return a + b

print(soma_numeros_positvos(3, 2))


# Exemplo 2

def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'doces',
        'amburger com batata frita',
    ], 'A comida precisa ser fast food dos itens'
    return f'Estou comendo {comida}'

comida = input('Informe a comida: ')
print(comer_fast_food(comida))


# ALERTA: Cuidado ao utilizar  'assert'
- Se um programa Python for executado com o parâmetro -O nenhuma assertion será validado. Ou seja, todos as suas validações já eram.

Teste com este comando "python3 -O 02_assertions.py" e insera alguma coisa que esta fora da lista da função acima, veja que ele não deu erro então tome muito cuidado ao usar o assert, 
"""

def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'doces',
        'amburger com batata frita',
    ], 'A comida precisa ser fast food dos itens'
    return f'Estou comendo {comida}'

comida = input('Informe a comida: ')
print(comer_fast_food(comida))



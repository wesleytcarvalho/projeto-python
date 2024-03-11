"""
Geradores
- Geradores (Generators) são Iterators (Iteradores)

Obs: O contrário não é verdadeiro, ou seja, nem todo interator é um generator

Outras informações:
- Generators podem ser criados com função geradoras;
- Função geradoras utilizam a palavra reservada yield;
- Generators podemos criar Expressões Geradoras;

Diferente entre Funções e Generator Functions (Funções geradoras)
------------------------------------------------------------------------------
| +++ Funcoes ++++                      | +++++ Generator Functions ++++++   |
------------------------------------------------------------------------------
| Utilizam return                      |  Utilizam yield                     |
------------------------------------------------------------------------------
| Retorna uma vez                     |  Podem utilizar yield multiplas vezes |
------------------------------------------------------------------------------
| Quando executada, retorna um valor | Quando executado, retorna um generator|
------------------------------------------------------------------------------

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1

# Obs: Uma generator functions não é um generator. Ela gera um generator.

con = conta_ate(4)

print(next(con))
print(next(con))
print(next(con))
print(next(con))
# print(next(con))  # StopIteration

# Usando com FOR
gen = conta_ate(10)
for num in gen:
    print(num)

# Obs quando usamos a funcao para gerar um numero ele não inserir mais este numero na sequência  ele começa
# com o número subsequente
gen = conta_ate(10)
print(next(gen))  # Estou gerando o número 1
print('-------')
for num in gen:
    print(num)

gen = list(conta_ate(10))
print(gen)

# Então, o fim da miada é o "yield" quando você executa a função conta_ate() ele fica esperando até
# todo o conteúdo da função seja executada
"""
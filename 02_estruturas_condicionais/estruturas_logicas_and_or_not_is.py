"""
Estruturas Lógicas: and (e), or (ou), not (não), is (é)

Operadores unários, este operador precisa somente de valor
 - not
Operates binários, precisa de 2 valores
 - and, or, is

Regras de funcionamento:
- Para o 'end' ambos os valores precisam ser TRUE
- Para o 'or' um ou outro valor precisa ser TRUE
- Para o 'not' o valor do boleano é invertido, ou seja, se for True vira Falso, se for falso vira True

# Exemplo de END
ativo = True
logado = True

if ativo and logado:
    print('Bem-vindo usuário')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')

# Exemplo de OR
if ativo or logado:
    print('Bem-vindo usuário')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')

# Exemplo de NOT
if not ativo:
    print('Você precisa ativar sua conta')

"""

# Exemplo de NOT
if not ativo:
    print('Você precisa ativar sua conta')

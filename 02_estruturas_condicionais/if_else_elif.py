"""
Estrutura condicionais: if, else, elif

# Exemplo: Verificando idade usando if, elif e else
# Isso se chama condição composta

idade = int(input('Digite sua idade: '))
if idade < 18:
    print('Menor de idade')
else:
    print('Maior de idade')


# Condição aninhada
nome = str(input('Digite seu nome: '))
if nome == 'Andre':
    print('Que nome bonito')
elif nome == 'Jose' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Claudia Juliana':  # Se em nome ESTIVER(in) algumas das strings ('Ana Claudia Juliana')
    print('Belo nome Feminino')
else:
    print('Seu nome pe bem normal. ')
print(f'Tenha um bom dia {nome}')


"""




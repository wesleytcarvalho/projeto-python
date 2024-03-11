"""
Tipo String

Em python, um dado é considerado do tipo string sempre que:
- Estiver entre àspas simples ou duplas: 'Uma string' ou "Uma string"
- Estiver entre àspas simples ou duplas triplas: '''Uma string''' ou ""Uma string""


# Aspas simples ou duplas (o mais comum é usar aspas simples)
nome = 'Uday Academy'
print(nome)
print(type(nome))


# Quando temos apostrofi (Você precisa usar aspas duplas)
nome = "Gina's Bar"
print(nome)
print(type(nome))

# Claro que se eu quiser usar as simples em tudo eu posso usar, mas precisamos do caractere de escape "\"
nome = 'Gina\'s Bar'
print(nome)
print(type(nome))

# Pulando linha
nome = 'Bebe \nLay'
print(nome)
print(type(nome))

nome = 'Bebe Lay'

# Deixando tudo maiúsculo
print(nome.upper())

# Deixando em minuscolo
print(nome.lower())

# Separando as palavras em Lista ele separa verificando os espacos, mas podemos colocar apartir de algum caractere
print(nome.split())

# NOTA: Uma string é uma lista, sabendo disso a palavra 'Bebe Lay' está indexado ficando assim
Lista = ['B', 'e', 'b', 'e', ' ', 'L', 'a', 'y']
index = [ 0,   2,   3,   4,   5,   6,   7,   8 ]

Sabendo que eles tem indices podemos trabalhar ele.

nome = 'Bebe aLy'
print(nome[1:3])

print(nome[:-1])

print(nome[1:8:2])


nome = 'Uday Academy'

# Se eu quisesse pegar tudo que tem na frente ate qualquer coisa depois de 4 posicoes
print(nome[:4])  # Slice de string

# Se eu quisesse pegar do Univercity pra frente
print(nome[5:])  # Slice de string

# Para você separar cada elemento dentro de ums string é só usar a função o split()
# OBS: para esta função ele separa por default por espaço, mas podemos colocar o carateres que usermos, ou seja,
# split(',')

print(nome.split())

#  uma coisa legal também como o split() ele cria uma lista já podemos acessar o elemento, ou seja,
# Vamos imagina que você quer pegar primeira ocorrência dentro da palavra 'Uday Academy' então,
# você usar o split() para isso, veja abaixo

print(nome.split()[0])  # Uday


# Como é feito esta indexação
# [  0,          1     ]
# ['Uday', 'University']
print(nome.split()[1])  # University
print(nome.split()[0])

nome = 'Uday Academy'

# Como trabalhar com cada elemento de Uday Academy
# [::-1] comece até o primeiro elemento, vá até o último elemento e inverta
print(nome[::-1])

# Inverter a string
print(nome.replace('G', 'P'))
"""
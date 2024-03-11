"""
Manipulando Data e Hora

Python tem um módulo built-in (integrado) para se trabalhar com data e hora chamado datetime
import datetime

# Como podemos verificar o que temos neste modulo
print(dir(datetime))

# Costante de ano 9999
print(datetime.MAXYEAR)

# Costante Minimo de ano entao vai de 1 a 9999
print(datetime.MINYEAR)

# Retorno de data e hora 2023-11-24 14:15:55.166324
print(datetime.datetime.now())

# Como é presentado este método
print(repr(datetime.datetime.now()))

# replace() para fazer ajustes na data/hora
inicio = datetime.datetime.now()

print(inicio)

# Alterar o hor[ario para 16 horas, 0 minuto, 0 segund, 0 microsegund
inicio = inicio.replace(hour=14, minute=0, second=0, microsecond=0)

print(inicio)

# E se quisemos criar ou customizar data e hora, vamos aprender isso agora.

evento = datetime.datetime(2023, 1, 1, 0)

print(type(evento))  # Veja aqui que temos uma data Python

print(type('31/12/2023'))  # Veja que isso nada mais é que uma string

print(evento)


# Agora você deve está se perguntando como receber uma data de um usuário e transforma em uma data Python;
nascimento = input('Informe sua data de nascimento (dd/mm/yyyy): ')

print(nascimento)

print(type(nascimento))  # Mesmo recebendo do usuario ainda esta em String

nascimento = nascimento.split('/')  # Aqui eu recebo o dado e separo os elemento pela barra criando uma lista

print(nascimento)

print(type(nascimento))  # Agora o tipo de dado é uma lista

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))
# NOTA: Acima eu estou converto de string para int

print(nascimento)

print(type(nascimento))  # Agora veja que esta sendo convertido para datetime e recebendo do usuario.

evento = datetime.datetime.now()

# Acessa individual dos elemento de data e hora
print(evento.year)
print(evento.month)
print(evento.day)
print(evento.hour)
print(evento.minute)
print(evento.second)
print(evento.microsecond)

# Verificando as possibilidades
print(dir(evento))
"""




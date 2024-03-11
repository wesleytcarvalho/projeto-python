"""
Método de data e hora

# Com now() podemos especificar um timezone (Fuso Horário)
agora = datetime.datetime.now()  # now == agora
print(agora)
print(type(agora))
print(repr(agora))

hoje = datetime.datetime.today()  # today == hoje
print(hoje)
print(type(hoje))
print(repr(hoje))

# Mudanças ocorrendo à meia-note combine()
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao)
print(type(manutencao))
print(repr(manutencao))


# Encontrando o dia da semana. weekday()
#  Os dias da semana do método weekday() começa em 0, sendo esta a segunda-feira

# 0 - Segunda-feira (Monday)
# 1 - Terça-feira (Tuesday)
# 2 - Quarta-feira (Wednesday)
# 3 - Quinta-feira (Thursday)
# 4 - Sexta-feira (Friday)
# 5 - Sábado (Saturday)
# 6 - Domingo (Sunday)

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao.weekday())


aniversario = input('Qual sua data de nascimento? dd/mm/yyyy: ')

aniversario = aniversario.split('/')

aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[0]), day=int(aniversario[0]))

if aniversario.weekday() == 0:
    print('Você nasceu numa segunda-feira')
elif aniversario.weekday() == 1:
    print('Você nasceu numa terça-feira')
elif aniversario.weekday() == 2:
    print('Você nasceu numa quarta-feira')
elif aniversario.weekday() == 3:
    print('Você nasceu numa quinta-feira')
elif aniversario.weekday() == 4:
    print('Você nasceu numa sexta-feira')
elif aniversario.weekday() == 5:
    print('Você nasceu num sabado')
elif aniversario.weekday() == 6:
    print('Você nasceu num domigo')
"""

import datetime

# Formatando datas/horas com strftime() (string format time)
hoje = datetime.datetime.today()

print(hoje)

hoje_formatada = hoje.strftime('%d/%m/%Y')

print(hoje_formatada)

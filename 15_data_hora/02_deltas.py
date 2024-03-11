"""
Trabalhando com deltas de data e hora

data_inicial = dd/mm/yyyy 12:55:34.5678
data_final = dd/mm/yyyy 13:55:34.5678

delta = data_inicial - data_final



import datetime

# Data de hoje
data_hoje = datetime.datetime.now()

# Data para ocorrer determinado evendo
aniversario = datetime.datetime(2024, 7, 10)

# calculando o delta
tempo_para_evento = aniversario - data_hoje

print(type(tempo_para_evento))

print(repr(tempo_para_evento))

print(tempo_para_evento)

print(f'Faltam {tempo_para_evento.days} dias, {tempo_para_evento.seconds // 60 // 60} horas..')

data_da_compra = datetime.datetime.now()

print(data_da_compra)

regra_boleto = datetime.timedelta(days=3)

print(regra_boleto)

vencimento_boleto = data_da_compra + regra_boleto

print(vencimento_boleto)
"""


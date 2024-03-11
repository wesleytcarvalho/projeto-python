# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
# F - Feminino, M - Masculino, Sexo Inválido.

origem = str(input('Digite M - Masculino ou F - Feminino: '))
if origem in 'm':
    print('Entendi! Você é Masculino')
elif origem in 'f':
    print(f'Entendi! Você é Feminino ')
else:
    print('Você não é nenhuma das opções, \ntente novamente mais tarde!')
"""
Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado das componentes deste vetor, armazenando
o resultado em outro vetor. Os conjuntos têm 10 elementos cada. Imprimir todos os conjuntos.
"""
valor_resultado = set({})
reais = set({})
resposta = ''
while resposta != 'sair':
    reais.add(float(input('Digite o primeiro valor: ')))
    reais.add(float(input('Digite segundo valor: ')))
    reais.add(float(input('Digite terceiro valor: ')))
    reais.add(float(input('Digite quarto valor: ')))
    reais.add(float(input('Digite quinto valor: ')))
    resposta = input('Digite sair para [sair] ou [enter] pra continuar: ')

soma = sum(reais)
quadrado = soma ** 2
valor_resultado.add(quadrado)

print('------------------------------')
print(f'Os valores [reais]: {reais}')
print(f'Valor [Total]: {valor_resultado}')


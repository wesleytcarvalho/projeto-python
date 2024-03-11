"""
Escrevendo em arquivos

# OBS: Ao abrir um arquivo para leitura, não podemos relaizar a escreita nele. Apenas ler.
Da mesma forma, se abrirmos um arquivo para escrita, não podemos lê-lo, somente escrever nele.

# OBS: Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional

- Para escrevermos dados em um arquivo, após abrir um arquivo utilizandos a função write().
- Esta função recebe uma string como parâmetro, caso contrário teremos um TypeError.
- Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existe será criado,
caso ele já exista, o anterior srá apagado e uma nova será criado. Dessa forma, todo
conteúdo anterior será perdido.

# Exemplo de escrita - modo 'w'  - write (escrita)
# Forma Pythonica de fazer (indicado)
with open('novo.txt', 'w') as arquivo:
    arquivo.write('Novo dados.\n')
    arquivo.write('Outros.\n')
    arquivo.write('Esta é a última linha.\n')


# Forma tradicional de escrita em arquivo (Não Pythonica)
arquivo = open('mais.txt', 'w')

arquivo.write('Um texto qualquer.\n')
arquivo.write('Mai um texto.\n')

arquivo.close()
print(arquivo.closed)

# Exemplo 1
with open('Uday.txt', 'w') as arquivo:
    arquivo.write('Uday\n' * 100)

Exemplo 2
with open('user.txt', 'w') as usuario:
    usuario.write(str(input('Qual seu nome: ')))

Exemplo 3 um pouco mais avancado
with open('fruta.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe uma frunta: ')
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break
"""



"""
Bloco with
Passos anteriores de como se trabalhar com arquivo
1 - abrir o arquivo
arquivo = open(texto.txt)
2 - trabalhar com o arquivo
print(arquivo.read())
3 - fechar o arquivo
arquivo.clouse()
print(arquivo.cloused)

Usando o bloco with
- O bloco with é utilizado para criar um contexto de trabalho onde os recursos
utilizados são fechados apos o bloco with.

with open('texto.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)

# Veja que o print que está dentro da estrutura with ele mostra False
# porque o arquivo ainda está aberto, agora com o print abaixo comprova
# que quando termina a estrutura do with ele mesmo fecha a conexão com o arquivo.
print(arquivo.closed)
"""

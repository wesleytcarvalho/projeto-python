"""
Criando seu própria verão de loops

# FOR
for num in [1, 2, 3, 4,]:
    print(num)

for letra in 'Uday Academy':
    print(letra)

# Por debaixo dos panos o for usa o iter()
iter([1, 2, 3, 4])
iter('Uday Academy')

# Criando um função
def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

meu_for([1, 2, 3, 4])
meu_for('Uday Academy')
"""






"""
3. Write a Python function to multiply all the numbers in a list.
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336
"""

def multiplicacao(lista):
    mult = 1
    for i in lista:
        mult = mult * i
    return mult


lista = [8, 2, 3, -1, 7]


print(multiplicacao(lista))
# Write a Python program to import a built-in array module and display the namespace of the said module.

"""
Esse código é útil para inspecionar quais atributos estão presentes em um objeto específico, o que pode 
ser particularmente útil para depuração ou introspecção. No entanto, é importante usar esse tipo de reflexão 
com cuidado, especialmente em um ambiente de produção, pois pode expor detalhes internos do objeto que normalmente
não devem ser acessados diretamente.

Isso pode ser feito no terminal tambem no terminal entre como python e digite
# import sys
Agora veja os atributos com o comando abaixo
# dir(sys)

"""

import sys

for nome in sys.__dict__:
    print(nome)
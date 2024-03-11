"""
Dunder Name e Dunder Main
- Dunder -> Doble Under
- Dunder Name -> __name__
- Dunder Main -> __main__

Em Python, são utilizados dunder para criar funções, atributos, proriedades e etc, utilizando Double Under para
não gerar conflito com os nomes desses elementos na programação.

# Em Python, se executarmos um módulo Python diretamente na linha de comando, internamente o python atribuirá à variável
 __name__ o valor __main__ indicando que este módulo é o módulo de execução principal.

# Vamos criar um exemplo aqui, veja que eu utilizo o pacote Uday1, dentro dele tem uma função e um print, mas veja
# se eu importa este pacote e pegar somente a função ele também vai imprimir o print que tenho dentro deste arquivos
# Então, então ele está entendendo que esse arquivo Uday1 é o nosso principal arquivo de execução, mas não é
# nosso princial arquivo é o pacote é a função "Uday1.funcao1(12, 5)" então eu não quero que ele imprima o print que
# temos dentro deste arquivos.

from Uday import Uday1
print(Uday1.funcao1(12, 5))

# Agora veja no arquivo Uday1 que agora ele só vai ser executado se ele estiver no pacote direto, ou seja, executar o
# o proprio Uday1, se por acaso eu chamar ele de outros lugares ele não vai mais imprimir porque ele não é mais
# o principal, ou seja, a variavel __name__ vai receber outra coisa não mais o __main__
"""

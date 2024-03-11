"""
Definindo Funcoes
- Funcoes sao pequenas parte do codigo que realizam tarefas especificas:
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muito uteis para executar procedimento similares por repetidas vezes;

Obs: Se você escrever uma função que realiza várias tarefas dentro dela;
é bom fazer uma verificação para que a função seja simplificada.

Já utilizamos várias funcões desde que iniciamos este curso:
- print()
- len()
- max()
- count()
-e muitos outros;


# Em python, a forma geral de definir uma função é:
def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao

    
Onde:
- def -> palavra reservada para definir uma função
- nome_da_funcao  -> SEMPRE, com letras minusculas, e se for nome composto, separado por underline
- bloco_da_funcao -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece.
Neste bloco, pode ter ou não retorno da função

# Definindo as primeiras funções

def diz_oi():
    print('oi')

Obs:
1 - Veja que, dentro das nossas funções podemos utilizar outras funções;
2 - Veja que nossa função só executa uma tarefa, ou seja, a única coisa que ela faz é dizer oi;
3 - Veja que esta função não recebe nenhum parametro de entrada;
4 - Veja que está função não retorna nada;

# Definindo a primeira função
def diz_oi():
    print('oi')

# utilizando a função
diz_oi()

# ATENÇÃO
Nunca esqueça de utilizar o parenteses ao executar uma função;
Exemplo:
# Errado
diz_oi
# Certo
diz_oi()
# Errado
diz_oi () # não tem espaços no pareteses

# Exemplos 2
def cantar_parabens():
    print('Parabens para voce')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')

# Estou rodando a função 5 vezes
for n in range(5):
    cantar_parabens()

"""
"""
NOTA: Precisa estudar mais esta sessao

Links
- https://www.w3resource.com/python-exercises/decorator/index.php

Decoradores (Decorators)
Os decoradores em Python são uma maneira de modificar o comportamento de uma função ou classe sem modificar diretamente
seu código. Eles permitem que você envolva uma função ou classe em torno de outra função, adicionando funcionalidade
adicional antes, depois ou em torno da execução da função original. Os decoradores são indicados pelo símbolo @ seguido
pelo nome da função decoradora. Eles fornecem uma maneira concisa e reutilizável de estender a funcionalidade do código
Python. Eles são comumente usados para registro, autenticação, cache e muito mais.

O que são Decorators?
- Decorators são funções;
- Decorators envolvem outras funções e aprimora seus comportamentos;
- Decorators também são exemplos de Higher Order Functions;
- Decorators tem uma sintaxe própria, usando "@" (Syntact Sugar / Acucar Sintatico)

# Decorators como funcoes (Sintaxe nao recomendada / Sem Acucar Sintatico)

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer voce! ')
        funcao()
        print('Tenha um otimo dia! ')
    return sendo



def saudacao():
    print('Seja bem-vindo a UDayTC')


# Testando 1
teste = seja_educado(saudacao)
teste()


# Testando 2
def raiva():
    print('EU NAO GOSTO DE VOCE')

raiva_educada = seja_educado(raiva)
raiva_educada()


OBS:
- Podemos falar que a função está decorando a outra função para ser executgado


# Decorators como Syntax Sugar (Açucar Sintático ---USO RECOMENDADO----)

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você! ')
        funcao()
        print('Tenha um otimo dia! ')
    return sendo_mesmo


#  Veja que aqui é o que muda, eu quero que a função "seja_educado_mesmo" consiga executar esta função
# então eu passo o @mais o nome da função decoradora
@seja_educado_mesmo
def apresentando():
    print('Meu nome é Jose')


# Testando
apresentando()


@seja_educado_mesmo
def dormir():
    print('Quero dormi! ')


dormir()


Não é uma opção funcional, mas o Decoretor é muito utilizado em páginas web para avaliar o comportamento do site
# OBS: este exemplo abaixo não é funcional, mas vamos entender ela
# Vamos imagina o seguinte menu
|------------------------------------------------------|
| Home   |  Servicos  | Produtos  | Administrativo     |
|------------------------------------------------------|


def checa_login():
    if not resquest.usuario:
        redirect('https://uday.com.br')

def home(request):
    return 'Pode acessar home'

def servico(request):
    return 'Pode acessar home'

def produto(request):
    return 'Pode acessar home'

@checa_login
def home(request):
    return 'Pode acessar home'


OBS: Nao confunda Decorator com Decoretor Function
- Decorator e o que inicia com @funcao
- Decorator Function e a funcao propriamente dito decorador
"""

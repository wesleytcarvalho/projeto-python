"""
Introdução ao módulo Unittest

Unittest -> Testes Unitários

O que são testes unitários?
- Teste é a forma de se testar unidades individuais de código fonte.
- Unidades individuais podem ser: funções, métodos, classes módulo etc.

# OBS: Teste unitário não é especifico da linguagem Python

Para criar nossos testes, criamos classes que herdam de unittest.TestCase e apartir de então
ganhamos todos os 'assertions' presentes no módulo.

Para rodar os testes, utilzamos unittest.main()

Para exemplificar melhor nossa pratica, vamos criar dois arquivos um chamado atividades.py que seria exatamente o codigo que queremos testar e nossos teste em especifico chamado de teste.py

# Conhecendo os assertions do unitttest
https://docs.python.org/3/library/unittest.html

###########################

if __name__ == '__main__':
    unittest.main()

Claro! Então, o name em Python é como se fosse o nome de uma pessoa. Quando uma pessoa está sozinha, ela usa seu próprio nome. Mas quando ela está em um grupo, ela pode usar um apelido ou um nome diferente. Em Python, o name é como o nome da pessoa, mas pode mudar dependendo de onde o código está sendo executado.

Quando o código está sendo executado sozinho, o name é igual a "main".
Mas quando o código está sendo importado por outro arquivo, o name é igual ao nome do arquivo.

Então, o name ajuda o Python a entender se o código está sendo executado sozinho ou se está sendo importado por outro código. Espero que isso ajude a entender!

Por convenção, todos os testes em um test case devem ter seu nome iniciado com test_
"""

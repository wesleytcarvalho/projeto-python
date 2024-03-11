"""
utilizando dir e o help para auxiliar na procura de comandos

dir -> Apresenta todos os atributos/propriedades e função/metodos disponiveis
para determinar o tipo de dados ou variável.

help - Apresenta a documentação de como utilizar os atributos/propriedades e funcoes/metodos
disponiveis para determinar o tipo de dado ou variavel

Vamos imagina o seguinte cenário
Digito no terminal: 'UdayTC'
Se eu quero saber o tipo de dados estamos utilizando no 'UdayTC' eu utilizado o dir
dir('UdayTC')

Veja tudo que posso fazer com o dado

['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
'__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__',
'__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
'__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center',
'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii',
'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join',
'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex',
'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title',
'translate', 'upper', 'zfill']

Vamos imagina que quero usar a função lower()

('UdayTC').lower()

Mas eu não sei o que ela faz, aí entra o help

help('UdayTC'.lower)

Veja que ele abriu a documentação
"""
from builtins import print

functions = []

def add(x, y):
    return x + y


def addToList(element):
    if element != "" and element != " ":
        if element not in functions:
            functions.append(element);
        else:
            print('Esta função já existe no array')
    else:
        print('O elemento não pode ser null')
    print(functions)


def validarNumeroElementos(a):
    if len(a) <= 1:
        print('Tem que se')
        return

def add(a):
    x = 0
    validarNumeroElementos(a)
    for i in a:
        x + i
    return x

def sub(a):
    x = 0
    for i in a:
        x - i
    return x

def mul(a):
    x = 1
    for i in a:
        x * i
    return x

def div(a):
    x = 1
    for i in a:
        if i == 0:
            print('Escolha nuúmeros que sejam diferentes de 0')
        if i != 0:
            x / i
    return x


functions = {}

def addToDictionary(functionValue):
    if functionValue != "" and functionValue != " ":
        if functionValue not in functions:
            functions[str(functionValue)] = functionValue
        else:
            print('Esta função já existe no array')
    else:
        print('O elemento não pode ser null')


def hasElements(a):
    if len(a) <= 1:
        print('Tem que ter no minimo 2 números')
        return False
    return True

def add(a):
    x = 0
    if hasElements(a) == True:
        for i in a:
            x += i
        return x
    else:
        return None

def sub(a):
    x = 0
    if hasElements(a) == True:
        for i in a:
            x -= i
        return x
    else:
        return

def mul(a):
    x = 1
    if hasElements(a) == True:
        for i in a:
            x *= i
        return x
    else:
        return

def div(a):
    if len(a) == 2:
        return a[0] / a[1]
    else:
        print("Apenas pode dividir dois números.")

addToDictionary(sub)
addToDictionary(add)
addToDictionary(div)
addToDictionary(mul)

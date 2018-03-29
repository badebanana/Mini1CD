functions = {}

def addToDictionary(fuctionKey, functionValue):
    if fuctionKey != "" and fuctionKey != " ":
        if functionValue != "" and functionValue != " ":
            if fuctionKey not in functions and functionValue not in functions:
                functions[fuctionKey] = functionValue
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
        return 'A operação não foi bem executada tente de novo!'

def sub(a):
    x = 0
    if hasElements(a) == True:
        for i in a:
            x -= i
        return x
    else:
        return 'A operação não foi bem executada tente de novo!!'

def mul(a):
    x = 1
    if hasElements(a) == True:
        for i in a:
            x *= i
        return x
    else:
        return 'A operação não foi bem executada tente de novo!!!'

def div(a):
    if len(a) == 2:
        return a[0] / a[1]
    else:
        return 'Apenas pode dividir dois números.'

addToDictionary('sub',sub)
addToDictionary('add',add)
addToDictionary('div',div)
addToDictionary('mul',mul)
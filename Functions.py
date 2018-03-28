functions = []

#ALTERAR METODO PARA DICIONARIO EM VEZZ DE LISTA

def addToDictionary(fuctionKey, functionValue):
    if fuctionKey != "" and fuctionKey != " ":
        if functionValue != "" and functionValue != " ":
            if fuctionKey not in functions and functionValue not in functions:
                functions[fuctionKey] = functionValue
            else:
                print('Esta função já existe no array')
    else:
        print('O elemento não pode ser null')
    print('Funcções existentes: ',functions)


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

a = [1,2,3]

print("Método sub da lista [", a ,"] dá: ", sub(a))

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


functions = {
    'add': add,
    'sub': sub,
}

addToDictionary('div', div)
addToDictionary('mul', mul)

print('Funções existentes: ', functions)
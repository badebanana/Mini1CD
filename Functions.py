
#ALTERAR METODO PARA DICIONARIO EM VEZZ DE LISTA
def addToList(element):
    if element != "" and element != " ":
        if element not in functions:
            functions.append(element);
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


functions = {
    'add': add,
    'sub': sub
}
def mul(a):
    x = 1
    if hasElements(a) == True:
        for i in a:
            x *= i
        return x
    else:
        return


"""
def div(a):
    x = 1
    for i in a:
        if i == 0:
            print('Escolha nuúmeros que sejam diferentes de 0')
        if i != 0:
            x / i
    return x
"""

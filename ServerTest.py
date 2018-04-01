import math
functions = {}

#Função que nos permite adicionar novas funções ao dicionário
def addToDictionary(fuctionKey, functionValue):
    if fuctionKey != "" and fuctionKey != " ":
        if functionValue != "" and functionValue != " ":
            if fuctionKey not in functions and functionValue not in functions:
                functions[fuctionKey] = functionValue
            else:
                print('Esta função já existe no array')
    else:
        print('O elemento não pode ser null')

#Função que nos permite saber se existem mais que 1 elemento na lista. Retornando True caso haja e False caso não haja
def hasElements(a):
    if len(a) <= 1:
        print('Tem que ter no minimo 2 números')
        return False
    return True

#Função que nos permite adicionar os elementos que estão dentro de uma lista
def add(a):
    x = 0
    if hasElements(a) == True:
        for i in a:
            x += i
        return x
    else:
        return 'A operação não foi bem executada tente de novo!'

#Função que nos permite subtrair os elementos que estão dentro de uma lista
def sub(a):
    x = 0
    aux = a[0]
    if hasElements(a) == True:
        for i in a[1:]:
            x = aux - i
            aux = x
        return x
    else:
        return 'A operação não foi bem executada tente de novo!!'

#Função que nos permite multiplicar os elementos que estão dentro de uma lista
def mul(a):
    x = 1
    if hasElements(a) == True:
        for i in a:
            x *= i
        return x
    else:
        return 'A operação não foi bem executada tente de novo!!!'

#Função que nos permite dividir os elementos que estão dentro de uma lista
def div(a):
    if len(a) == 2:
        return a[0] / a[1]
    else:
        return 'Apenas pode dividir dois números.'

#Função que nos permite usar a folmula resolvente com os 3 elementos desta lista
def resolv(a):
    if len(a) == 3:
        x = a[0]
        b = a[1]
        c = a[2]
        root = (b**2) - (4 * x * c)
        if x == 0:
            return 'O primeiro valor não pode ser igual a zero!'
        if root < 0:
            return 'Não é possível calcular raizes negativas!'
    result = []
    result.append((-b + math.sqrt(root)) / (2 * x))
    result.append((-b - math.sqrt(root)) / (2 * x))
    result.sort()
    return result

#Função que nos permite usar a potência com os elementos que estão dentro de uma lista
def pow(a):
    if hasElements(a) == True:
        x = 1
        aux = 0
        for i in a[1:]:
            x = x * i
            aux = x
        return a[0] ** aux
    else:
        return 'Tem que contenter no minímo dois números1'


addToDictionary('sub',sub)
addToDictionary('add',add)
addToDictionary('div',div)
addToDictionary('mul',mul)
addToDictionary('resolv', resolv)
addToDictionary('pow', pow)


#Função que nos permite escolher uma função do dicionário saindo quando o utilizador escreve a palavra exit
def calcula(dicionario):
    val = []
    for k,v in functions.items():
        if dicionario['method'].lower() == k:
            for i,j in dicionario['params'].items():
                val.append(int(j))
            return (v(val))
        elif dicionario['method'].lower() == 'exit':
            return 'Até à próxima'

def fileJson(msg):
    file_json = \
        {
            "id": 0,
            "jsonrpc": "2.0",
            "result": msg,
        }
    return file_json


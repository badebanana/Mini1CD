from ServerTest import*

def msgUser():
    print('Para sair escreva o seguinte:  exit                                   ')
    print('Escreva a função no seguinte formato:    nomeFunção,valor1,valor2,...')
    val=[]
    for k,v in functions.items():
        val.append(k)
    print('Funções Existente',val)
    msg = input("> ")
    array = msg.split(',')
    return array

def fileJson(msg):
    file_json = \
        {
        "id": 0,
        "method": msg[0],
        "jsonrpc": "2.0",
        }
    del msg[0]
    dParams = { }
    for i in range(len(msg)):
        dParams[i] = msg[i]
        i += 1
    file_json['params'] = dParams
    return file_json

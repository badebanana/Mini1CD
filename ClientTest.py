def msgUser():
    print('Escreva a função no seguinte formato:    nomeFunção,valor1,valor2,...')
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


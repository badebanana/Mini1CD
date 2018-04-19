from Functions import*

#Função que nos permite escolher uma função do dicionário saindo quando o utilizador escreve a palavra exit
def calcula(dicionario):
    val = []
    for k,v in functions.items():
        if dicionario['method'].lower() == k:
            for i,j in dicionario['params'].items():
                if j == '':
                    break
                val.append(int(j))
            return v(val)
        elif dicionario['method'].lower() == 'exit':
            return 'Até à próxima'
        else:
            return 'Escreva a função no seguinte formato: nomeFunção,valor1,valor2,...'

#Função que converte a mensagem recebida em ficheiro RPC-Json
def fileJson(msg):
    file_json = \
        {
            "id": 0,
            "jsonrpc": "2.0",
            "result": msg,
        }
    return file_json
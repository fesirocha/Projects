import os
from lib.interface import *

mensagens = []
nome = str(input('Nome: '))

while True:

    #Limpando o Terminal
    os.system('cls')

    if len(mensagens) > 0:
        cabeçalho('CHAT')
        for m in mensagens:
            print(m['nome'], ' - ', m['texto'])
    traços()

    #Obtendo mensagens
    texto = str(input('Mensagem: '))
    if texto in 'FIMfim':
        break

    #Adicionando mensagem no chat
    mensagens.append({'nome': nome, 'texto': texto})

    



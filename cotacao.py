import requests

from tkinter import *

def obter_cotacao():
    requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    print(requisicao)
    requisicao_dic = requisicao.json()

    dolar_name = requisicao_dic['USDBRL']['name']
    dolar = requisicao_dic['USDBRL']['bid']
    
    euro_name = requisicao_dic['EURBRL']['name']
    euro = requisicao_dic['EURBRL']['bid']

    btc_name = requisicao_dic['BTCBRL']['name']
    btc = requisicao_dic['BTCBRL']['bid']

    resultado = f'''
    {dolar_name}: {dolar} 
    {euro_name} {euro}
    {btc_name} {btc}'''

    #print(resultado)
    texto_resultado["text"] = resultado


janela = Tk()
janela.title('Cotação atual das moedas')
janela.geometry('310x150')

orientacao = Label(janela, text='Clique no botao para exibir a cotação atualizada')
orientacao.grid(column=0, row=0, padx=20, pady=10)

botao = Button(janela, text='Buscar cotacoes!', command = obter_cotacao)
botao.grid(column=0, row=1)

texto_resultado = Label(janela, text = "")
texto_resultado.grid(column=0, row=2)


janela.mainloop()
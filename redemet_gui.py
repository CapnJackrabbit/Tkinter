import requests, datetime
from tkinter import *
from textwrap import *

chave = 'api_key=2JEa2iWav9FvjNdFfvoQVUUGs3ZZP7CHCs33FZ0a'

def obter():
    global icao, inicio, fim
    icao_get = icao.get()
    requisicao = requests.get('https://api-redemet.decea.mil.br/mensagens/metar/{}?api_key=2JEa2iWav9FvjNdFfvoQVUUGs3ZZP7CHCs33FZ0a&{}&{}'.format(icao_get,inicio,fim))
    print(requisicao)

    requisicao_dic = requisicao.json()
    acc=""
    for quant in range (5):
        try:
            metar = requisicao_dic['data']['data'][quant]['mens']

            resultado = f'''
            >> {metar}'''
            acc += resultado+'\n'

            metar_obtido['text'] = acc
        except IndexError:
            break

        finally:
            obter_taf()    


def obter_taf():
    global icao, inicio, fim
    icao_get = icao.get()
    requisicao = requests.get('https://api-redemet.decea.mil.br/mensagens/taf/{}?api_key=2JEa2iWav9FvjNdFfvoQVUUGs3ZZP7CHCs33FZ0a&{}&{}'.format(icao_get,inicio,fim))
    print(requisicao)

    requisicao_dic = requisicao.json()
    acc=""
    for quant in range (5):
        try:
            taf = requisicao_dic['data']['data'][quant]['mens']

            resultado = f'''
            >> {taf}'''
            acc += resultado+'\n'

            taf_obtido['text'] = acc
        except IndexError:
            break

window = Tk()
window.title('Consulta METAR')
window.geometry('1000x450')

orientacao1 = Label(window, text='Informe o código ICAO: ')
orientacao1.grid(column=0, row=0, padx=10,pady=10)
icao = Entry(window, width=25)
icao.grid(column=1, row=0)

data = datetime.datetime.now()
ano = data.year
mes = data.month
dia = data.day
hora = data.hour
minuto = data.minute
inicio = '{}{}{}{}'.format(ano,mes,dia,hora)
fim = inicio
orientacao4 = Label(window, text='Data atual: {}/{}/{}  {}:{}'.format(dia,mes,ano,hora,minuto))
orientacao4.place(x=9,y=45)

botao = Button(window, text='Consultar', command=obter)
botao.place(x=185,y=42)

metar_obtido = Label(window, justify='left', text="")
metar_obtido.place(x=330,y=0)

taf_obtido = Label(window, wraplength=900, justify='left', text="")
taf_obtido.place(x=20, y=180)

window.mainloop()
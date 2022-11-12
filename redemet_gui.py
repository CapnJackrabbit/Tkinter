import requests, datetime
from tkinter import *

chave = 'api_key=2JEa2iWav9FvjNdFfvoQVUUGs3ZZP7CHCs33FZ0a'

def obter():
    global icao, inicio, fim
    icao_get = icao.get()
    # inicio_get = inicio.get()
    # fim_get = fim.get()
    requisicao = requests.get('https://api-redemet.decea.mil.br/mensagens/metar/{}?api_key=2JEa2iWav9FvjNdFfvoQVUUGs3ZZP7CHCs33FZ0a&{}&{}'.format(icao_get,inicio,fim))
    print(requisicao)

    requisicao_dic = requisicao.json()
    acc=""
    for quant in range (5):
        try:
            metar = requisicao_dic['data']['data'][quant]['mens']

            resultado = f'''
            >> {metar}'''
            acc += resultado

            metar_obtido['text'] = acc
        except IndexError:
            break    

window = Tk()
window.title('Consulta METAR')
window.geometry('640x250')

orientacao1 = Label(window, text='Informe o código ICAO: ')
orientacao1.grid(column=0, row=0, padx=100,pady=5)
icao = Entry(window)
icao.grid(column=1, row=0)

# orientacao2 = Label(window, text='Informe a data de início: (YYYYMMDDHH: ')
# orientacao2.grid(column=0, row=1, padx=100, pady=5)
# inicio = Entry(window)
# inicio.grid(column=1, row=1)

# orientacao3 = Label(window, text='Informe a data de fim: (YYYYMMDDHH: ')
# orientacao3.grid(column=0, row=2, padx=100, pady=5)
# fim = Entry(window)
# fim.grid(column=1, row=2)

data = datetime.datetime.now()
ano = data.year
mes = data.month
dia = data.day
hora = data.hour
minuto = data.minute
inicio = '{}{}{}{}'.format(ano,mes,dia,hora)
fim = inicio
orientacao4 = Label(window, text='Data atual: {}/{}/{}  {}:{}'.format(dia,mes,ano,hora,minuto))
orientacao4.place(x=100,y=45)

botao = Button(window, text='Consultar', command=obter)
botao.place(x=300,y=100)

metar_obtido = Label(window, text='')
metar_obtido.place(x=90,y=150)

window.mainloop()
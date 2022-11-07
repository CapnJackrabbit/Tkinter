import requests

from tkinter import *

def obter_cep():
    global armazenar_cep
    armazenar_cep = cep.get()
    requisicao = requests.get('https://cep.awesomeapi.com.br/json/{}'.format(armazenar_cep))
    print(requisicao)
    if requisicao.status_code == 400 or requisicao.status_code == 404:
        texto_resultado['text'] = 'CEP informado é inválido!'
    else:
        requisicao_dic = requisicao.json()

        endereco = requisicao_dic['address']
        cidade = requisicao_dic['city']
        estado = requisicao_dic['state']
        bairro = requisicao_dic['district']

        resultado = f'''
        Rua: {endereco} 
        Cidade: {cidade}
        Bairro: {bairro}
        Estado: {estado}'''

        texto_resultado['text'] = resultado
        print(armazenar_cep)


janela = Tk()
janela.title('Buscar endereço por CEP')
janela.geometry('310x200')

orientacao = Label(janela, text='Digite o CEP no campo abaixo')
orientacao.grid(column=0, row=0, padx=70, pady=10)

cep = Entry(janela, )
cep.grid(column=0, row=1)

botao = Button(janela, text='Buscar CEP!', command = obter_cep)
#botao.grid(column=0, row=2)
botao.place(x=120,y=70)

texto_resultado = Label(janela, text = "")
#texto_resultado.grid(column=0, row=3)
texto_resultado.place(x=70,y=100)

janela.mainloop()
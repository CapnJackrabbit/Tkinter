import requests

def obter_cep(cep):
    requisicao = requests.get('https://cep.awesomeapi.com.br/json/{}'.format(cep))
    print(requisicao)

    requisicao_dic = requisicao.json()

    endereco = requisicao_dic['address']
    cidade = requisicao_dic['city']
    municipio = requisicao_dic['district']
    estado = requisicao_dic['state']
    ddd = requisicao_dic['ddd']

    resultado = f'''
    Rua: {endereco} 
    Cidade: {cidade}
    Município: {municipio}
    Estado: {estado}
    DDD: {ddd}'''

    print(resultado)

cep = input('Informe o CEP para consulta: ')
obter_cep(cep)
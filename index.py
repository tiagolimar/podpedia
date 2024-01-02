from core import *
from flask import Flask, request
from flask_cors import CORS


# Cria uma instância do aplicativo Flask
app = Flask(__name__)
CORS(app)

resposta_dividida = []
index = 0
max_index = 0


@app.route('/')
def pesquisar():
    global resposta_dividida, index, max_index
    # Obtém o valor do parâmetro 'termo'
    termo = request.args.get('termo', 'Python')
    resposta = pesquisa_wikipedia(termo)
    if resposta:
        resposta_dividida = dividir_texto(resposta)
        max_index = len(resposta_dividida)
        resultado = {"max_index": max_index, "index": index}
        return resultado
    else:
        return "error"


@app.route('/audio')
def obter_audio():
    global resposta_dividida, index, max_index
    print(max_index)
    index = int(request.args.get('index', 0))
    print(index)
    print(len(resposta_dividida))
    trecho = resposta_dividida[index]
    resposta = texto_para_audio(trecho)

    return {"status":"ok"}


# Executa o aplicativo se este script for o ponto de entrada
web()
app.run(debug=True)

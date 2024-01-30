import os
import wikipediaapi
import nltk

from gtts import gTTS


def pesquisa_wikipedia(texto_pesquisa):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    wiki_wiki = wikipediaapi.Wikipedia(user_agent=user_agent, language='pt')
    page_py = wiki_wiki.page(texto_pesquisa)

    if not page_py.exists():
        return None
    texto = page_py.text[:]  # Limita o texto para não ser muito longo

    return texto


def texto_para_audio(texto, nome_arquivo='./audios/output.mp3'):
    tts = gTTS(texto, lang='pt')
    tts.save(nome_arquivo)
    return True

def dividir_texto(texto):
    # Baixa os dados necessários para a tokenização, caso ainda não estejam presentes
    nltk.download('punkt')

    # Usa a função sent_tokenize para dividir o texto em frases
    trechos = nltk.sent_tokenize(texto)

    return trechos

def web():
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    path = diretorio_atual.replace(" ","%").replace("\\","/").replace("//","/")
    os.system(f'start file:///{path}/web/index.html')


def main():
    pesquisa = input("Digite o que deseja pesquisar na Wikipedia: ")

    resultado_pesquisa = pesquisa_wikipedia(pesquisa)
    resultado_em_trechos = dividir_texto(resultado_pesquisa)
    n_trechos = len(resultado_em_trechos)

    if resultado_pesquisa != "Desculpe, a pesquisa não retornou resultados.":
        for i in range(n_trechos):
            print(f'Executando parte {i+1} de {n_trechos}.')
            print(f'Total de {len(resultado_pesquisa)} caracteres retornados.')

            trecho_resultado = resultado_em_trechos[i]

            texto_para_audio(trecho_resultado)

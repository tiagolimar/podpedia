# Podpedia: Um "podcast" baseado em pesquisas na Wikipedia com Áudio

Este código permite que você pesquise na Wikipedia e ouça os resultados em áudio. Ele usa a biblioteca `wikipediaapi` para pesquisar na Wikipedia, a biblioteca `gTTS` para converter texto em áudio e a biblioteca `pygame` para reproduzir o áudio.

## Requisitos de Sistema

- Python 3.x
- pip (Gerenciador de pacotes Python)

## Instalação

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/tiagolimar/podpedia.git
    ```

2. **Navegue até o diretório do projeto:**

    ```bash
    cd podpedia
    ```

3. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. **Execute o script Python:**

    ```bash
    python nome_do_script.py
    ```

2. **Você será solicitado a inserir um termo de pesquisa na Wikipedia.**

3. **O programa dividirá o texto da Wikipedia em trechos e reproduzirá o áudio correspondente para cada trecho.**
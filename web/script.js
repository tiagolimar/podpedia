let index = 0;
let max_index = 0;

function enviar() {
    texto = document.querySelector("p");
    texto.classList.add("loading");
    texto.innerText = "Carregando...";

    termo = document.querySelector("input").value;
    // Cria uma requisição usando a API fetch
    fetch(`http://127.0.0.1:5000/?termo=${termo}`)
        .then((response) => response.json())
        .then((data) => {
            index = data.index;
            max_index = data.max_index;
            obter_audio();
            // Atualiza o conteúdo do elemento h1
            texto.classList.remove("loading");
            texto.innerText = data;
        })
        .catch((error) => console.error("Erro na requisição:", error));
}

function obter_audio() {
    atualizarProgressBar()
    fetch(`http://127.0.0.1:5000/audio?index=${index}`)
        .then((response) => response.json())
        .then((data) => {
            if (data) {
                const meuAudio = document.querySelector("audio");
                meuAudio.removeAttribute('src');
                meuAudio.setAttribute('src', '../audios/output.mp3');
                meuAudio.load();
                console.log('atualizado!');
            }
        });
}

function add_index() {
    if (index < max_index) {
        index++;
        obter_audio();
    }
}

function atualizarProgressBar() {
    // Calcula a porcentagem concluída
    var porcentagemConcluida = (index / max_index) * 100;

    // Atualiza a barra de progresso com a porcentagem concluída
    var progressBar = document.getElementById("progressBar");
    progressBar.style.width = porcentagemConcluida + "%";
    progressBar.setAttribute("aria-valuenow", porcentagemConcluida);
    progressBar.innerText = porcentagemConcluida.toFixed(2) + "% Concluído";
}

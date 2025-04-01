# YT-Insight

Essa é uma ferramenta que, a partir de uma URL de um vídeo no YouTube, extrai o conteúdo através do áudio e gera resumos utilizando Inteligência Artificial. Seu objetivo é contribuir para o aprendizado utilizando a tecnologia como aliada. 

## Getting Started



### Prerequisites

O que você precisa para instalar o software e como instalá-lo:

```
Python 3.5 or superior

```

Instale o codec utilizado na transcrição de áudio. Você pode instalar no seu computador através do site da ffmpeg (https://www.ffmpeg.org/) ou através do gerenciador de pacotes Chocolatey (https://chocolatey.org/install), pelo comando abaixo:

```
choco install ffmpeg

```
Baixe e instale o Ollama, que é uma ferramenta de código aberto que executa large language models (LLMs) diretamente no seu computador: https://ollama.com/

Após intalar o Ollama, execute o comando abaixo no prompt de comando:

```
ollama run deepseek-r1:7b

```

Após a instalação, vc estará apto a rodar LLMs na sua máquina. Para fins de demonstração, foi escolhido o modelo DeepSeek-R1

### Installing

Crie um ambiente virtual 

```
python3 -m venv myvenv
```

Ative o ambiente virtual 

```
source myvenv/bin/activate (linux)

ou

myvenv/Scripts/activate (windows)
```

Instale as dependências do projeto descritas no requirements.txt
```
pip install -r requirements
```

### Running

Agora que já preparamos o ambiente, vamos subir nossa aplicação Flask.

Execute a aplicação

```
python main.py
```


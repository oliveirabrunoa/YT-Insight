# YT-Insight

Essa é uma ferramenta que, a partir de uma URL de um vídeo no YouTube, baixa e extrai o áudio, trascreve e gera resumos utilizando Inteligência Artificial. Seu objetivo é contribuir para o aprendizado utilizando a tecnologia como aliada. 

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


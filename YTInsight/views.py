from flask import Blueprint, render_template, request, redirect, url_for,jsonify
from pytubefix import YouTube
from pytubefix.cli import on_progress
import whisper
from dotenv import load_dotenv
import os
from google import genai
from google.genai import types
import re

ytinsight = Blueprint('ytinsight', __name__)
load_dotenv()
chave_google = os.getenv('GOOGLE_API_KEY')
client = genai.Client(api_key=chave_google)

@ytinsight.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':

        videoLink = request.form['videoLink']

        if not videoLink:
            return jsonify({"resumo": "Link inválido"}), 400
    
        audio = audio_download(videoLink)
        if audio:
            transcricao = audio_transcricao(audio)
            resumo = chat_gemini(transcricao["text"])    
            return render_template('index.html',resumo=resumo)
        else:
            return render_template('index.html', resumo=resumo, error='Erro ao fazer download do vídeo')        
  
    return render_template('index.html')

def audio_download(videoLink):
    path_to_save = "audios"
    try:
        yt = YouTube(videoLink, on_progress_callback=on_progress)
        print(f'fazendo download do vídeo {yt.title}')
        video = yt.streams.get_audio_only()
        # Gera nome seguro para arquivo
        safe_title = re.sub(r'[\\/*?:"<>|]', "", yt.title)
        filename = f"{safe_title}"
        video.download(output_path=path_to_save, filename=filename)
        return filename
    except Exception as e: 
        print(f'Erro ao fazer download do vídeo: {e}')
        return False  
    
def audio_transcricao(audio_title):
    try:
        modelo = whisper.load_model("base")
        print(f'fazendo transcrição do áudio {audio_title}')
        transcricao = modelo.transcribe(f"audios\\{audio_title}.m4a")
        return transcricao
    except Exception as e:
        print(f'Erro ao fazer transcrição do áudio: {e}')

def chat_gemini(transcription):
    response = client.models.generate_content(
    model="gemini-2.0-flash",
    config=types.GenerateContentConfig(
        system_instruction="Você é um especialista em criar resumos a partir de um texto fornecido. Para isso, siga a estrutura a seguir: \n"
        "1. Título: Nome do vídeo ou um título representativo \n"
        "2. Resumo Geral (20 ou 30 linhas): O que foi falado? Qual é a ideia principal? \n"
        "3. Pontos-Chave (bullet points): Principais ideias ou argumentos; Dados, exemplos ou frases de destaque \n"
        "4. Conclusão: Fechamento da fala ou aprendizado principal (20 linhas)",
    ),
    contents=transcription,
    )

    return response.text

"""if __name__ == '__main__':
    chat_gemini("O que é Python?")"""
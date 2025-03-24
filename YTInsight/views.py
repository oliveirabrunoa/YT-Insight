from flask import Blueprint, render_template, request, redirect, url_for
#from pytube import YouTube
from pytubefix import YouTube
from pytubefix.cli import on_progress
import whisper

ytinsight = Blueprint('ytinsight', __name__)

@ytinsight.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        videoLink = request.form['videoLink']
        audio = audio_download(videoLink)
        if audio:
            audio_transcricao(audio)
            return render_template('index.html', error='Audio baixado com sucesso')
        else:
            return render_template('index.html', error='Erro ao fazer download do vídeo')        
  
    return render_template('index.html')

def audio_download(videoLink):
    path_to_save = "audios"
    try:
        yt = YouTube(videoLink, on_progress_callback=on_progress)
        print(f'fazendo download do vídeo {yt.title}')
        video = yt.streams.get_audio_only()
        video.download(output_path=path_to_save) 
        return video.title
    except Exception as e: 
        print(f'Erro ao fazer download do vídeo: {e}')
        return False    
    
def audio_transcricao(audio_title):
    try:
        modelo = whisper.load_model("base")
        print(f'fazendo transcrição do áudio {audio_title}')
        transcrição = modelo.transcribe(f"audios/{audio_title}.m4a")
        return transcrição["text"]
    except Exception as e:
        print(f'Erro ao fazer transcrição do áudio: {e}')
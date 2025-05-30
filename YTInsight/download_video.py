from flask import Blueprint, render_template, request, redirect, url_for
from pytubefix import YouTube
from pytubefix.cli import on_progress
from dotenv import load_dotenv
import os

ytinsight = Blueprint('ytinsight', __name__)
load_dotenv()
chave_api = os.getenv('OPENAI_API_KEY')

def video_download(videoLink):
    path_to_save = "audios"
    try:
        yt = YouTube(videoLink, on_progress_callback=on_progress)
        print(f'fazendo download do vídeo {yt.title}')
        video = yt.streams.get_highest_resolution()
        video.download(output_path=path_to_save) 
        return video.title
    except Exception as e: 
        print(f'Erro ao fazer download do vídeo: {e}')
        return False    

if __name__ == '__main__':
    #chat_openai()
    video_download("https://www.youtube.com/watch?v=4tGFgAZihv0")
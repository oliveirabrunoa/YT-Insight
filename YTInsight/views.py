from flask import Blueprint, render_template, request, redirect, url_for
from .models import Video

ytinsight = Blueprint('ytinsight', __name__)

@ytinsight.route('/', methods=['GET', 'POST'])
def index():
    #video = Video()
    return render_template('index.html')
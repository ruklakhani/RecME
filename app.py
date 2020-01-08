from flask import Flask, render_template, request, redirect, url_for
from random import randint 
import os
import requests

app = Flask(__name__)

@app.route('/')
def music_index():
    return render_template('index.html')

@app.route('/playlist')
def playlist_generator():
    return render_template('playlist_generator.html')

@app.route('/emo')
def emo_form():    
    return render_template('emo_form.html')

@app.route('/emo_results')
def emo_results():
    emo_results = request.args.getlist('artist')
    # if emo_results == "true"
    print(emo_results)
    return render_template('emo_results.html', emo_results=emo_results)

@app.route('/login')
def login_page():
    return render_template('login_page.html')
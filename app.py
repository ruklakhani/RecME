from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def music_index():
    return render_template('index.html')

@app.route('/playlist')
def playlist_generator():
    return render_template('playlist_generator.html')

@app.route('/quiz')
def quiz_page():
    return render_template('quiz_page.html')

@app.route('/login')
def login_page():
    return render_template('login_page.html')
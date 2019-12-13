from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def music_index():
    return render_template('index.html')
from flask import Flask, render_template, request, redirect, url_for
from random import randint 
from pymongo import MongoClient
from bson import ObjectId
import os
import requests

app = Flask(__name__)

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/MusicForm')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()

forms = db.form

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

@app.route('/ruk')
def ruk_form():    
    return render_template('ruk_form.html')

@app.route('/ruk_results')
def ruk_results():
    ruk_results = request.args.getlist('artist')
    print(ruk_results)
    return render_template('ruk_results.html', ruk_results=ruk_results)

@app.route('/form/new')
def new_form():    
    return render_template('new_form.html', form={})

@app.route('/form', methods=['POST'])
def form_submit():
    artists = request.form.get('artists')
    form = {
        'form_name': request.form.get('form_name'),
        'artists': artists.split("\n")
    }
    
    form_id = forms.insert_one(form).inserted_id
    return redirect(url_for('form_show', form_id=form_id))

@app.route('/form/<form_id>')
def form_show(form_id):
    form = forms.find_one({'_id': ObjectId(form_id)})
    return render_template('show_form.html', form=form)

@app.route('/login')
def login_page():
    return render_template('login_page.html')
from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='../views', static_folder='../static')

@app.route('/')
def home():
    return render_template('home.html')

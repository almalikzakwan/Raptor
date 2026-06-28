from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='template')

cwd = os.getcwd()

@app.route('/')
def home():
    return render_template(f'{cwd}/views/home.html')

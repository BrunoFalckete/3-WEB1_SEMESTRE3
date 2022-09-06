from flask import Flask,render_template

meu_app = Flask(__name__)

@meu_app.route ('/')

def to_index():

    return render_template('index.html')
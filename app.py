from flask import Flask, url_for, render_template
from models.py import buscar_livro, resenhas_do_livro, buscar_livros

app = Flask(__name__)

@app.route("/", methods =["GET"])
def index():
    return render_template('index.html')

@app.route("/livro/<int:livro_id>", methods =["GET"])
def renderizar_livro():
    return render_template('livro.html')

@app.route("/login",methods =["GET", "POST"])
def login():
    return render_template('login.html')

@app.route("/logout")
def logout():
    return render_template('index.html')
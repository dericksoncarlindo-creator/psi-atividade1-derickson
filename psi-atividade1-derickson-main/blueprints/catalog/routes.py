from flask import render_template, abort, request
from . import catalog_bp
from models import buscar_livros, buscar_livro 

@catalog_bp.route("/")
def index():
    query = request.args.get("q", "").strip()
    livros_filtrados = buscar_livros(query)
    return render_template("catalog/index.html", livros=livros_filtrados, query=query)

@catalog_bp.route("/livro/<int:livro_id>")
def ver_livro(livro_id):
    livro = buscar_livro(livro_id)
    if not livro:
        abort(404, description="Livro não encontrado.")
    return render_template("catalog/livro.html", livro=livro, livro_id=livro_id)

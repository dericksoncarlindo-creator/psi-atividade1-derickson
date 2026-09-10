from flask import request, redirect, url_for, session
from . import reviews_bp
from models import resenhas, proximo_id_resenha 

@reviews_bp.route("/resenhar", methods=["POST"])
def resenhar(livro_id):
    if "usuario" not in session:
        return redirect(url_for("auth.login"))
    
    conteudo = request.form.get("conteudo")
    nota = request.form.get("nota")
    usuario_atual = session["usuario"]
    
    novo_id = proximo_id_resenha()
    nova_resenha = {
        "id": novo_id,
        "livro_id": livro_id,
        "usuario": usuario_atual,
        "conteudo": conteudo,
        "nota": int(nota) if nota else 5
    }
    resenhas.append(nova_resenha)
    
    return redirect(url_for("livros.detalhes", livro_id=livro_id))
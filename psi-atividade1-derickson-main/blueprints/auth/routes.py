from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required

from . import auth_bp

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        return redirect(url_for("catalog/templates/catalog.index"))
        
    return render_template("auth/login.html")

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Você saiu da sessão.", "info")
    
    return redirect(url_for("catalog/templates/catalog.index"))

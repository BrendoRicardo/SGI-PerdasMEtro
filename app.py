from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "chave_fallback_segura")

usuarios = {
    "Admin": {"senha": "Admin", "perfil": "ADM"},
    "Perfil1": {"senha": "Perfil1", "perfil": "NIVEL1"},
    "Perfil2": {"senha": "Perfil2", "perfil": "NIVEL2"},
    "Perfil3": {"senha": "Perfil3", "perfil": "NIVEL3"}
}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]

        if usuario in usuarios and usuarios[usuario]["senha"] == senha:
            session["usuario"] = usuario
            session["perfil"] = usuarios[usuario]["perfil"]
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", erro="Usuário ou senha inválidos")
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "usuario" not in session:
        return redirect(url_for("login"))

    perfil = session.get("perfil")

    link_powerbi = "https://app.powerbi.com/view?r=eyJrIjoiMzExOWJjY2QtZmM4NC00YzUxLWE2MjYtMTViMjNhODQ3MWEzIiwidCI6ImFiMjQwN2E1LTMxOWEtNGRmOS1hOGI4LTM1MjgwNTRjYzEzZSJ9"

    if perfil in ["ADM", "NIVEL1", "NIVEL2", "NIVEL3"]:
        url_powerbi = link_powerbi
    else:
        url_powerbi = None

    return render_template("dashboard.html", perfil=perfil, url_powerbi=url_powerbi)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/ping")
def ping():
    return "pong", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

from flask import Flask, render_template, request, session,redirect,url_for
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

notes = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)
    return render_template("index.html", notes=notes)

@app.route("/delete", methods=["POST"])
def delete():
    note = request.form.get("note")
    if note in notes:
        notes.remove(note)
    return redirect(url_for("index"))
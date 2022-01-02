from os import removedirs
from flask import Flask, redirect, url_for, render_template, session, flash
from flask import request
from datetime import timedelta  
#!python

app = Flask(__name__)
app.secret_key = "secret key"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/", methods = ["POST", "GET"])
def home():
    return render_template("home.html")

# New functions
@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/login/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user  = request.form['nm']
        session["user"] = user
        return redirect (url_for("user"))
    else:
        if "user" in session:
            return redirect (url_for("user"))
        else:
            return render_template("login.html")

@app.route("/logout/")
def logout():
    if "user" in session:
        user = session["user"]
        flash (f"You have been logged out, {user}", "info")
    session.pop("User", None)
    return redirect(url_for("login "))

@app.route("/user/")
def user():
    if "user" in session:
        user = session["user"]
        return render_template(
            "user.html",
            usr = user
        )
    else:
        return redirect(url_for("login"))


@app.route("/make-quiz/", methods=["POST", "GET"])
def make_quiz():
    if "user" in session:
        if request.method == "POST":
            quiz_name = request.form['qn']
            num_questions = request.form.get('num_q', type=int)
            return redirect(url_for('create_questions', qzn=quiz_name, num_q = num_questions))
        else:
            return render_template("make_quiz.html")
    else:
        return redirect(url_for("login"))

@app.route("/<qzn>/<num_q>/")
def create_questions(qzn, num_q: int):
    return render_template(
        "create_questions.html",
        qzn = qzn,
        num_q = num_q,
        usr = session["user"]
    )


@app.route("/take-quiz/")
def take_quiz():
    return render_template("take_quiz.html")
    

@app.route("/api/")
def get_data():
    return app.send_static_file("data.json")
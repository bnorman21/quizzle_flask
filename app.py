from flask import Flask
from datetime import datetime
from flask import render_template
from flask import render_template
import re
#!python
import mlbgame

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

# New functions
@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/games/<name>/<team>/<month>/<year>")
def hello_there(name = None, team = None, month = None, year = None):
    return render_template(
        "games.html",
        name=name,
        team=team,
        month=month,
        year=year,
        games = mlbgame.combine_games(mlbgame.games(int(year), int(month), home=team)),
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
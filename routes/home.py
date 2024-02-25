from flask import Blueprint, render_template

home = Blueprint("home", __name__)

@home.route("/")
def main():
    return render_template("index.html")
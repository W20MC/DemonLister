from flask import Blueprint, render_template

challenge = Blueprint("challenge", __name__, url_prefix = "/challenge")

@challenge.route("/")
def home():
    return render_template("challenge.html")
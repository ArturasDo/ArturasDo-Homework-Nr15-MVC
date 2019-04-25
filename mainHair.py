from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("HairSalon.html")


@app.route("/about")
def about():
    return render_template("Fakebook.html")


@app.route("/portfolio")
def portfolio():
    return render_template("GuesFunkcijos.py")


if __name__ == '__main__':
    app.run(debug=True)
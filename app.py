from flask_bootstrap import Bootstrap5
from flask import Flask, render_template

app = Flask(__name__)

bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)

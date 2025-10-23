from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")
    #return "こんにちは、Flaskの世界へ！"

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("sidebar.html")

@app.route("/second")
def second():
    return render_template("second.html")

@app.route("/third")
def third():
    return render_template("third.html")

if __name__ == "__main__":
    app.run(debug=True)

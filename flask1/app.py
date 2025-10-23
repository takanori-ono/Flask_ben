from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")
    #return "こんにちは、Flaskの世界へ！"

@app.route("/about")
def about():
    return render_template("sidebar.html")

if __name__ == "__main__":
    app.run(debug=True)

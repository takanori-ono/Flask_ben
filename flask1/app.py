from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

# SQLiteデータベースの設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<Id {self.id}><User {self.name}>'

with app.app_context():
    db.create_all()
    
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

@app.route("/formtest", methods=["GET", "POST"])
def formtest():
    if request.method == "POST":
        # name = request.form.get("name")
        # return f"こんにちは、{name}さん！フォームの送信が成功しました。"
        name = request.form.get("name")
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("result", name=name))
    else:
        return render_template("form.html")

@app.route("/result/<name>")
def result(name):
    return render_template("result.html", name=name)

@app.route("/users")
def users():
    all_users = User.query.all()
    return render_template("users.html", users=all_users)

@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/search_users")
def search_users():
    q = request.args.get("q", "")  # ?q=xxx
    if q:
        users = User.query.filter(User.name.like(f"%{q}%")).all()
    else:
        users = []
    results = [{"id": u.id, "name": u.name} for u in users]
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)

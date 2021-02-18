from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

#CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URL'] = "sqlite:///books.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, Primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
db.create_all()

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        #creating records
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"]
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)


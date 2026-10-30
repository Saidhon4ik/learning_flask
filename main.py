from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
        return render_template("about.html", hobby = "chess",city = "Berlin")

@app.route("/hello/<name>")
def hello(name):
        return f"hello {name}"

@app.route("/square/<int:n>")
def square(n):
        return f"Square: {n*n}"

@app.route("/books")
def books():
        books = ["Dune","Emma","Ulysses"]
        return render_template("books.html", books=books)

if __name__ == "__main__":
    app.run(debug=True)

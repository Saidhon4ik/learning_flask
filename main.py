from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
        return "Hello, Flask!"

@app.route("/about")
def about():
        return "I like chess"

@app.route("/hello/<name>")
def hello(name):
        return f"hello {name}"

@app.route("/square/<int:n>")
def square(n):
        return f"Square: {n*n}"

if __name__ == "__main__":
    app.run(debug=True)

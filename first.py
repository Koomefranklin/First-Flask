from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")
def home():
    return"""<h1>Heading with html """

@app.route("/<name>")
def user(name):
    a=5
    return f"""hello {name}"""

@app.route("/admin")
def admin():
    return redirect(url_for("user", name = "Admin"))

if __name__== "__main__":
    app.run(debug=True)
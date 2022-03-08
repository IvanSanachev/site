from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        print(request.form)
    return render_template("index.html")

@app.errorhandler(404)
def er(e):
    return render_template("error404.html")


@app.route('/game')
def game():
    return render_template("game.html")


if __name__ == "__main__":
    app.run(debug=True)
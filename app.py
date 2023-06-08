from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template("index.html")

@app.route("/movies", methods=['POST'])
def movies():
    return render_template("movies.html")
if __name__ == "__main__":
    app.run(debug=True)
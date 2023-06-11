from flask import Flask, render_template, url_for, request
app = Flask(__name__)
import psycopg2
from psycopg2 import Error

genres=['action', 'animation', 'comedy', 'crime', 'drama', 'fantasy', 'horror', 'sci-fi', 
        'thriller', 'western', 'adventure', 'romance', 'musical', 'mystery']

def getInfo(form_data):
    recommendations = form_data.get('recommendations')
    form_genres = []
    for x in genres:
        if form_data.get(x) == 'on':
             form_genres.append(x.capitalize())
    actors = form_data.get('actor').split('\r\n')
    director = form_data.get('director').split('\r\n')
    result = []
    result.append(recommendations)
    result.append(form_genres)
    result.append(actors)
    result.append(director)
    return result

@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template("index.html")

@app.route("/movies", methods=['POST'])
def movies():
    if request.method == "POST":
        data = getInfo(request.form)
    return render_template("movies.html")
if __name__ == "__main__":
    app.run(debug=True)
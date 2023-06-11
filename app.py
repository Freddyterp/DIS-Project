from flask import Flask, render_template, url_for, request
app = Flask(__name__)
import psycopg2
from psycopg2 import Error

connection = psycopg2.connect(user='postgres',
                              password='changepassword',
                              host="localhost",
                              port="5432",
                              database='postgres')
cursor = connection.cursor()

genres=['action', 'animation', 'comedy', 'crime', 'drama', 'fantasy', 'horror', 'sci-fi', 
        'thriller', 'western', 'adventure', 'romance', 'musical', 'mystery']

def getInfo(form_data):
    recommendations = form_data.get('recommendations')
    form_genre = form_data.get('genre[]')
    actors = form_data.get('actor')
    directors = form_data.get('director')
    result = []
    result.append(recommendations)
    result.append(form_genre)
    result.append(actors)
    result.append(directors)
    return result

def SQLQuery(data):
    query = """ SELECT DISTINCT movie_name, year, rating, services_name, services_price
                 FROM movies
                 JOIN streaming ON movies.movie_id = streaming.movie_id
                 JOIN streamingservices AS ss ON streaming.services_id = ss.services_id
                 """
    if not data[1] == None:
        query += """JOIN moviegenre ON movies.movie_id = moviegenre.movie_id
                     JOIN genre ON moviegenre.genre_id = genre.genre_id
                     """
    if not data[2] == '':
        query += """JOIN acted_in ON movies.movie_id = acted_in.movie_id
                     JOIN actors ON acted_in.actor_id = actors.actor_id
                     """
    if not data[3] == '':
        query += """JOIN directed ON movies.movie_id = directed.movie_id
                     JOIN directors ON directed.director_id = directors.director_id
                     """
    if not data[1] == None:
        query += f"WHERE genre.genre = '{data[1]}' "
    if not data[2] == '':
        subquery = ''
        if not data[1] == None:
            subquery += f"AND actors.actor_name = '{data[2]}' "
        else:
            subquery += f"WHERE actors.actor_name = '{data[2]}' "
        query += subquery
    if not data[3] == '':
        subquery = ''
        if not data[1] == None or not data[2] == '':
            subquery += f"AND directors.director_name = '{data[3]}'"
        else:
            subquery += f"WHERE directors.director_name = '{data[3]}'"
        query += subquery
    return query

@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template("index.html")

@app.route("/movies", methods=['POST'])
def movies():
    data = getInfo(request.form)
    print(data)
    cursor.execute(SQLQuery(data))
    movies = cursor.fetchall()
    print(movies)
    return render_template("movies.html", movies=movies)
if __name__ == "__main__":
    app.run(debug=True)
DROP SCHEMA IF EXISTS moviegenerator CASCADE;
CREATE SCHEMA moviegenerator
CREATE TABLE Movies(
	movie_id SERIAL PRIMARY KEY,
	movie_name text NOT NULL,
	year integer NOT NULL,
	rating real
);

CREATE TABLE Actors(
	actor_id SERIAL PRIMARY KEY,
	actor_name text NOT NULL
);

CREATE TABLE Directors(
	director_id SERIAL PRIMARY KEY,
	director_name text NOT NULL
);

CREATE TABLE Genre(
	genre_id SERIAL PRIMARY KEY,
	genre text NOT NULL
);

CREATE TABLE StreamingServices(
	services_id SERIAL PRIMARY KEY,
	services_name text NOT NULL,
	services_price real NOT NULL
);

CREATE TABLE acted_in(
	movie_id integer,
	actor_id integer,
	FOREIGN KEY(movie_id) REFERENCES Movies(movie_id),
	FOREIGN KEY(actor_id) REFERENCES Actors(actor_id),
	PRIMARY KEY(movie_id, actor_id)
);

CREATE TABLE Directed(
	movie_id integer,
	director_id integer,
	FOREIGN KEY(movie_id) REFERENCES Movies(movie_id),
	FOREIGN KEY(director_id) REFERENCES Directors(director_id),
	PRIMARY KEY(movie_id, director_id)
);

CREATE TABLE streaming(
	movie_id integer,
	services_id integer,
	FOREIGN KEY(movie_id) REFERENCES Movies(movie_id),
	FOREIGN KEY(services_id) REFERENCES StreamingServices(services_id),
	PRIMARY KEY(movie_id, services_id)
);

CREATE TABLE MovieGenre(
	movie_id integer,
	genre_id integer,
	FOREIGN KEY(movie_id) REFERENCES Movies(movie_id),
	FOREIGN KEY(genre_id) REFERENCES Genre(genre_id),
	PRIMARY KEY(movie_id, genre_id)
);

COPY movies(movie_id, movie_name, year, rating)
FROM 'C:\\dev\\DIS-project\\database\movies.csv'
DELIMITER ','
CSV HEADER;

COPY actors(actor_id, actor_name)
FROM 'C:\\dev\\DIS-project\\database\actors.csv'
DELIMITER ','
CSV HEADER;

COPY directors(director_id, director_name)
FROM 'C:\\dev\\DIS-project\\database\directors.csv'
DELIMITER ','
CSV HEADER;

COPY genre(genre_id, genre)
FROM 'C:\\dev\\DIS-project\\database\genre.csv'
DELIMITER ','
CSV HEADER;

COPY StreamingServices(services_id, services_name, services_price)
FROM 'C:\\dev\\DIS-project\\database\StreamingServices.csv'
DELIMITER ','
CSV HEADER;

COPY acted_in(movie_id, actor_id)
FROM 'C:\\dev\\DIS-project\\database\acted_in.csv'
DELIMITER ','
CSV HEADER;

COPY directed(movie_id, director_id)
FROM 'C:\\dev\\DIS-project\\database\directed.csv'
DELIMITER ','
CSV HEADER;

COPY streaming(movie_id, services_id)
FROM 'C:\\dev\\DIS-project\\database\streaming.csv'
DELIMITER ','
CSV HEADER;

COPY moviegenre(movie_id, genre_id)
FROM 'C:\\dev\\DIS-project\\database\moviegenre.csv'
DELIMITER ','
CSV HEADER;
# Connection
from getpass import getpass
from mysql.connector import connect, Error

try:
	with connect(
			host="localhost", user=input("Enter username: "), password=getpass("Enter password: "),
			database="online_movie_rating", ) as connection:
		print(connection)
except Error as e:
	print(e)

# Create table
create_movies_table_query = """
CREATE TABLE movies(
	id INT AUTO_INCREMENT PRIMARY KEY,
	title VARCHAR(100),
	release_year YEAR(4),
	genre VARCHAR(100),
	collection_in_mil INT
)
"""
with connection.cursor() as cursor:
	cursor.execute(create_movies_table_query)
	connection.commit()

# Showing Table Schema
show_table_query = "DESCRIBE movies"
with connection.cursor() as cursor:
	cursor.execute(show_table_query)
	# Fetch rows from last executed query
	result = cursor.fetchall()
	for row in result:
		print(row)

# Modify table
alter_table_query = """
	ALTER TABLE movies
	MODIFY COLUMN collection_in_mil DECIMAL(4,1)
	"""
show_table_query = "DESCRIBE movies"
with connection.cursor() as cursor:
	cursor.execute(alter_table_query)
	cursor.execute(show_table_query)
	# Fetch rows from last executed query
	result = cursor.fetchall()
	print("Movie Table Schema after alteration:")
	for row in result:
		print(row)

# Deleting table
drop_table_query = "DROP TABLE ratings"
with connection.cursor() as cursor:
	cursor.execute(drop_table_query)


# Insert records
insert_movies_query = """
INSERT INTO movies (title, release_year, genre, collection_in_mil)
VALUES
	("Forrest Gump", 1994, "Drama", 330.2),
	("3 Idiots", 2009, "Drama", 2.4),
	("Eternal Sunshine of the Spotless Mind", 2004, "Drama", 34.5),
	("Good Will Hunting", 1997, "Drama", 138.1),
	("Skyfall", 2012, "Action", 304.6),
	("Gladiator", 2000, "Action", 188.7),
	("Black", 2005, "Drama", 3.0),
	("Titanic", 1997, "Romance", 659.2),
	("The Shawshank Redemption", 1994, "Drama",28.4),
	("Udaan", 2010, "Drama", 1.5),
	("Home Alone", 1990, "Comedy", 286.9),
	("Casablanca", 1942, "Romance", 1.0),
	("Avengers: Endgame", 2019, "Action", 858.8),
	("Night of the Living Dead", 1968, "Horror", 2.5),
	("The Godfather", 1972, "Crime", 135.6),
	("Haider", 2014, "Action", 4.2),
	("Inception", 2010, "Adventure", 293.7),
	("Evil", 2003, "Horror", 1.3),
	("Toy Story 4", 2019, "Animation", 434.9),
	("Air Force One", 1997, "Drama", 138.1),
	("The Dark Knight", 2008, "Action",535.4),
	("Bhaag Milkha Bhaag", 2013, "Sport", 4.1),
	("The Lion King", 1994, "Animation", 423.6),
	("Pulp Fiction", 1994, "Crime", 108.8),
	("Kai Po Che", 2013, "Sport", 6.0),
	("Beasts of No Nation", 2015, "War", 1.4),
	("Andadhun", 2018, "Thriller", 2.9),
	("The Silence of the Lambs", 1991, "Crime", 68.2),
	("Deadpool", 2016, "Action", 363.6),
	("Drishyam", 2015, "Mystery", 3.0)
"""
with connection.cursor() as cursor:
	cursor.execute(insert_movies_query)
	# see also executemany()
connection.commit()

# Reading records from ddbb
select_movies_query = "SELECT * FROM movies LIMIT 5"
with connection.cursor() as cursor:
	cursor.execute(select_movies_query)
	result = cursor.fetchall()
	for row in result:
		print(row)

# Filtering results
select_movies_query = """
	SELECT title, collection_in_mil
	FROM movies
	WHERE collection_in_mil > 300
	ORDER BY collection_in_mil DESC
	"""

with connection.cursor() as cursor:
	cursor.execute(select_movies_query)
	for movie in cursor.fetchall():
		print(movie)

# Handling multiple tables with JOIN
	select_movies_query = """
	SELECT title, AVG(rating) as average_rating
	FROM ratings
	INNER JOIN movies
		ON movies.id = ratings.movie_id
	GROUP BY movie_id
	ORDER BY average_rating DESC
	LIMIT 5
	"""
	with connection.cursor() as cursor:
		cursor.execute(select_movies_query)
		for movie in cursor.fetchall():
			print(movie)

# Update records
update_query = """
UPDATE
    reviewers
SET
    last_name = "Cooper"
WHERE
    first_name = "Amy"
"""
with connection.cursor() as cursor:
	cursor.execute(update_query)
	connection.commit()

# Delete records
select_movies_query = """
	SELECT reviewer_id, movie_id FROM ratings
	WHERE reviewer_id = 2
	"""
with connection.cursor() as cursor:
	cursor.execute(select_movies_query)
	for movie in cursor.fetchall():
		print(movie)

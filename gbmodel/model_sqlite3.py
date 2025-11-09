"""
Data is stored in a SQLite database that looks something like the following:
+------------+------------------+------------+----------------+
| title                | artist  | genre       | rating |
+============+==================+============+----------------+
| Wish You Were Here  | Incubus | Alternative | 5.0    |
+------------+------------------+------------+----------------+
"""
from .Model import Model
import sqlite3
DB_FILE = 'entries.db'    # file for our Database

class model(Model):
    def __init__(self):
        # Make sure our database exists
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from songs")
        except sqlite3.OperationalError:
            cursor.execute("create table songs (title text, artist text, genre text, rating float)")
        cursor.close()

    def select(self):
        """
        Gets all rows from the database
        Each row contains: name, email, date, message
        :return: List of lists containing all rows of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM songs")
        return cursor.fetchall()

    def insert(self, title, artist, genre, rating):
        """
        Inserts entry into database
        :param title: String
        :param artist: String
        :param genre: String
        :param rating: Float
        :return: True
        :raises: Database errors on connection and insertion
        """
        params = {'title':title, 'artist':artist, 'genre':genre, 'rating':rating}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into songs (title, artist, genre, rating) "
                       "VALUES (:title, :artist, :genre, :rating)", params)

        connection.commit()
        cursor.close()
        return True

'''
Abstract Model Class design
'''

class Model():
    def select(self):
        """
        Gets all entries from the database
        :return: Tuple containing all rows of database
        """
        pass

    def insert(self, title, artist, genre, rating):
        """
        Inserts entry into database
        :param title: String
        :param artist: String
        :param genre: String
        :param rating: Float
        :return: none
        :raises: Database errors on connection and insertion
        """
        pass

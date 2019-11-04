import os.path
import sqlite3


class DatabaseConnect:

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, 'movies.sqlite')

    def __init__(self):
        self.CONNECT_DATABASE = sqlite3.connect(DatabaseConnect.db_path)

    def get_column_name(self):
        """
        description: function get all column names from database
        use: POPULATE database with api data
        :return: LIST of column names
        """
        cursor = self.CONNECT_DATABASE.execute('select * from MOVIES')
        list_column_names = [description[0] for description in cursor.description]
        return list_column_names

    def get_column_record(self, column_name):
        """
        description: function get all title names from database
        use: POPULATE database with api data
        :return: LIST of title names
        """
        cursor = self.CONNECT_DATABASE.execute('select {0} from MOVIES'.format(column_name))

        column_record_list = []

        for column in cursor:
            for record in column:
                column_record_list.append(record)

        return column_record_list


#databaseconnect = DatabaseConnect()
#print(databaseconnect.CONNECT_DATABASE)
#print(databaseconnect.get_column_name())
#print(databaseconnect.get_column_record('TITLE'))

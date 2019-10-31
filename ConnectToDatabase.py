import os.path
import sqlite3


class SqliteConnectQuery:

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, 'movies.sqlite')

    def __init__(self):
        self.connect_database = sqlite3.connect(SqliteConnectQuery.db_path)

    def connect_to_database(self):
        connection = sqlite3.connect(SqliteConnectQuery.db_path)
        return connection

    def cursor_execute_query(self, query):

        return self.connect_database.execute(query)


#sqliteconnectquery = SqliteConnectQuery()
#print(sqliteconnectquery.connect_to_database())


class SqliteColumnTitle(SqliteConnectQuery):

    def get_column_name(self):

        cursor = self.cursor_execute_query('select * from MOVIES')
        list_column_names = [description[0] for description in cursor.description]
        return list_column_names

    def get_title_name(self, query):
        
        cursor = self.cursor_execute_query(query)
        row = cursor.fetchall()
        return row


sqlitecolumntitle = SqliteColumnTitle()
print(sqlitecolumntitle.get_column_name())
print(sqlitecolumntitle.get_title_name('select TITLE from MOVIES'))

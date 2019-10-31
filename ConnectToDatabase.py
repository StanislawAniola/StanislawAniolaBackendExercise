import os.path
import sqlite3


class SqliteConnectQuery:

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, 'movies.sqlite')

    def __init__(self):
        self.CONNECT_DATABASE = sqlite3.connect(SqliteConnectQuery.db_path)

    def cursor_execute_query(self, query):

        return self.CONNECT_DATABASE.execute(query)


#sqliteconnectquery = SqliteConnectQuery()
#print(sqliteconnectquery.CONNECT_DATABASE)


class SqliteColumnTitle(SqliteConnectQuery):

    def get_column_name(self):

        cursor = self.cursor_execute_query('select * from MOVIES')
        list_column_names = [description[0] for description in cursor.description]
        return list_column_names

    def get_title_name(self):
        
        cursor = self.cursor_execute_query('select TITLE from MOVIES')

        title_list = []
        
        for column in cursor:
            for record in column:
                title_list.append(record)

        return title_list


    def get_as_dict():

        




#sqlitecolumntitle = SqliteColumnTitle()
#print(sqlitecolumntitle.get_column_name())
#print(sqlitecolumntitle.get_title_name())

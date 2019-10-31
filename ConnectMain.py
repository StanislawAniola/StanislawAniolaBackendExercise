import requests
import sqlite3

from ConnectToDatabase import SqliteConnectQuery, SqliteColumnTitle
from ConnectToApi import ApiGetData


class ProcessApiDict():

    def convert_api_keys(self, dict_key_to_process):

        dict_key_upper = {k.upper():v for k, v in dict_key_to_process.items()}

        dict_key_upper['CAST'] = dict_key_upper.pop('ACTORS')
        dict_key_upper['IMDb_Rating'] = dict_key_upper.pop('IMDBRATING')
        dict_key_upper['IMDb_votes'] = dict_key_upper.pop('IMDBVOTES')

        if 'BOXOFFICE' in dict_key_upper.keys():
            dict_key_upper['BOX_OFFICE'] = dict_key_upper.pop('BOXOFFICE')
        else:
            print('')

        return dict_key_upper

    def convert_api_values(self, dict_val_to_process):

        dict_movie_without_quote = {k:v.replace('"', '') for k, v in dict_val_to_process.items()}
        return dict_movie_without_quote

    def get_api_col_same_as_database(self, column_name_list, dict_with_all_col):
        
        dict_col_as_database = {}
        
        dict_upper_key = self.convert_api_keys(dict_with_all_col)

        for column in column_name_list:
            if column in dict_upper_key:
                dict_col_as_database[column] = dict_upper_key[column]

        dict_processed_val = self.convert_api_values(dict_col_as_database)

        return dict_processed_val


class ApiSqlitePutData(ApiGetData, SqliteColumnTitle, SqliteConnectQuery, ProcessApiDict):

    def get_same_movie_as_database(self):

        movie_list_of_dict = []

        for record in self.get_title_name():
            api_movie = self.get_api_data(record)
            api_dict = self.convert_data_to_dict(api_movie)

            movie_list_of_dict.append(self.get_api_col_same_as_database(self.get_column_name(), api_dict))

        return movie_list_of_dict


    def populate_database(self):

        connection = self.CONNECT_DATABASE
        id = 0

        while id < len(self.get_same_movie_as_database()):
            for dict_movie in self.get_same_movie_as_database():
                for k, v in dict_movie.items():

                    query_update = 'UPDATE MOVIES SET "{0}" = "{1}" WHERE "ID" = "{2}"'.format(k, v, id)
                    connection.execute(query_update)
                    connection.commit()
                print('POPULATED: ' + dict_movie['TITLE'])
                id += 1            

#apisqliteputdata = ApiSqlitePutData()
#print(apisqliteputdata.get_same_movie_as_database())
#apisqliteputdata.populate_database()







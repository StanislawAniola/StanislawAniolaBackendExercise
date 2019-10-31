import requests
import sqlite3

from ConnectToDatabase import SqliteConnectQuery, SqliteColumnTitle
from ConnectToApi import ApiGetData


class ProcessApiDict():

    def convert_api_keys(self, dict_key_process):

        dictionary_key_upper = {}

        for k, v in dict_key_process.items():
            k_upper = k.upper()
            dictionary_key_upper[k_upper] = v

        dictionary_key_upper['CAST'] = dictionary_key_upper.pop('ACTORS')
        dictionary_key_upper['IMDb_Rating'] = dictionary_key_upper.pop('IMDBRATING')
        dictionary_key_upper['IMDb_votes'] = dictionary_key_upper.pop('IMDBVOTES')

        if 'BOXOFFICE' in dictionary_key_upper.keys():
            dictionary_key_upper['BOX_OFFICE'] = dictionary_key_upper.pop('BOXOFFICE')
        else:
            print('')

        return dictionary_key_upper

    def convert_api_values(self, dict_val_process):

        dictionary_val_quote = {}

        for k, v in dict_val_process.items():
            v_quote = v.replace('"', '')

            dictionary_val_quote[k] = v_quote

        return dictionary_val_quote

    def get_api_column_same_as_database(self, column_name_list, dict_with_all_col):
        
        dict_col_as_database = {}
        
        dict_upper_key = self.convert_api_keys(dict_with_all_col)

        for column in column_name_list:
            if column in dict_upper_key:
                dict_col_as_database[column] = dict_upper_key[column]

        dict_processed_val = self.convert_api_values(dict_col_as_database)

        return dict_processed_val

class ApiSqliteSameData(ApiGetData, SqliteColumnTitle, SqliteConnectQuery, ProcessApiDict):

    def get_same_movie_as_database(self):
        movie_list_of_dict = []

        for column in self.connect_database.execute('select TITLE from MOVIES'):
            for record in column:
                api_movie = self.get_api_data(record)
                api_dict = self.convert_data_to_dict(api_movie)

                movie_list_of_dict.append(self.get_api_column_same_as_database(self.get_column_name(), api_dict))

        return movie_list_of_dict


#apisqlitesamedata = ApiSqliteSameData()
#print(apisqlitesamedata.get_same_movie_as_database())


class ApiSqlitePutData(ApiSqliteSameData, SqliteColumnTitle, SqliteConnectQuery):

    def put_data_to_database(self):

        connection = self.connect_to_database()
        x = 0

        while x < len(self.get_same_movie_as_database()):
            for dict_movie in self.get_same_movie_as_database():
                for k, v in dict_movie.items():

                    query = 'UPDATE MOVIES SET "{0}" = "{1}" WHERE "ID" = "{2}"'.format(k, v, x)
                    connection.execute(query)
                    connection.commit()
                print('POPULATED: ' + dict_movie['TITLE'])
                x += 1            

apisqliteputdata = ApiSqlitePutData()
apisqliteputdata.put_data_to_database()





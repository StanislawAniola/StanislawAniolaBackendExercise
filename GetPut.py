from ConnectToApi import ApiGetData
from ConnectMain import ProcessApiDict
from ConnectToDatabase import SqliteColumnTitle, SqliteConnectQuery


class GetApiData(ApiGetData, ProcessApiDict, SqliteColumnTitle):

    def get_api_movie(self, movie_name):

        x = self.convert_data_to_dict(self.get_api_data(movie_name))
        y = self.get_api_col_same_as_database(self.get_column_name(), x)

        return y

#getapidata = GetApiData()
#print(getapidata.get_api_movie('Blade'))


class PutApiMovieToDatabase(GetApiData):

    def put_movie_to_database(self, movie_title):

        if movie_title in self.get_title_name():
            print('movie is already in database')
        else:
            connection = self.CONNECT_DATABASE
            max_id = len(self.get_title_name())
            add_id = self.get_api_movie(movie_title)

            query_insert = 'INSERT INTO MOVIES (ID) VALUES ({0})'.format(max_id)
            connection.execute(query_insert)
            connection.commit()

            for k, v in add_id.items():
                query_update = 'UPDATE MOVIES SET "{0}" = "{1}" WHERE "ID" = "{2}"'.format(k, v, max_id)
                connection.execute(query_update)
                connection.commit()
                print('UPDATED: {0}'.format(k))


#putapimovietodatabase = PutApiMovieToDatabase()
#test.put_movie_to_database('Blade')
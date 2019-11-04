from ConnectToApi import ApiGetData, ProcessApiDict
from ConnectToDatabase import DatabaseConnect

class UpdateDatabase(DatabaseConnect):

    def update_database_with_api(self, api_dict_processed, index):
        """
        description: fill missed data in database with those from api
        :param api_dict_processed
        :param index: index where data will be place
        :return: UPDATE database with api values
        """

        connection = self.CONNECT_DATABASE #DatabaseConnect
        for k, v in api_dict_processed.items():
            query_update = 'UPDATE MOVIES SET "{0}" = "{1}" WHERE "ID" = "{2}"'.format(k, v, index)
            connection.execute(query_update)
            connection.commit()

        print('UPDATED: {0}'.format(api_dict_processed['TITLE']))


class InsertIntoDatabase(UpdateDatabase, ProcessApiDict, ApiGetData, DatabaseConnect):

    def put_movie_to_database(self, movie_title):
        """
        description: Insert next ID to database to next populate it
        :param movie_title - title of movie that will be putted to dataabse
        """

        if movie_title in self.get_column_record('TITLE'):
            print('movie is already in database')
        else:
            connection = self.CONNECT_DATABASE
            max_id = len(self.get_column_record('TITLE'))
            movie_to_insert = self.api_data_processed(movie_title)

            query_insert = 'INSERT INTO MOVIES (ID) VALUES ({0})'.format(max_id)
            connection.execute(query_insert)
            connection.commit()

            self.update_database_with_api(movie_to_insert, max_id)


#insertintodatabase = InsertIntoDatabase()
#insertintodatabase.put_movie_to_database('Blade')


class GetDatabaseRecords(DatabaseConnect):

    def combine_column_row(self, database_column):
        """
        description: get database TITLE and indicated column records
        :param database_column: variable by with will be operations like sorting
        :return: LIST of DICTIONARIES contains TITLE and indicated column records
        """
        list_of_movies = []

        movie_list_zip = zip(self.get_column_record('TITLE'), self.get_column_record(database_column))
        movie_list = []

        for movie in movie_list_zip:
            movie_list.append(movie)

        for i in movie_list:
            main_dict = {}
            main_dict['TITLE'] = i[0]
            main_dict[database_column] = i[-1]
            list_of_movies.append(main_dict)

        return list_of_movies

    def filter_by(self, database_column):
        """
        FUNCTION IN PROGRESS
        :param database_column: variable by with will be operations like sorting
        :return:
        """

        raw_list = self.get_column_record(database_column)
        str_list = []
        for i in raw_list:
            str_list.append(str(i))
        
        replace_ist = [j.replace('–', '') for j in str_list]
        int_list = []

        for i in replace_ist:
            int_list.append(int(i))

        return sorted(int_list)

        
#get_database_records = GetDatabaseRecords()
#print(get_database_records.combine_column_row('YEAR'))
#print(get_database_records.filter_by('YEAR'))
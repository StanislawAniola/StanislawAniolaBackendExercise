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
        description: fill missed data in database with those from api
        :param api_dict_processed
        :param index: index where data will be place
        :return: UPDATE database with api values
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

        raw_list = self.get_column_record(database_column)
        ll_list = []
        for i in raw_list:
            ll_list.append(str(i))
        
        lll_list = [j.replace('–', '') for j in ll_list]
        llll_list = []

        for i in lll_list:
            llll_list.append(int(i))

        return sorted(lll_list)

        



#get_database_records = GetDatabaseRecords()
#print(get_database_records.combine_column_row('YEAR'))
#print(get_database_records.filter_by('YEAR'))


def post_code(first, second):
    first_one = first.replace('-', '')
    second_one = second.replace('-', '')

    x = int(first_one)
    y = int(second_one)

    int_list = [i for i in range(x, y+1)]
        
    str_list = [str(i) for i in int_list]

    asd = []
    for i in str_list:
        print(i[-1])
    


post_code('79-900', '80-155')
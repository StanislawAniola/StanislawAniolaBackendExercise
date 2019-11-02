from ConnectToDatabase import DatabaseConnect
from ConnectToApi import ApiGetData


class ProcessApiDict(DatabaseConnect):

    def get_api_col_same_as_database(self, api_dict_raw):
        """
        MAIN FUNC OF CLASS
        description: function process api_dict to makes it contain same dictionary keys as database columns
        use: same dictionary keys as database columns
        :api_dict_raw dict_with_all_col: api dictionary with all keys and values
        :return: DICTIONARY with filtered keys
        """
        column_name_list = self.get_column_name() #DatabaseConnect
        dict_upper_key = self.convert_api_keys(api_dict_raw)

        dict_key_as_col = {}
        for column in column_name_list:
            if column in dict_upper_key:
                dict_key_as_col[column] = dict_upper_key[column]

        dict_processed_val_and_keys = self.convert_api_values(dict_key_as_col)

        return dict_processed_val_and_keys

    def convert_api_keys(self, api_dict_key):
        """
        description: function makes key in dictionary from api to be similar with column names in database
        use: dictionary key == database column name
        :param api_dict_key: dict with keys and values from api
        :return: DICTIONARY with processed keys
        """
        dict_key_upper = {k.upper(): v for k, v in api_dict_key.items()}

        dict_key_upper['CAST'] = dict_key_upper.pop('ACTORS')
        dict_key_upper['IMDb_Rating'] = dict_key_upper.pop('IMDBRATING')
        dict_key_upper['IMDb_votes'] = dict_key_upper.pop('IMDBVOTES')

        if 'BOXOFFICE' in dict_key_upper.keys():
            dict_key_upper['BOX_OFFICE'] = dict_key_upper.pop('BOXOFFICE')
        else:
            print('')

        return dict_key_upper

    def convert_api_values(self, api_dict_val):
        """
        description: function prepares api dict values to populate database
        use: replace '"' with ''
        :param api_dict_val: dict with keys and values from api
        :return: DICTIONARY with processed values
        """
        dict_movie_without_quote = {k: v.replace('"', '') for k, v in api_dict_val.items()}
        return dict_movie_without_quote


#test = ProcessApiDict()
#test2 = ApiGetData()
#print(test.get_api_col_same_as_database(test2.convert_data_to_dict('Blade')))


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


class ApiPopulateDatabase(ApiGetData, ProcessApiDict, UpdateDatabase):

    def populate_database(self):
        """
        MAIN FUNC OF CLASS
        description: populate database
        :return:
        """
        id_movie = 0

        while id_movie < len(self.get_same_movie_as_database()):
            for dict_movie in self.get_same_movie_as_database(): #ApiGetData
                self.update_database_with_api(dict_movie, id_movie)
                id_movie += 1

    def get_same_movie_as_database(self):
        """
        description: function adds api dict if key 'TITLE' is in database
        :return: LIST of api movies same as in database
        """
        movie_list_of_dict = []

        for title in self.get_title_name(): #DatabaseConnect
            #api_movie = self.get_api_data(title)
            api_dict = self.convert_data_to_dict(title)

            movie_list_of_dict.append(self.get_api_col_same_as_database(api_dict)) #ProcessApiDict

        return movie_list_of_dict


#apisqliteputdata = ApiPopulateDatabase()
#print(apisqliteputdata.get_same_movie_as_database())
#apisqliteputdata.populate_database()







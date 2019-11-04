import requests
from ConnectToDatabase import DatabaseConnect


class ApiGetData:

    def get_api_data(self, movie_title):
        """
        description: establishes connection with an api
        :movie_title: movie title that will be geted
        :return: JSON with all selected film details
        """
        respond = requests.get('http://www.omdbapi.com/?t={0}&apikey=4554a5a6'.format(movie_title))
        return respond

    def convert_data_to_dict(self, movie_title):
        """
        descirption: convert json to dict
        :movie_title: movie title that will be geted
        :return: DICTIONARY with all selected film details
        """
        connection = self.get_api_data(movie_title)

        read_json = connection.json()
        movies_dictionary_json = dict(read_json)

        return movies_dictionary_json

#apigetdata = ApiGetData()
#print(apigetdata.get_api_data('Blade'))
#print(apigetdata.convert_data_to_dict('Blade'))


class ProcessApiDict(ApiGetData, DatabaseConnect):

    def api_data_processed(self, movie_title):
        """
        MAIN FUNC OF CLASS
        description: function is a hub between get_api_col_same_as_database and 
        raw data from api: convert_data_to_dict
        :movie_title: title of movie that will be get from api
        :return: DICTIONARY with data from api ready to work with
        """
        api_dict_raw = self.convert_data_to_dict(movie_title)
        api_dict_processed = self.get_api_col_same_as_database(api_dict_raw)

        return api_dict_processed

    def get_api_col_same_as_database(self, api_dict_raw):
        """
        description: function process api_dict to makes it contain same dictionary keys as database columns
        use: same dictionary keys as database columns
        :api_dict_raw: api dictionary with all keys and values
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

#processapidict = ProcessApiDict()
#print(processapidict.api_data_processed('Blade'))

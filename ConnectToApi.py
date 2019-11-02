import requests


class ApiGetData:

    def get_api_data(self, movie_title):
        
        respond = requests.get('http://www.omdbapi.com/?t={0}&apikey=4554a5a6'.format(movie_title))
        return respond

    def convert_data_to_dict(self, movie_title):

        connection = self.get_api_data(movie_title)

        read_json = connection.json()
        movies_dictionary_json = dict(read_json)

        return movies_dictionary_json

#apigetdata = ApiGetData()
#print(apigetdata.convert_data_to_dict('Blade'))

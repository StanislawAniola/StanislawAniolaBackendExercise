import requests


class ApiGetData:

    def get_api_data(self, movie_title):
        
        respond = requests.get('http://www.omdbapi.com/?t={0}&apikey=4554a5a6'.format(movie_title))
        return respond

    def convert_data_to_dict(self, api_connection):

        read_json = api_connection.json()
        movies_dictionary_json = dict(read_json)

        return movies_dictionary_json

#apigetdata = ApiGetData()
#connect = apigetdata.get_api_data('Gran Torino')
#print(connect)
#print(apigetdata.convert_data_to_dict(connect))
from ConnectToDatabase import DatabaseConnect
from ConnectToApi import ApiGetData, ProcessApiDict
from DatabaseQueries import UpdateDatabase


class ApiPopulateDatabase(ProcessApiDict, ApiGetData, UpdateDatabase, DatabaseConnect):

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

        for title in self.get_column_record('TITLE'): #DatabaseConnect
            api_dict = self.convert_data_to_dict(title)
            movie_list_of_dict.append(self.get_api_col_same_as_database(api_dict)) #ProcessApiDict

        return movie_list_of_dict


#apisqliteputdata = ApiPopulateDatabase()
#print(apisqliteputdata.get_same_movie_as_database())
#apisqliteputdata.populate_database()







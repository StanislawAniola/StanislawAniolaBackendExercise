import argparse


from PopulateDatabase import ApiPopulateDatabase
from DatabaseQueries import InsertIntoDatabase, GetDatabaseRecords

# populate database
# get/put spceyfic film
# filter by YEAR

parser = argparse.ArgumentParser(description='Execute operations')
parser.add_argument('-populate', '--populate', action='store_true', help='fill missing data')
parser.add_argument('-add', '--add', type=str, metavar='', help='movie title to insert to the database')
# parser.add_argument('-sort_by', '--sort_by', type=str, metavar='', help='sort movies by year')

args = parser.parse_args()

if __name__ == '__main__':
    if args.populate:
        api_populate_database = ApiPopulateDatabase()
        api_populate_database.populate_database()
    elif args.add:
        insert_into_database = InsertIntoDatabase()
        insert_into_database.put_movie_to_database(args.add)
    """
    elif args.sort_by:
        get_database_records = GetDatabaseRecords()
        get_database_records.filter_by(args.sort_by)
    """



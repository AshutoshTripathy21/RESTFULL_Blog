from pymongo import MongoClient

class Database:
    def __init__(self, db_name='blogging_platform'):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client[db_name]
        self.posts_collection = self.db['posts']
        self.users_collection = self.db['users']
        self.comments_collection = self.db['comments']

    def close_connection(self):
        self.client.close()

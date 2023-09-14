import unittest
from app import app
# if you're going to use a database, make sure you import the necessary modules here

class BaseCase(unittest.TestCase):

    def setUp(self):
        # this statement will be executed before each test
        self.app = app.test_client()
        # If you're planning to use a database:
        # self.db = db.get_db()  # e.g., get db connection
    
    def tearDown(self):
        # this statement will be executed after each test
        # If you're planning to use a database:
        # for collection in self.db.list_collection_names():
        #     self.db.drop_collection(collection)

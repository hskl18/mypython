import unittest
from app.routes import calculate_sum
from tests.base_case import BaseCase

class TestSum(BaseCase):

    def test_list_int(self):
        data = [1, 2, 3, 4, 5]
        result = calculate_sum(data)
        self.assertEqual(result, 15)
    
    # ... add your other test methods for sum ...

class TestFlaskRoutes(BaseCase):

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Hello, World!")
        
    # ... add other test methods for other routes ...

if __name__ == '__main__':
    unittest.main()

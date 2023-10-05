''' server tests '''

import unittest

from server import Server

class HelloWorldAPITestCase(unittest.TestCase):
    ''' Class for "hello world" api call testing '''
    def setUp(self):
        ''' call before each test '''
        server = Server()
        app = server.get_app()
        app.testing = True
        self.app = app.test_client()

    def test_hello_world(self):
        ''' test "hello world" call '''
        # Send GET request to the /hello endpoint
        response = self.app.get('/')

        # Check the status code
        self.assertEqual(response.status_code, 200)

        # Check the response data
        self.assertEqual(response.data.decode(), "Hello World!")

if __name__ == '__main__':
    unittest.main()

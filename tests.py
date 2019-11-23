import unittest
from app import *

class TestHome(unittest.TestCase):
	def test_get(self):
		"""Must return status code 200"""
		app_test = app.test_client()
		response = app_test.get('/')
		self.assertEqual(200, response.status_code)

if __name__ == '__main__':
	unittest.main()
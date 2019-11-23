import unittest
from app import *

class TestHome(unittest.TestCase):
	def test_get(self):
		"""Must return status code 200"""
		app_test = app.test_client()
		response = app_test.get('/')
		self.assertEqual(200, response.status_code)

	def test_content_type(self):
		"""Must return file type html""" 
		app_test = app.test_client()
		response = app_test.get('/')
		self.assertIn('text/html', response.content_type)
		
if __name__ == '__main__':
	unittest.main()
import unittest
from app import *

class TestHome(unittest.TestCase):

	def setUp(self):
		"""good development practices"""
		app_test = app.test_client()
		self.response = app_test.get('/')

	def test_get(self):
		"""Must return status code 200"""
		#app_test = app.test_client()
		#response = app_test.get('/')
		self.assertEqual(200, self.response.status_code)

	def test_content_type(self):
		"""Must return file type html""" 
		#app_test = app.test_client()
		#response = app_test.get('/')
		self.assertIn('text/html', self.response.content_type)

if __name__ == '__main__':
	unittest.main()
import unittest
from app import *

class TestHome(unittest.TestCase):

	def setUp(self):
		"""good development practices"""
		app_test = app.test_client()
		self.response = app_test.get('/')

	def test_get(self):
		"""Must return status code 200"""
		self.assertEqual(200, self.response.status_code)

	def test_content_type(self):
		"""Must return file type html""" 
		self.assertIn('text/html', self.response.content_type)

	def test_content_text(self):
		"""Must contain 'Lista dos Buckets' as text content"""
		#self.assertIn('Lista dos Buckets', self.response.data)
		self.assertIn('Lista dos Buckets', self.response.data.decode('utf-8'))		

if __name__ == '__main__':
	unittest.main()
from django.urls import resolve
from django.test import TestCase
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string


class HomePageTest(TestCase):

	def test_uses_home_template(self):
		response = self.client.get("/")
		self.assertTemplateUsed(response, "home.html")
	
	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		html = response.content.decode("utf8")
		expected_html = render_to_string("home.html")
		self.assertEqual(html, expected_html)
	
		'''
		response = self.client.get('/')
		
		html = response.content.decode('utf8')
		self.assertTrue(html.startswith('<html>'))
		self.assertIn('<title>To-Do lists</title>', html)
		self.assertTrue(html.strip().endswith('</html>'))
		
		self.assertTemplateUsed(response, 'home.html')
		'''

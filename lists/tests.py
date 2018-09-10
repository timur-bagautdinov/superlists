from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from lists.views import home_page


class HomePageTest(TestCase):
    """
    Test for home page
    """

    def test_root_url_resolves_to_home_page_view(self):
        """
        Test: root url transform to a view
        """
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        """
        test: Home page returns a correct html
        :return:
        """
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf-8')

        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))

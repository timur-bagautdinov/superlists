from django.test import TestCase


class HomePageTest(TestCase):
    """
    Test for home page
    """
    def test_home_page_returns_correct_html(self):
        """
        test: Home page returns a correct html
        :return:
        """
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'home.html')

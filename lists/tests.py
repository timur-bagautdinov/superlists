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

    def test_can_save_a_POST_request(self):
        """
        test: can save post request
        :return:
        """
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
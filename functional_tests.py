from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    """
    Test for a new visitor
    """

    def setUp(self):
        """
        setup
        """
        self.browser = webdriver.Firefox()

    def tearDown(self):
        """
        tear down
        """
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        """
        test: become a list and get its later
        """
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        self.fail('End Test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')

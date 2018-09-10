from django.test import TestCase


class SmokeTest(TestCase):
    """
    Toxicity test
    """

    def test_bad_maths(self):
        """
        test: bad math calculation
        """
        self.assertEqual(1 + 1, 3)

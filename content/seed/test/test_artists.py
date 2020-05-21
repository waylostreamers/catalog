from django.test import TestCase
from content.seed.artists import get_initials


class InitialsTestCase(TestCase):
    def test_bach(self):
        """
        Johann Sebastian Bach should be correctly initialed.
        """
        assert get_initials("Johann Sebastian Bach") == "J.S. Bach"

    def test_lowercase_bach(self):
        """
        lowercase names should be correctly capitalized.
        """
        assert get_initials("johann sebastian bach") == "J.S. Bach"

    def test_oneword_name(self):
        """
        Names made up of a single word should throw an error.
        """
        with self.assertRaises(ValueError):
            get_initials("sean")

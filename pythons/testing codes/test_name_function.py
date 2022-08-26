import unittest
from name_function import formattedname as name


class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted = name('janis', 'joplin')
        self.assertEqual(formatted, 'Janis Joplin')


unittest.main()

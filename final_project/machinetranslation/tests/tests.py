import unittest
from ..translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test_for_null_input(self):
        self.assertEqual(english_to_french(''), '')

    def test_for_hello(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
    def test_for_null_input(self):
        self.assertEqual(french_to_english(''), '')
    
    def test_for_bonjour(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()

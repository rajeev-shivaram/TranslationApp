"""Tests for translator."""

import unittest

from language_translation.translator import (english_to_french,
                                             french_to_english)


class TestLanguageService(unittest.TestCase):
    """Test."""

    def test_english_to_french(self):
        """Test english_to_french."""

        # Equals
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french("Goodbye"), "Au revoir")
        # Not Equals
        self.assertNotEqual(english_to_french("Hello"), "Au revoir")
        self.assertNotEqual(english_to_french("Goodbye"), "Bonjour")
        # Null Case
        self.assertEqual(english_to_french("")[0], 400)


    def test_french_to_english(self):
        """Test french_to_english."""
        # Equals
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("Au revoir"), "Goodbye")
        # Not Equals
        self.assertNotEqual(french_to_english("Bonjour"), "Goodbye")
        self.assertNotEqual(french_to_english("Au revoir"), "Hello")
        # Null Case
        self.assertEqual(french_to_english("")[0], 400)

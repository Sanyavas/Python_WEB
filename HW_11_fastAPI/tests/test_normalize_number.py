import unittest
from normalize_number import normalize_phone


class NormalizePhoneTests(unittest.TestCase):
    def test_normalize_phone_with_valid_number(self):
        value = "+1 (234) 567-8901"
        expected = None
        result = normalize_phone(value)
        self.assertEqual(result, expected)

    def test_normalize_phone_with_empty_value(self):
        value = ""
        expected = None
        result = normalize_phone(value)
        self.assertEqual(result, expected)

    def test_normalize_phone_with_empty_suf(self):
        value = "(067) 222 - 43 -54"
        expected = "+380672224354"
        result = normalize_phone(value)
        self.assertEqual(result, expected)

    def test_normalize_phone_with_invalid_length(self):
        value = "4567890"
        expected = "+380444567890"
        result = normalize_phone(value)
        self.assertEqual(result, expected)

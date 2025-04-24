import unittest
from unittest.mock import patch
import dictionary

class TestDictionary(unittest.TestCase):

    def setUp(self):
        self.sample_data = {
            "apple": ["A fruit that grows on trees."],
            "python": {
                "definition": "A programming language.",
                "synonyms": ["py"],
                "example": "Python is popular for web development."
            }
        }

    def test_load_data_valid(self):
        data = dictionary.load_data("sample_data.json")
        self.assertIsInstance(data, dict)

    def test_translate_exact_match_list(self):
        result = dictionary.translate("apple", self.sample_data)
        self.assertIn("A fruit that grows on trees.", result)

    def test_translate_exact_match_dict(self):
        result = dictionary.translate("python", self.sample_data)
        self.assertIn("A programming language.", result)
        self.assertIn("Synonyms", result)

    def test_translate_not_found(self):
        result = dictionary.translate("nonexistentword", self.sample_data)
        self.assertIn("Word cannot be found", result)

    @patch('builtins.input', return_value='apple')
    def test_get_user_input_valid(self, mock_input):
        self.assertEqual(dictionary.get_user_input(), 'apple')

    @patch('builtins.input', side_effect=['', 'python'])
    def test_get_user_input_empty_then_valid(self, mock_input):
        self.assertEqual(dictionary.get_user_input(), 'python')

    @patch('builtins.input', return_value='exit')
    def test_get_user_input_exit(self, mock_input):
        self.assertIsNone(dictionary.get_user_input())

if __name__ == '__main__':
    unittest.main()

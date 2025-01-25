"""
Amadla python management cli application unit test.

(C) 2024 Amadla. All rights reserved.
Released under MIT License
"""

import unittest
from amadlacli.utils.dict import DictUtils


class TestDictUtils(unittest.TestCase):
    """
    Test the Dictionary utilities used for merging dictionaries together (multiple methods).
    """

    def test_merge_multilevel(self):
        """
        Test merge two dictionaries and add missing components.
        """
        first = {'v1': {'configuration': {'$schema': '...', 'network': {'$schema': '...'}}}}
        second = {'v1': {'configuration': {'network': {'entries': {'$schema': '...'}}}}}
        expected = {'v1': {'configuration': {'$schema': '...', 'network': {'$schema': '...', 'entries': {'$schema': '...'}}}}}
        self.assertEqual(str(DictUtils().merge_multilevel(first, second)), str(expected), "not merging properly")

    def test_merge_first_level(self):
        """
        Test merge two dictionaries and add missing components.
        """
        first = {'v1': {'configuration': {'$schema': '...', 'network': {'$schema': '...'}}}}
        second = {'v1': {'configuration': {'network': {'entries': {'$schema': '...'}}}}}
        expected = {'v1': [{'configuration': {'$schema': '...', 'network': {'$schema': '...'}}}, {'configuration': {'network': {'entries': {'$schema': '...'}}}}]}
        self.assertEqual(str(DictUtils().merge_first_level(first, second)), str(expected), "not merging properly")

    def test_convert_to_dict_path(self):
        """
        Test merge two dictionaries and add missing components.

        @TODO: Make a better example.
        """
        first = {'v1': {'configuration': {'$schema': '...', 'network': {'$schema': '...'}}}}
        second = {'v1': {'configuration': {'network': {'entries': {'$schema': '...'}}}}}
        expected = {'v1': {'$schema': {'v1': {'configuration': {'network': {'entries': {'$schema': '...'}}}}}}}
        self.assertEqual(str(DictUtils().convert_to_dict_path(first, second)), str(expected), "not merging properly")

    #def test_wrong_compose_version(self):
    #    """
    #    Test that makes sure to fail fast if the `compose.yml` config file does not have the right version
    #    """
    #    self.assertRaises(Exception)


if __name__ == '__main__':
    unittest.main()

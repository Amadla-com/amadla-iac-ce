"""
Amadla python management cli application unit test.

(C) 2024 Amadla. All rights reserved.
Released under MIT License
"""

import unittest
from amadlacli.app import APP

# https://calmcode.io/typer/test.html
#from typer.testing import CliRunner

#runner = CliRunner()


class TestAPP(unittest.TestCase):
    """
    Test application information.
    """

    def setUp(self):
        """
        Set up the variables for the following tests.
        """
        self.app_name = 'Amadla CLI'
        self.version = '1.0.0'

    def test_name(self):
        """
        Make sure it has the name of the application.
        """
        self.assertEqual(APP().name(), self.app_name, "incorrect value")

    def test_version(self):
        """
        Make sure it has the version of the application.
        """
        self.assertEqual(APP().version(), self.version, "incorrect value")


if __name__ == '__main__':
    unittest.main()

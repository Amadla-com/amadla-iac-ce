"""
Amadla cli.

(C) 2024 Jean-Nicolas Boulay Desjardins (JNBD)
Released under MIT License

CLI classes.
"""

import unittest
from unittest.mock import patch
from amadlacli.utils.pyproject import PyProject


class TestPyProject(unittest.TestCase):

    @patch('pyproject.open')
    def test_data(self, mock_open):
        mock_file = mock_open.return_value.__enter__.return_value
        mock_file.read.return_value = '''
        [tool.poetry]
        name = "test_project"
        version = "0.1.0"
        description = "Test project description"
        '''
        project = PyProject()
        project.data = "pyproject.toml"
        self.assertEqual(project.data["tool"]["poetry"]["name"], "test_project")
        self.assertEqual(project.data["tool"]["poetry"]["version"], "0.1.0")
        self.assertEqual(project.data["tool"]["poetry"]["description"], "Test project description")

    @patch('pyproject.open')
    def test_project_version(self, mock_open):
        mock_file = mock_open.return_value.__enter__.return_value
        mock_file.read.return_value = '''
        [tool.poetry]
        name = "test_project"
        version = "0.1.0"
        description = "Test project description"
        '''
        project = PyProject()
        project.data = "pyproject.toml"
        self.assertEqual(project.project_version(), "0.1.0")

    @patch('pyproject.open')
    def test_project_name(self, mock_open):
        mock_file = mock_open.return_value.__enter__.return_value
        mock_file.read.return_value = '''
        [tool.poetry]
        name = "test_project"
        version = "0.1.0"
        description = "Test project description"
        '''
        project = PyProject()
        project.data = "pyproject.toml"
        self.assertEqual(project.project_name(), "test_project")

    @patch('pyproject.open')
    def test_project_description(self, mock_open):
        mock_file = mock_open.return_value.__enter__.return_value
        mock_file.read.return_value = '''
        [tool.poetry]
        name = "test_project"
        version = "0.1.0"
        description = "Test project description"
        '''
        project = PyProject()
        project.data = "pyproject.toml"
        self.assertEqual(project.project_description(), "Test project description")


if __name__ == '__main__':
    unittest.main()

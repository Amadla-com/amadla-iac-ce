"""
Amadla cli.

(C) 2024 Jean-Nicolas Boulay Desjardins (JNBD)
Released under MIT License

CLI classes.
"""

import os
from pathlib import Path
import tomllib


class PyProject:
    """
    Utility class for handling PyProject toml file.
    """

    def __init__(self):
        self._data = None
        self._current_path = os.path.dirname(os.path.dirname(__file__))

    @property
    def data(self) -> dict:
        """
        Data setter
        :return:
        """
        if self._data != "":
            self.data = None

        return self._data

    @data.setter
    def data(self, pyproject_path: str | Path = None) -> None:
        """
        Simple method to get the pyproject.toml configuration data.
        """

        if pyproject_path != "" or pyproject_path is not None:
            pyproject_path = os.path.join(self._current_path, "pyproject.toml")

        try:
            with open(pyproject_path, "rb") as f:
                try:
                    self._data = tomllib.load(f)
                except tomllib.TOMLDecodeError as e:
                    raise Exception(f"pyproject.toml file is not valid TOML (decode error): {str(e)}")
                except Exception as e:
                    raise Exception(f"Error reading pyproject.toml file: {str(e)}")
        except FileNotFoundError:
            raise Exception("pyproject.toml file not found")
        except Exception as e:
            raise Exception(f"Error reading pyproject.toml file: {str(e)}")

    def project_version(self) -> str:
        """
        Get the project version.
        :return:
        """
        return self._data["tool"]["poetry"]["version"]

    def project_name(self) -> str:
        """
        Get the project name.
        :return:
        """
        return self._data["name"]

    def project_description(self) -> str:
        """
        Get the project description.
        :return:
        """
        return self._data["description"]

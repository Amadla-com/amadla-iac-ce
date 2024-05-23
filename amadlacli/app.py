"""
Amadla CLI

(C) 2024 Amadla. All rights reserved.
Released under MIT License
"""

import tomllib

try:
    with open("pyproject.toml", "rb") as f:
        try:
            project_data = tomllib.load(f)
        except tomllib.TOMLDecodeError as e:
            raise Exception(f"pyproject.toml file is not valid TOML (decode error): {str(e)}")
        except Exception as e:
            raise Exception(f"Error reading pyproject.toml file: {str(e)}")
except FileNotFoundError:
    raise Exception("pyproject.toml file not found")
except Exception as e:
    raise Exception(f"Error reading pyproject.toml file: {str(e)}")

__version__ = project_data["tool"]["poetry"]["version"]


class APP:
    """
    Class that has the application information and details.
    """

    def __init__(self) -> None:
        self.metadata = project_data["tool"]["poetry"]

    def name(self) -> str:
        """
        Get application name.
        """
        return self.metadata["name"]

    @staticmethod
    def version() -> str:
        """
        Get application version.
        """
        return __version__

    def description(self):
        """
        Application description.
        """
        return self.metadata["description"]
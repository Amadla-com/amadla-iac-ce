# Configuration file for the Sphinx documentation builder.

# -- Project information

import os
import tomllib
import subprocess


def get_contributors(directory):
    git_command = ['git', 'log', '--pretty=format:%an', f'-- {directory}']
    result = subprocess.run(git_command, capture_output=True, text=True)
    contributors = set(result.stdout.splitlines())
    return contributors


def extract_copyright(filename):
    with open(filename) as f:
        for line in f:
            if "Copyright" in line:
                return line.strip()
    return None


def get_short_version(long_version: str):
    parts = long_version.split('.')
    if len(parts) >= 2:
        return '.'.join(parts[:2])
    else:
        return long_version


project_root = os.path.dirname(os.path.dirname(__file__))
pyproject_path = os.path.join(project_root, "../pyproject.toml")



metadata = project_data["tool"]["poetry"]
project = metadata["title"]
copyright = extract_copyright('../LICENSE')
author = ', '.join(get_contributors('docs/'))

# - version: This is a shorter, "quick reference" version of your project,
#   which usually omits smaller point-level details. For example, if your project's full version is '1.3.4',
#   the version might just be '1.3'.
# - release: This is the full version string of your project, including alpha/beta/rc tags.
#   Continuing the previous example, the release would be '1.3.4'.
#
# In the pyproject.toml file, the [tool.poetry] section only has a version field,
# which corresponds to the full version of your project, similar to the release field in Sphinx's conf.py.
# The version in pyproject.toml typically follows the format of MAJOR.MINOR.PATCH, for example '1.3.4',
# and can also include identifiers for pre-release and build metadata.
#
# For more information about Sphinx versioning see:
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-version
release = metadata["version"]
version = get_short_version(metadata["version"])

language = 'en'
languages = ['en', 'fr']

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.githubpages',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

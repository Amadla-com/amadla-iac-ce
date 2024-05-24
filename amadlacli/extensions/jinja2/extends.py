"""
Amadla cli.

(C) 2024 Jean-Nicolas Boulay Desjardins (JNBD)
Released under MIT License

CLI classes.
"""

from jinja2 import nodes
from jinja2.ext import Extension


class AmadlaExtendsExtension(Extension):
    """
    amadla_extends Jinja2 tag
    """
    tags = {'amadla_extends'}

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        template_name = parser.parse_expression()
        return nodes.Extends(template_name, lineno=lineno)


class UrlExtendsExtension(Extension):
    """
    url_extends Jinja2 tag
    """
    tags = {'url_extends'}

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        template_url = parser.parse_expression()
        return nodes.Extends(template_url, lineno=lineno)

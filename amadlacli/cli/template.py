"""
Amadla cli.

(C) 2024 Jean-Nicolas Boulay Desjardins (JNBD)
Released under MIT License

CLI classes.
"""

import click


class TemplateCli:
    """
    Schema utilities
    """

    @click.group()
    @click.pass_context
    def template(self, ctx):
        """
        Schema utilities
        """
        pass

    @template.command()
    @click.pass_context
    def validate(self, ctx):
        """
        Validate schemas
        """
        click.echo("Schema validated.")

    @template.command()
    @click.pass_context
    def generate(self, ctx):
        """
        Generate schema
        """
        click.echo("Schema generated.")


template_cli = TemplateCli()

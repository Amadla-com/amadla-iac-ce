"""
Amadla cli.

(C) 2024 Jean-Nicolas Boulay Desjardins (JNBD)
Released under MIT License

CLI classes.
"""

import click


class SchemaCli:
    """
    Schema utilities
    """

    @click.group()
    @click.pass_context
    def schema(self, ctx):
        """
        Schema utilities
        """
        pass

    @schema.command()
    @click.pass_context
    def validate(self, ctx):
        """
        Validate schemas
        """
        click.echo("Schema validated.")

    @schema.command()
    @click.pass_context
    def generate(self, ctx):
        """
        Generate schema
        """
        click.echo("Schema generated.")


schema_cli = SchemaCli()

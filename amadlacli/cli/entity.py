"""
Amadla cli.

(C) 2024 Jean-Nicolas Boulay Desjardins (JNBD)
Released under MIT License

CLI classes.
"""

import click


class EntityCli:
    """
    Schema utilities
    """

    @click.group()
    @click.pass_context
    def entity(self, ctx):
        """
        Schema utilities
        """
        pass

    @entity.command()
    @click.pass_context
    def validate(self, ctx):
        """
        Validate schemas
        """
        click.echo("Schema validated.")

    @entity.command()
    @click.pass_context
    def generate(self, ctx):
        """
        Generate schema
        """
        click.echo("Schema generated.")


entity_cli = EntityCli()


import click


class RegisterReaderOption(click.Option):
    """
    Mark this option as getting a _set option.
    :param click.Option:
    """

    register_reader = True


class RegisterWriterOption(click.Option):
    """
    Fix the help for the _set suffix.
    :param click.Option:
    """

    def get_help_record(self, ctx) -> tuple[str, str]:
        helper = super(RegisterWriterOption, self).get_help_record(ctx)
        return (helper[0].replace("_set ", "="),) + helper[1:]


class RegisterWriterCommand(click.Command):
    """
    Registrator for writer command.
    :param click.Command:
    """

    def parse_args(self, ctx, args) -> list[str]:
        """
        Translate any opt= to opt_set= as needed.
        :param ctx:
        :param args:
        """
        options = [o for o in ctx.command.params if getattr(o, "register_reader", None)]
        prefixes = {p for p in sum([o.opts for o in options], []) if p.startswith("--")}
        for i, a in enumerate(args):
            a = a.split("=")
            if a[0] in prefixes and len(a) > 1:
                a[0] += "_set"
                args[i] = "=".join(a)

        return super(RegisterWriterCommand, self).parse_args(ctx, args)

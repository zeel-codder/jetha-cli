import click


@click.group("Demo")
def start():
    """This is a basic Click command."""
    print("Hello World!")


@start.command("start_a")
def start_a():
    """This is a basic Click command."""
    print("Hello World A!")

@start.command("start_b")
def start_b():
    """This is a basic Click command."""
    print("Hello World A!")

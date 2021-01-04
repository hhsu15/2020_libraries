import typer

app = typer.Typer()

@app.command()
def hello(name):
    typer.echo(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        typer.echo(f"Goodby Mr.{name}")

    else:
        typer.echo(f"Bye {name}")

if __name__ == "__main__":
    app()


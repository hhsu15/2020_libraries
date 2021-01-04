import typer

def main(name):
    typer.echo(f"hello {name}")


if __name__ == '__main__':
    typer.run(main)

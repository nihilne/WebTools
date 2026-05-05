import click
from app.seeds import run_all


def register_commands(app):
    @app.cli.command("seed")
    def seed_command():
        results = run_all()

        for model, success in results:
            if success:
                click.echo(f"Seeded {model.__tablename__}")
            else:
                click.echo(f"Skipped {model.__tablename__} (data already exists)")

        click.echo("Done!")

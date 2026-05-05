import click
from app.seeds import run_all, all_seeds


def register_commands(app):
    @app.cli.command("seed")
    def seed_command():
        for data, model in all_seeds:
            click.echo(f"Seeding {model.__tablename__}...")
        run_all()
        click.echo("Done!")

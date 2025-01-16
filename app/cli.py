import click
from flask.cli import with_appcontext
from app import db
from flask_migrate import upgrade

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Initialize the database."""
    # Run migrations
    upgrade()
    click.echo('Initialized the database.')
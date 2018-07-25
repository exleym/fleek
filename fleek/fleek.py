import click
from cookiecutter.main import cookiecutter

from fleek.config import Config
from fleek.blueprint import Blueprint

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', type=str)
def new(name: str):
    config = Config()
    cookiecutter(config.template)
    #print(f'Initializing REST API named "{name}" ...')

@cli.group()
def add():
    pass

@add.command()
def model():
    click.echo('adding module ...')

@add.command()
@click.option('--name', type=str)
def blueprint(name: str):
    click.echo('adding blueprint ...')
    blueprint = Blueprint(name=name)
    blueprint.check_if_default()
    click.echo(blueprint)



import click

from generate_fake_data import GenerateFakeData
from utils import Clipboard

gfd = GenerateFakeData()
clipboard = Clipboard()


@click.option("--target", "-t", help="传入要生成的数据名", prompt=True, required=True)
@click.command()
def faker(target: str):
	result = getattr(gfd, target)()
	clipboard.set(result)
	click.echo(result)


if __name__ == '__main__':
	faker()
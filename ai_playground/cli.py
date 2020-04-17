import click
import pprint
from pyfiglet import Figlet
from ai_playground.config.config import Config
from ai_playground.utils.logger import get_logger
from ai_playground.utils.config_parser import load_cfg
logger = get_logger(__name__)


@click.group()
@click.option('--config', help='Training configuration file.')
@click.option('--log2neptune/--no-log2neptune', default=False, help='Choose whether to log to neptune or not.')
@click.pass_context
def main(ctx, config: str, log2neptune: bool):
    figlet = Figlet(font='slant')
    click.echo(figlet.renderText("AI Playground"))
    cfg = load_cfg(config)
    ctx.obj = Config(config=cfg)

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint("Configuration loaded: " + config)
    pp.pprint(ctx.obj.get_config())


@main.command()
@click.pass_context
def train(ctx):
    logger.info("Training")


def start():
    main(obj={})


if __name__ == '__main__':
    start()

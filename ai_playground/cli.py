import click
import pprint
import neptune
from pyfiglet import Figlet
from datetime import datetime

from ai_playground.selfdrive.train import Trainer
from ai_playground.selfdrive.train_haar import SelfDriveAgent
from ai_playground.selfdrive.train_ppo import PPOTrainer
from ai_playground.utils.logger import get_logger
from ai_playground.utils.config_parser import load_cfg

logger = get_logger()


@click.group()
@click.option('--exp_name', required=True, default='exp_' + datetime.now().strftime("%d/%m/%Y_%H:%M:%S"),
              help='The experiment name.')
@click.option('--config', help='Training configuration file.')
@click.option('--log2neptune/--no-log2neptune', default=False, help='Choose whether to log to neptune or not.')
@click.option('-load', '--load_exp', type=str, help='Load experiment from selected dir.')
@click.pass_context
def main(ctx, config: str, log2neptune: bool, exp_name: str, load_exp: bool):
    figlet = Figlet(font='slant')
    click.echo(figlet.renderText("AI Playground"))
    cfg = load_cfg(config)
    ctx.obj['exp_name'] = exp_name
    ctx.obj['config_file'] = config
    ctx.obj['config'] = cfg
    ctx.obj['log2neptune'] = log2neptune
    ctx.obj['load_exp'] = load_exp


@main.command()
@click.pass_context
def train(ctx):
    logger.info("Loaded config: " + ctx.obj['config_file'])
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(dict(ctx.obj['config']))

    logger.info("Starting training")
    sda = PPOTrainer(ctx)
    sda.train()

@main.command()
@click.pass_context
def inference(ctx):
    logger.info("Loaded config: " + ctx.obj['config_file'])
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(dict(ctx.obj['config']))

    logger.info("Starting training")
    sda = PPOTrainer(ctx)
    sda.inference()


def start():
    main(obj={})


if __name__ == '__main__':
    start()

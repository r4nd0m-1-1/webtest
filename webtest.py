import click
from core.engine import ScannerEngine
from utils.config_loader import load_config
from utils.logger import init_logger

@click.command()
@click.option('--target', '-u', help='Target URL')
@click.option('--target-file', '-f', help='File with list of targets')
@click.option('--scan-type', '-s', default='quick', help='Scan type: quick/full/module')
@click.option('--module', help='Specific module to run')
@click.option('--auth', help='Basic auth in format user:pass')
@click.option('--threads', default=5, help='Number of concurrent threads')
@click.option('--output', default='json', help='Output format')
@click.option('--proxy', help='Proxy URL')
@click.option('--verbose', is_flag=True, help='Verbose output')
def main(**kwargs):
    config = load_config("config/default.yaml")
    logger = init_logger(verbose=kwargs['verbose'])
    engine = ScannerEngine(config, logger)
    engine.run(kwargs)

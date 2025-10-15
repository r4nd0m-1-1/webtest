import asyncio
from core.plugins import sqli, xss

class ScannerEngine:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger

    async def run_module(self, module, target):
        if module == "sqli":
            return await sqli.scan(target, self.config)
        elif module == "xss":
            return await xss.scan(target, self.config)

    def run(self, args):
        targets = [args['target']] if args['target'] else open(args['target_file']).read().splitlines()
        loop = asyncio.get_event_loop()
        tasks = [self.run_module(args['module'], t) for t in targets]
        loop.run_until_complete(asyncio.gather(*tasks))

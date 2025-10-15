import schedule
import time
from core.engine import ScannerEngine

def schedule_scan(config, logger, args, interval_minutes=60):
    engine = ScannerEngine(config, logger)
    schedule.every(interval_minutes).minutes.do(lambda: engine.run(args))
    while True:
        schedule.run_pending()
        time.sleep(1)

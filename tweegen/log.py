import time
from loguru import logger
from contextlib import contextmanager


@contextmanager
def log(desc):
    logger.opt(colors=True).debug(f"Service called: <red>{desc}</red>")
    start = time.time()
    try:
        yield
    except:
        logger.opt(colors=True).exception(
            f"Encountered error on service: <red>{desc}</red>"
        )
    finally:
        end = time.time()
        logger.opt(colors=True).debug(
            f"Processing time for <red>{desc}</red>: <green>{end-start}</green> seconds"
        )

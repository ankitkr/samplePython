import logging
import structlog

LOGGER = logging.getLogger(__name__)
logger = structlog.get_logger(__name__)


class TestNew:
    def run(self):
        logger.info("This is second message")
        # logger.warn(result=self.subtract(40, 5))
        # LOGGER.error("Standard 2nd Message Warning")
        self.divide_by_zero()

    def subtract(self, x, y):
        # logger.debug("Value of x = {}".format(x))
        # logger.debug("Value of y = {}".format(y))
        return x - y

    def divide_by_zero(self):
        return 555/0

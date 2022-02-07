import logging
import requests

LOGGER = logging.getLogger(__name__)


class Test:
    def run(self):
        LOGGER.info("This is first message")
        # LOGGER.warning("result={}".format(self.add(4, 5)))
        # LOGGER.error('StructLog Error')
        self.divide_by_zero()

    def add(self, x, y):
        return x + y

    def divide_by_zero(self):
        r = requests.get('https://api.github.com/user', auth=('user', 'pass'))

        try:
            return 123/0
        except Exception as e:
            LOGGER.exception(e)

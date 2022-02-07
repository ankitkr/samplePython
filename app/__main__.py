from app.test import Test
from app.test_new import TestNew

from redis import Redis
from app.rq_test import count_words_at_url

import sentry_sdk
from structlog_wrapper.python import configure_struct_logging

configure_struct_logging('samplePython', 'python', 'development', log_level='INFO')

sentry_sdk.init(
    "https://f9a2117e2a004002b5f3a7e56aa38de0@o1133234.ingest.sentry.io/6179586",
    traces_sample_rate=1.0
)


if __name__ == '__main__':
    test = Test()
    test.run()
    test.add(3, 4)

    test_new = TestNew()
    test_new.run()

    # q = Queue(connection=Redis())
    # result = q.enqueue(count_words_at_url, 'http://nvie.com')
    count_words_at_url.delay('http://nvie.com')

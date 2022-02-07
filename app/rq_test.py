import requests
import structlog

from redis import Redis

logger = structlog.get_logger(__name__)
from rq_wrapper import Queue
from rq_wrapper import job


redis_queue = Queue(connection=Redis())


@job(queue=redis_queue, timeout=10)
def count_words_at_url(url):
    # logger_std.info("Standard Log")
    # logger.info("Start Word Counting!!")
    resp = requests.get(url)
    sum.delay(10, 55)
    # q = Queue(connection=Redis())
    # result = q.enqueue(count_words_at_url, 'http://nvie.com')
    return len(resp.text.split())


@job(queue=redis_queue, timeout=10)
def sum(a, b):
    222/0
    # logger.info("Summing")
    return a + b



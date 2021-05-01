import logging
import time
import functools
from django.db import reset_queries, connection

logger = logging.getLogger("queries")


def query_debugger(func):
    """
    Optimization working with databases
    """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        reset_queries()

        start_queries = len(connection.queries)

        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()

        end_queries = len(connection.queries)
        logger.info(f"QUERY: {end_queries - start_queries}, TIME: {(end_time - start_time):.2f}s")
        return result

    return wrapped_func

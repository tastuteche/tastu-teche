from contextlib import contextmanager
from timeit import default_timer


@contextmanager
def elapsed_timer():
    start = default_timer()

    # elapser = lambda: default_timer() - start
    last = None
    curr = start

    def elapser():
        nonlocal last, curr
        last = curr
        curr = default_timer()
        return (curr - last, curr - start)
    yield lambda: elapser()

    end = default_timer()

    def elapser(): return (end - start, end - start)

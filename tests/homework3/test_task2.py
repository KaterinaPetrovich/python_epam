import time

from homework3.task2 import calculate_500


def test_working_time_calculate_500():
    start = time.time()
    calculate_500()
    assert time.time()-start < 60

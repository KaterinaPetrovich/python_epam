import concurrent.futures
import hashlib
import random
import struct
import time


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


def calculate_500():
    with concurrent.futures.ProcessPoolExecutor(max_workers=50) as ex:
        ex.map(slow_calculate, [x for x in range(500)])

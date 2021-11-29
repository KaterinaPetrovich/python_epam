import sys


def my_precious_logger(text: str):
    if text[:5] == "error":
        sys.stderr.write(text)
    else:
        sys.stdout.write(text)

import glob
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    file_list = glob.glob(f"{dir_path}*.{file_extension}")
    counter = 0
    for file in file_list:
        with open(file) as fp:
            for line in fp:
                counter += len(tokenizer(line)) if tokenizer else 1
    return counter

"""Logger."""

import sys
import logging


def get_logger():
    """Init logger configuration."""

    level = logging.INFO

    formatter = logging.Formatter("%(asctime)s - "
                                  "%(name)s - "
                                  "%(funcName)s"
                                  "(%(lineno)d) - %(message)s")

    root = logging.getLogger()
    root.setLevel(level)

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(level)
    stdout_handler.setFormatter(formatter)

    file_handler = logging.FileHandler('../proxy-logs.log')
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)

    root.addHandler(stdout_handler)
    root.addHandler(file_handler)

    return root

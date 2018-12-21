#!/usr/bin/env python3

"""atman.py : The beginning."""

import argparse
import logging
import sys

from lib.samsara import ExternalConnector


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Alien Setup')
    parser.add_argument("--verbose", "-v", action="store_true")
    parser.add_argument("--log_file", "-lf", default=None, help="Set path to save log output")
    args = parser.parse_args()

    # --------------- Logging setup ---------------------
    logger = logging.getLogger("alien")

    if args.log_file:
        log_file_handler = logging.FileHandler(args.log_file)
        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
        log_file_handler.setFormatter(formatter)
        logger.addHandler(log_file_handler)

    stdout_handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(stdout_handler)

    if args.verbose:
        logger.setLevel(level=logging.DEBUG)
    else:
        logger.setLevel(level=logging.INFO)

    world_events_listener = ExternalConnector()
    world_events_listener.start()
    world_events_listener.join()

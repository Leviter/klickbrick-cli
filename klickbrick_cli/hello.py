#!/usr/bin/env python3
"""
Author: Marcel van den Brink <marcel.vandenbrink@gmail.com>
Purpose: Say hello
"""

import argparse
import sys


def get_args():
    """Get the command-line arguments"""

    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='name', help='name to greet')
    return parser.parse_args()


def main():
    if not len(sys.argv) > 1:
        print('hello world')
    else:
        args = get_args()
        print('hello ' + args.name)


if __name__ == '__main__':
    main()

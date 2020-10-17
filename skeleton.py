# -*- coding: utf-8 -*-
"""This module ..."""

import argparse
import sys


def get_args():
    """
    Parse command line arguments.
    """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '--smiley', '-s',
        help='smiley added',
        type=str,
        default=':)')
    
    return parser.parse_args()

def main():
    """Main."""

    # CLI args
    args = get_args()

    # stdin -> stdout identity filter
    for line in sys.stdin:
        print(f'{line.strip()} {args.smiley}')

if __name__ == '__main__':
    main()

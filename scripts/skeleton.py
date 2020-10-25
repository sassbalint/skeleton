"""
This is a skeleton module
intended to be a good starting point for any python script.
(Write a useful global docstring here.)
"""

import argparse
import sys


def skeleton(text, smiley):
    """
    Do the thing.
    (Rename this function to something meaningful.)
    (Write a useful docstring for every function.)
    """
    return f'{text} {smiley}'


def main():
    """Main. A simple stdin -> stdout filter."""
    # get CLI arguments
    args = get_args()

    # stdin -> stdout identity filter
    for line in sys.stdin:
        print(skeleton(line.strip(), args.smiley))


def get_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '--smiley', '-s',
        help='add smiley',
        type=str,
        default=':)')
    
    return parser.parse_args()


if __name__ == '__main__':
    main()

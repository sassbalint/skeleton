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
    # ... as a dict!
    args_dict = vars(args)

    # stdin -> stdout identity filter
    for line in sys.stdin:
        result = skeleton(line.strip(), args.smiley)
        print(result)
        if args.duplicate:
            print(result)


def get_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    # string-valued argument
    parser.add_argument(
        '-s', '--smiley',
        help='add smiley',
        type=str,
        default=':)'
    )
    # boolean argument: True if present, False if not present
    parser.add_argument(
        '-d', '--duplicate',
        help='do something twice',
        action='store_true'
    )
    
    return parser.parse_args()


if __name__ == '__main__':
    main()

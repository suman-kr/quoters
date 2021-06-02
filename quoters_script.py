#! /usr/bin/env python3

import sys
from quoters import main as quoters


def main():
    try:
        print(quoters.Quote().print(True))
        return 0
    except:
        return 1


if __name__ == "__main__":
    sys.exit(main())

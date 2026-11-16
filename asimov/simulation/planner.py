"""Example untrusted request generator, with stdout as its only output."""

import sys


if __name__ == "__main__":
    sys.stdout.buffer.write(b"+\n" * 11 + b"999\n-\n")

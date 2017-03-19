#!/usr/local/bin/python3
import sys

while True:
    c = sys.stdin.read(1)
    if not c: break
    sys.stdout.write(c)
    sys.stdout.flush()
    if c == '~':
        sys.stderr.write("\b \b")
    else:
        sys.stderr.write(c)
    sys.stderr.flush()

print("")
sys.stderr.write("\n")

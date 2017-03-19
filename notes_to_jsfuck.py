#! /usr/local/bin/python3

import sys

def handle_note(note):
    print('[') # TODO: output real JSFuck.

def main():
    for line in sys.stdin:
        note = int(line.strip())
        handle_note(note)

if __name__ == '__main__':
    main()

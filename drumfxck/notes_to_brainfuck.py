#! /usr/local/bin/python3

import sys

note_to_symbol_map = {48: ">", 47: "<", 38: "+", 37: "-", 51: ".", 42: ",", 49: "[", 52: "]", 43: "~"}

def handle_note(note):
    if note in note_to_symbol_map:
        print(note_to_symbol_map[note], end='')
        sys.stdout.flush()

def main():
    for line in sys.stdin:
        note = int(line.strip())
        handle_note(note)

if __name__ == '__main__':
    main()

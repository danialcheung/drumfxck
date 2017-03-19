#! /usr/local/bin/python3

import sys

# TODO: check note_to_symbol_map
note_to_symbol_map = {0: ">", 1: "<", 2: "+", 3: "-", 4: ".", 5: ",", 6: "[", 7: "]", 8: "~"}

def handle_note(note):
    print(note_to_symbol_map[note])

def main():
    for line in sys.stdin:
        note = int(line.strip())
        handle_note(note)

if __name__ == '__main__':
    main()

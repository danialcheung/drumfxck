#! /usr/local/bin/python3

import sys

note_to_symbol_map = {
    48: ">", # Hi Tom
    47: "<", # Low-Mid Tom
    38: "+", # Snare
    37: "-", # Side Stick/Rim Shot
    51: ".", # Ride Cymbal 1
    42: ",", # Hi Hat
    49: "[", # Crash Cymbal 1
    52: "]", # Chinese Cymbal
    43: "~"  # Floor Tom
}

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

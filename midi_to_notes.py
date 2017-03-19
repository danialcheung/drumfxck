#! /usr/local/bin/python3

import mido
import sys

def handle_note(note):
    print(note)
    sys.stdout.flush()

def handle_message(message):
    message_dict = message.dict()
    if message_dict['type'] == 'note_on':
        note = message_dict['note']
        handle_note(note)

def main():
    with mido.open_input() as port:
        for message in port:
            handle_message(message)

if __name__ == '__main__':
    main()

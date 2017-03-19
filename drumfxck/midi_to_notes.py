#! /usr/local/bin/python3

import mido
import sys

def handle_note(note):
    if note == 53:
        raise EOFError
    print(note)
    sys.stdout.flush()

def handle_message(message):
    message_dict = message.dict()
    if message_dict['type'] == 'note_on' and message_dict['velocity'] != 0:
        note = message_dict['note']
        handle_note(note)

def main():
    try:
        with mido.open_input('UM-ONE') as port:
            for message in port:
                handle_message(message)
    except Exception as e:
        pass

if __name__ == '__main__':
    main()

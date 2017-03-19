# Drumfxck
### Drumfxck: the drumming based programming language.

A collection of programs that combine to process MIDI input as [Brainfuck](https://en.wikipedia.org/wiki/Brainfuck), interpret it, and use the interpreter execution as input into an audio/visual output.

##### drumfxck/midi_to_notes.py
Script to read input from the first attached MIDI instrument. Depends on the Python [mido](https://mido.readthedocs.io/en/latest/) library, installable via pip.

Note that if there are problems getting input, check to see that the desired device is listed when mido.get_input

##### drumfxck/notes_to_brainfuck.py
Script to read processed notes



```
./midi_to_notes.py | ./notes_to_brainfuck.py | python3 feedback.py | ../bf 10 | drumfxck-play
```

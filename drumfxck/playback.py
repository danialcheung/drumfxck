import simpleaudio as _simpleaudio
import numpy as _np
import sys as _sys
from collections import namedtuple

PlusOp = namedtuple('PlusOp', ['instruction', 'pc', 'imem', 'mem'])
MinusOp = namedtuple('MinusOp', ['instruction', 'pc', 'imem', 'mem'])
LtOp = namedtuple('LtOp', ['instruction', 'pc', 'imem', 'mem'])
GtOp = namedtuple('GtOp', ['instruction', 'pc', 'imem', 'mem'])
LbrOp = namedtuple('LbrOp', ['instruction', 'pc', 'imem', 'mem', 'taken'])
RbrOp = namedtuple('RbrOp', ['instruction', 'pc', 'imem', 'mem', 'nextpc'])
DotOp = namedtuple('DotOp', ['instruction', 'pc', 'imem', 'mem', 'output'])
CommaOp = namedtuple('CommaOp', ['instruction', 'pc', 'imem', 'mem'])

BF_OPS = {
    '+': PlusOp,
    '-': MinusOp,
    '<': LtOp,
    '>': GtOp,
    '[': LbrOp,
    ']': RbrOp,
    '.': DotOp,
    ',': CommaOp,
}

sample_rate = 44100

def make_note(freq, time=1):
    t = _np.linspace(0, time, time * sample_rate, False)
    return _np.sin(freq * t * 2 * _np.pi)

BF_SOUNDS = {
    '+': make_note(440),
    '-': make_note(440*2),
    '<': make_note(440*1.5),
    '>': make_note(440*0.75),
    '[': make_note(440*1.25),
    ']': make_note(440*1.75),
    '.': make_note(440*2.5),
    ',': make_note(440*2.25),
}

def play_sound(audio):
    return _simpleaudio.play_buffer((audio * 32767 / _np.max(_np.abs(audio))).astype(_np.int16), 1, 2, sample_rate)

def parse_operation(operation):
    s = operation.split(' ')
    if len(s) < 4: return None
    instruction, pc, imem, mem, *rest = s
    args = {
        'instruction': instruction,
        'pc': pc,
        'imem': imem,
        'mem': mem,
    }
    if instruction == '[':
        args['taken'] = rest[0] == '-'
    elif instruction == ']':
        args['nextpc'] = rest[0]
    elif instruction == '.':
        args['output'] = rest[0]
    if instruction not in BF_OPS: return None
    return BF_OPS[instruction](**args)

def operation_parser(lines):
    for line in lines:
        op = parse_operation(line)
        if op is not None:
            yield op

def play(ops):
    s = None
    for op in ops:
        if s is not None:
            s.stop()
        s = play_sound(BF_SOUNDS[op.instruction])

def main():
    try:
        play(operation_parser(_sys.stdin))
    except KeyboardInterrupt:
        pass

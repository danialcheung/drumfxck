#!/usr/bin/env python3
# https://www.pygame.org/docs/tut/MoveIt.html
import os
import queue
import threading

import pygame
import sys

#from .playback import parse_operation

SCREEN_WIDTH = 800 # 1366
SCREEN_HEIGHT = int(800 * (9.0/16.0)) # 768


def main():
    ASSETS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'frames')

    FRAME_COUNTS = {
        'bass': 2,
        'cymbal1': 2,
        'cymbal2': 2,
        'hihat': 2,
        'idle': 13,
        'snare': 2,
        'tomtom1': 2,
        'tomtom2': 2,
        'tomtom3': 2,
    }

    FRAME_FILEPATHS = {
        frame_type:
            [os.path.join(ASSETS_DIR, frame_type + '-' + str(i) + '.png') for i in range(0, frame_count)]
        for frame_type, frame_count in FRAME_COUNTS.items()
        }

    FRAMES = {
        frame_type:
            [pygame.transform.scale(pygame.image.load(path), (SCREEN_WIDTH, SCREEN_HEIGHT))
             for path in frame_filepaths]
        for frame_type, frame_filepaths in FRAME_FILEPATHS.items()
        }

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # start at the idle state's first frame
    state = 'idle'
    state_counter = 0
    clock = pygame.time.Clock()
    event_queue = queue.Queue()

    def input_reader_thread():
        #for line in sys.stdin:
        while True:
            sys.stdin.flush()
            c = sys.stdin.read(1)
            if c is None:
                sys.stdout.write("\n")
                sys.stdout.flush()
                sys.stdout.close()
                break

            sys.stdout.write(c)
            sys.stdout.flush()
            event_queue.put(c)
            #op = parse_operation(c)
            #sys.stderr.write("OP={}\n".format(op))
            #if op is not None:
                #event_queue.put(op.instruction)

    threading.Thread(target=input_reader_thread, daemon=True).start()

    def reset_state(state_name):
        nonlocal state, state_counter
        state = state_name
        state_counter = 0

    while True:
        # loop the current state
        if state_counter+1 < FRAME_COUNTS[state]:
            state_counter += 1
        elif state == 'idle':
            state_counter = 0
        else:
            reset_state('idle')

        while True:
            try:
                queued_event = event_queue.get_nowait()
                if queued_event is not None:
                    if queued_event == '~':
                        reset_state('tomtom3')
                    elif queued_event == '.':
                        reset_state('cymbal1')
                    elif queued_event == '[':
                        reset_state('cymbal2')
                    elif queued_event == ',':
                        reset_state('hihat')
                    elif queued_event == '+':
                        reset_state('snare')
                    elif queued_event == ']':
                        reset_state('cymbal1')
                    elif queued_event == '<':
                        reset_state('tomtom2')
                    elif queued_event == '>':
                        reset_state('tomtom1')
                    elif queued_event == '9':
                        reset_state('idle')

            except queue.Empty:
                break

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    reset_state('bass')
                elif event.key == pygame.K_2:
                    reset_state('cymbal1')
                elif event.key == pygame.K_3:
                    reset_state('cymbal2')
                elif event.key == pygame.K_4:
                    reset_state('hihat')
                elif event.key == pygame.K_5:
                    reset_state('snare')
                elif event.key == pygame.K_6:
                    reset_state('tomtom1')
                elif event.key == pygame.K_7:
                    reset_state('tomtom2')
                elif event.key == pygame.K_8:
                    reset_state('tomtom3')
                elif event.key == pygame.K_9:
                    reset_state('idle')

            elif event.type == pygame.QUIT:
                sys.exit()

        screen.blit(FRAMES[state][state_counter], (0,0))
        pygame.display.update()
        # lock FPS to 24
        clock.tick(24)

if __name__ == '__main__':
    main()

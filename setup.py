from setuptools import setup, find_packages

setup(
    name='drumfxck',
    version='0.1',
    install_requires=['simpleaudio', 'numpy', 'mido'],
    packages=['drumfxck'],
    entry_points={
        'console_scripts': [
            'drumfxck-play = drumfxck:run_play',
        ]
    }
)

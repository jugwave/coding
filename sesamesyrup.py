import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("You've had a long list of lovers,", 0.1),
        ("But none of them matter to you except me", 0.12),
        ("I've had a long list of lovers,", 0.1),
        ("But none of them matter to me except you", 0.12),
        ("Sesame syrup,", 0.08),
        ("I heard it a long time ago", 0.1)
    ]
    delays = [0.3, 5.0, 10.0, 14.5, 20.0, 24.

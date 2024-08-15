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
        ("But none of them matter to you except me", 0.1),
        ("I've had a long list of lovers,", 0.1),
        ("But none of them matter to me except you", 0.1),
        ("Sesame syrup,", 0.2),
        ("I heard it a long time ago", 0.1)
    ]
    delays = [0.3, 5.0, 10.0, 15.0, 20.3, 25.0]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()

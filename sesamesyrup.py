import time
import queue
import threading

def animate_text(text_queue, delay=0.1):
    while True:
        try:
            char = text_queue.get(timeout=0.01)
            if char is None:
                break
            print(char, end='', flush=True)
            time.sleep(delay)
        except queue.Empty:
            pass

def sing_lyric(lyric, delay, speed, text_queue):
    time.sleep(delay)
    for char in lyric:
        text_queue.put(char)
    text_queue.put(None)  # Signal end of lyric

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

    text_queue = queue.Queue()
    animator = threading.Thread(target=animate_text, args=(text_queue,))
    animator.start()

    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = threading.Thread(target=sing_lyric, args=(lyric, delays[i], speed, text_queue))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()
    animator.join()

if __name__ == "__main__":
    sing_song()

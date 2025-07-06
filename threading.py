
#Threading allows your program to perform multiple tasks at once. For example, downloading files while showing a progress bar.

#Basic Example

import threading
import time

def say_hello():
    for i in range(5):
        print("Hello")
        time.sleep(1)

def say_world():
    for i in range(5):
        print("World")
        time.sleep(1)

# Create two threads
thread1 = threading.Thread(target=say_hello)
thread2 = threading.Thread(target=say_world)

# Start threads
thread1.start()
thread2.start()

# Wait for both to finish
thread1.join()
thread2.join()

print("Done!")

# When do we use threading?
# You want to do I/O tasks at the same time (network calls, file reads, user input).

# You want to avoid blocking the main program while doing background tasks.

# Threads in Python do not run in parallel for CPU-heavy work due to the Global Interpreter Lock (GIL). For CPU-heavy tasks, consider using multiprocessing.

# You can also pass arguments to a thread:


def greet(name):
    print(f"Hello, {name}!")

thread = threading.Thread(target=greet, args=("Matheus",))
thread.start()
thread.join()
🔹 5. Using a Thread Class (Advanced Style)

class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            print(f"Running in thread: {self.name}")
            time.sleep(1)

t = MyThread()
t.start()
t.join()

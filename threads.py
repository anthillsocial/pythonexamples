#!/bin/pyhton
# Use ctr+c to stop the script as threads can remain open in the background.
# If unsure, kill all processes from the commandline:
#   $ killall threads.py
# Or search for open processes with: 
#   $ ps aux | grep threads.py
# And kill the process ids: 
#   $ kill -9 12345

import time, threading

def startthreads():
    variable = 1234
    threading.Thread(target=function1).start()
    threading.Thread(target=function2, args=(12345,)).start()

# Start a thread
def function1():
    while True:
        print('Run function 1')
        time.sleep(1)

# Thread started with a passed variable
def function2(a):
    while True:
        print('run function 2: {}'.format(a))
        time.sleep(0.5)

# Start the example
startthreads()



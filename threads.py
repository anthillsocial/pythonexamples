#!/bin/pyhton
# Be sure to kill all processes from the commandline: killall threads.py
# As threads can remain open in the background
# i.e use ctr+c to stop the script
# Or search for open threads with: ps aux | grep threads.py
# The kill the process ids: kill -9 12345

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



# Definition
# Threading is a technique that allows a program to run multiple tasks (threads) concurrently within the same process.
# A thread is the smallest unit of execution inside a process.
# Why Use Threading? Perform multiple tasks simultaneously. Improve responsiveness of applications. Useful for I/O operations such as file handling, downloading files, network requests, etc.

import threading

def task1():
    for i in range(3):
        print("Task 1 is running")

def task2():
    for i in range(3):
        print("Task 2 is running")

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()



# 54)Threading with classes

from threading import Thread
from time import sleep

class A(Thread):
  def run(self):
    for i in range(5):
      print("Nashik")
      sleep(5)

class B(Thread):
   def run(self):
    for i in range(5):
      print("Pune")
      sleep(5)


t1=A()
t2=B()

t1.start()
t2.start()

t1.join()
t2.join()




# 55)Download Multiple files simultaniously by b threading
import threading
import time

def download_file(file):
    print("Downloading", file)
    time.sleep(2)      # use sleep to give outpoot slowly
    print(file, "Downloaded")

t1 = threading.Thread(target=download_file, args=("file1.pdf",))
t2 = threading.Thread(target=download_file, args=("file2.pdf",))
t3 = threading.Thread(target=download_file, args=("file3.pdf",))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

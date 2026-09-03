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



# 56)Is oveloading is supported in python
# Python does not support Method Overloading directly like C++ or Java.
# In Python, if multiple methods with the same name are defined in a class, the last definition overrides the previous ones.


class addition:
    def add(self,a):
       print("Addition of 1 number:",a)

    def add(self,a,b):
       print("Addition of 2 numbers:",a+b)

d = addition()
d.add(10,20)  # This will call the second add method
# output: Addition of 2 numbers: 30



# 58)what is and Is python support overriding
# Method Overriding occurs when a child class provides its own implementation of a method that is already defined in the parent class.
# The method in the child class overrides the method of the parent class.
# Yes, Python Supports Method Overriding ✅

class Parent:
    def show(self):
        print("Parent Class Method")

class Child(Parent):
    def show(self):
        print("Child Class Method")

c = Child()
c.show()



# 59)what is Inheritance
# Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (called the child or subclass) to inherit properties and behaviors (methods) from another class (called the parent or superclass). This promotes code reusability and establishes a hierarchical relationship between classes.
# Parent Class (Base Class) → Class whose properties are inherited.
# Child Class (Derived Class) → Class that inherits from the parent class.

class Person:
    def display(self):
        print("I am a Person")

class Student(Person):
    def study(self):
        print("I am Studying")

s = Student()

s.display()
s.study()



# 60)what is type of Inheritance
class A:
    def show(self):
        print("Class A")

class B(A):
    pass

obj = B()
obj.show()



class A:
    def showA(self):
        print("Class A")

class B:
    def showB(self):
        print("Class B")

class C(A, B):
    pass

obj = C()
obj.showA()
obj.showB()


# 3. Multilevel Inheritance
class A:
    def showA(self):
        print("Class A")

class B(A):
    pass

class C(B):
    pass

obj = C()
obj.showA()



# 4. Hierarchical Inheritance
class A:
    def show(self):
        print("Class A")

class B(A):
    pass

class C(A):
    pass

b = B()
c = C()

b.show()
c.show()
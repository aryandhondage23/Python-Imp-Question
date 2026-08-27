# don't modify current function just add more function in function and add things in it

# basic code of function

def say_hello():
    print("Hello World")

say_hello()

# To use Decorator denote it by "@"
def my_day(say_hello):
    def greet():
        print("Before the function is called.")
        say_hello()
        print("After the function is called.")
    return greet
@my_day
def say_hello():

    print("Hello Team")

say_hello()





# 44) Addition of two num by Decorator
def numbers(func):
    def add()
        a,b = func()
        print("Adition is", a+b)
    return add

@numbers
def get_input():
    a=10
    b=20
    return a,b
get_input()



1)List

Q1)print list with index 1 to -1 and with step 1(by skeeping one)


[ ]
lst = [10, 20, 30, 40, 50, 60, 70]

print(lst[1:-1:2])
[20, 40, 60]
Q2) Difference Beteween Append and incert


[ ]
lst = [1, 2, 3]

lst.append(4)

print(lst)
[1, 2, 3, 4]

[ ]
lst = [1, 2, 3]

lst.insert(1, 10)   # Insert 10 at index 1

print(lst)
[1, 10, 2, 3]

[ ]
lst = [1, 2, 3]

lst.extend([4, 5, 6])

print(lst)
[1, 2, 3, 4, 5, 6]
Q3) average of List


[ ]
lst=[1,4,5,6,7,8]
average=sum(lst)/len(lst)
print(average)
5.166666666666667
Q4) pop remove


[ ]
lst=[1,4,5,6,7]
x=lst.pop()
print(x) #we dont specify the index so it remove last element only
7

[ ]
lst = [10, 20, 30, 40]

x = lst.pop(1)

print("Removed:", x)
Removed: 20
Q5) print list from right to left with step one


[ ]
lst = [1, 3, 2, 4, 6, 0]

print(lst[-1:-7:-2])
[0, 4, 3]
2) Tuple

Q6) how to define empty tuple


[ ]
t = ()
print(t)
()

[ ]
t = ()
print(type(t))
<class 'tuple'>

[ ]
t = (5,)
print(type(t))
<class 'tuple'>

[ ]
t = (5)
print(type(t))# it not consider tuple becuase it not have "," so it show int
<class 'int'>

[ ]
t = (5,)
print(type(t))
<class 'tuple'>
Q7) is it possible to change tuple to list

ans=we can do it forcefully by typecasting means changing it data type

Q8) want find index of value in tuple


[ ]
t = (10, 20, 30, 40, 50)

print(t.index(30))
2

[ ]
# if value not present
t = (10, 20, 30)

print(t.index(50)) # it give error

3) Set

unorder data , set can store diff diff dataset

Q9) how to define set and empty set


[ ]
s = {10, 20, 30, 40}

print(s)
print(type(s))

{40, 10, 20, 30}
<class 'set'>

[ ]
#emptSet
s = set()

print(s)
print(type(s))
set()
<class 'set'>

[ ]
s = {}
print(type(s))
# {} creates an empty dictionary, not an empty set.
<class 'dict'>
discard in set

[ ]
s = {10, 20, 30, 40}

s.discard(20)

print(s)
{40, 10, 30}

[ ]
s = {10, 20, 30}

s.discard(50)

print(s)  #it not show error like remove funtion
{10, 20, 30}
Method	If Element Exists	If Element Does Not Exist
remove()	Removes element	Raises KeyError
discard()	Removes element	No error
Intersection of set
The intersection of two sets contains the elements that are common in both sets.


[ ]
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

result = s1.intersection(s2)

print(result)
{3, 4}

[ ]

{3, 4}

[ ]
# Using & Operator
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print(s1 & s2)
{3, 4}
12)by taking two set make one set (union)


[ ]
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print(s1.union(s2))
{1, 2, 3, 4, 5, 6}

[ ]
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print(s1|s2)
{1, 2, 3, 4, 5, 6}
13)pop operation in set

ans+ it remove randome element becuase it is randome set


[ ]
s = {10, 20, 30, 40}

x = s.pop()

print("Removed:", x)
print("Set:", s)
Removed: 40
Set: {10, 20, 30}

[ ]
s = {"apple", "banana", "mango"}

print(s.pop())
print(s)
banana
{'apple', 'mango'}
Collection	pop() Behavior
List	Removes element at a given index (or last element)
Set	Removes a random element (no index allowed)
14)can set store diff diff dataset

ans=Yes


[ ]
s = {"apple", "banana", "mango",3,4,5,True}
print(s)
{True, 'banana', 3, 4, 5, 'apple', 'mango'}
4) Dictionary

collection of key values, it cannot be changeble. ex- adarcard number of me not changable, in previous version it is unordered but now it is oredered

14)print element of dictionary


[ ]
d = {"name": "Aryan", "age": 20, "city": "Pune"}

print(d)
print(d["age"])
print(d["city"])
{'name': 'Aryan', 'age': 20, 'city': 'Pune'}
20
Pune
15)changine key value in dict


[ ]
d = {"name": "Aryan", "age": 20, "city": "Pune"}

d["name"] = "Rahul"
d["city"] = "Nashik"

print(d)
{'name': 'Rahul', 'age': 20, 'city': 'Nashik'}
16)in value mupletiple dictionary


[ ]
students = {
    1: {"name": "Aryan", "age": 20},
    2: {"name": "Rahul", "age": 21},
    3: {"name": "Rohit", "age": 22}
}

print(students)
{1: {'name': 'Aryan', 'age': 20}, 2: {'name': 'Rahul', 'age': 21}, 3: {'name': 'Rohit', 'age': 22}}

[ ]
d = {"name": ["Aryan", "Rahul", "Rohit"], "age": [20,30,50], "city": "Pune"}

print(d)

{'name': ['Aryan', 'Rahul', 'Rohit'], 'age': [20, 30, 50], 'city': 'Pune'}
5) function

17)with Parameter and without parameter


[ ]
# Function Without Parameters

# A function that does not take any input.

def greet():
    print("Hello World")

greet()
Hello World

[ ]
# Function With Parameters

# A function that takes input values (parameters).

def greet(name):
    print("Hello", name)

greet("Aryan")
Hello Aryan
18)multiple value we can store in function by args (*)

ans= Yes. In Python, *args allows a function to accept multiple values (variable number of arguments).


[ ]
def display(args):
    print(args)

display(10, 20, 30, 40)


[ ]
def display(*args):
    print(args)

display(10, 20, 30, 40)
(10, 20, 30, 40)
19)multiple value store by kwargs (**)

ans= Yes. **kwargs is used to pass multiple keyword arguments to a function. The values are stored as a dictionary.


[ ]
def display(**kwargs):
    print(kwargs)

display(name="Aryan", age=20, city="Pune")
{'name': 'Aryan', 'age': 20, 'city': 'Pune'}
find second highest number in list without using inbuild

[ ]
lst=[1,3,6,8,9]

[ ]
arr = [10, 50, 20, 40, 30]
n = len(arr)

for i in range(n):
    for j in range(i + 1, n):
        if arr[i] < arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

print("Second highest number =", arr[1])

Second highest number = 40
21)Reverse a String without inbuiled function


[ ]
s = "Python"
rev = ""

for i in s:
    rev = i + rev

print("Reversed String =", rev)
Reversed String = nohtyP
22)take string from user and how many vowels in string


[ ]
s = input("Enter a string: ")

count = 0

for ch in s:
    if ch in "aeiouAEIOU":
        count += 1

print("Number of vowels =", count)

[ ]
s = input("Enter String: ")
count = 0

for ch in s:
    if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
        count += 1

print(count)
Enter String: aryan
2
23)convert the upper case into lower case


[ ]
s = input("Enter a string: ")

result = ""

for ch in s:
    if 'A' <= ch <= 'Z':
        result += chr(ord(ch) + 32)
    else:
        result += ch

print("Lowercase String =", result)
Enter a string: ARYAn
Lowercase String = aryan

[ ]
s = input("Enter a string: ")

result = ""

for ch in s:
    if 'a' <= ch <= 'z':
        result += chr(ord(ch) -32 )
    else:
        result += ch

print("Lowercase String =", result)
Enter a string: ayan
Lowercase String = AYAN
24)Fibonaci


[ ]
n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
Enter number of terms: 6
0 1 1 2 3 5 
factorial

[ ]
n = int(input("Enter a number: "))

fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial =", fact)
Enter a number: 3
Factorial = 6
26)remove duplicate from list


[ ]
lst = [1, 2, 3, 2, 4, 1, 5]

new_lst = []

for i in lst:
    if i not in new_lst:
        new_lst.append(i)

print(new_lst)
[1, 2, 3, 4, 5]
27)Global


[ ]
a=10  # global variable
def my_function():
  global a
  b=10+a  # b is local variable
  print(b)

my_function()
print(a)
print(b)#it not give value as 20 beacuse we call local outside of function it directly give error

28)Break, Continue and


[ ]

1
2

[ ]
# 1. break

# break is used to exit the loop immediately.

for i in range(1, 6):
    if i == 3:
        break
    print(i)
1
2

[ ]
#break

for i in range(10):
  if i==5:
    break
print(i)
5

[ ]
# 3. pass

# pass does nothing. It is used as a placeholder when a statement is required syntactically.

for i in range(1, 6):
    if i == 3:
        pass
    print(i)

1
2
3
4
5

[ ]
#without pass
def my_function():
     for i in range(10):
      if i%2==0:
        print(i)
      else:
        print("odd")
my_function()
0
odd
2
odd
4
odd
6
odd
8
odd

[ ]
#Pass

def my_function():
     for i in range(10):
      if i%2==0:
        print(i)
      else:
        pass
my_function()

0
2
4
6
8
29)LAmbda


[ ]
# A lambda function is a small anonymous (nameless) function that can have any number of arguments but only one expression.

# Syntax

lambda arguments : expression

[ ]
add = lambda a, b: a + b

print(add(10, 20))
30

[ ]
square = lambda x: x * x

print(square(5))
25

[ ]
even= lambda x: x%2==0
print(even(5))
False

[ ]
to_lower = lambda ch: chr(ord(ch) + 32) if 'A' <= ch <= 'Z' else ch

print(to_lower('A'))
print(to_lower('H'))
a
h
sort List without using sort function

[ ]
lst = [5, 2, 8, 1, 3]

n = len(lst)

for i in range(n):
    for j in range(i + 1, n):
        if lst[i] > lst[j]:
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp

print(lst)
[1, 2, 3, 5, 8]
31)FizzBuzz

Rules:

If a number is divisible by 3, print "Fizz" If a number is divisible by 5, print "Buzz" If a number is divisible by both 3 and 5, print "FizzBuzz" Otherwise, print the number


[ ]
for i in range(1, 16):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
      print("Fizz")
    elif i%5 == 0:
      print("Buzz")

    else:
      print(i)

1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
32)Palindrome


[ ]
s = input("Enter a string: ")

rev = ""

for i in s:
    rev = i + rev

if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
Enter a string: 121
Palindrome
33)Passward Authentication


[ ]
password= input("Enter your Password: ")
if len(password)>=8 and any(c.isdigit() for c in password):
  print("Password is valid")
else:
  print("Password is not valid")
Enter your Passwordaryan1237
Password is valid
6)File Handling

34)what is file handlingg

35)diff between write mode and read mode

36)Types of File handling Function

37)Weak Key word in File handling

38)**if i open file apend text and forgot to close file at that case what is happening

What can happen? Data may not be written immediately Python uses buffering. Some data may remain in memory and not be saved to the file right away. File remains open The operating system keeps the file handle open. This consumes system resources. Data loss is possible If the program crashes before the buffer is flushed, some appended data may be lost. Python often closes it automatically When the program ends normally, Python usually closes open files and flushes buffers. But you should not rely on this.

39)File handling with "With" function


[ ]
with open("data.txt", "w") as f:
    f.write("Hello Python")

[ ]
with open("data.txt", "r") as f:
    data = f.read()
    print(data)
Hello Python
40)what if try to read & unexisting file and what if in write mode


[ ]
# 1. Read Mode ("r")

# If the file does not exist and you try to open it in read mode, Python raises a FileNotFoundError.

f = open("abc.txt", "r")


[ ]
# 2. Write Mode ("w")

# If the file does not exist, Python creates a new file automatically.

f = open("abc.txt", "w")
f.write("Hello")
f.close()
41)create one file with poem and read line by line


[ ]
# Create and write poem to file
with open("poem.txt", "w") as f:
    f.write("Twinkle Twinkle Little Star\n")
    f.write("How I Wonder What You Are\n")
    f.write("Up Above The World So High\n")
    f.write("Like A Diamond In The Sky\n")

# Read file line by line
with open("poem.txt", "r") as f:
    for line in f:
        print(line, end="")
Twinkle Twinkle Little Star
How I Wonder What You Are
Up Above The World So High
Like A Diamond In The Sky
42)In file there is one string give count of it


[ ]
count = 0

with open("data.txt", "r") as f:
   content=f.read()
   words=content.split()
   print("Total Words: ",len(words))

TotalWords 2
43)How to delete file


[ ]
import os

os.remove("data.txt")

print("File deleted")
File deleted
7)Decoraters imp

domt modify current function just add more function in function and add things in it


[ ]
def say_hello():

  print("hello Team")

say_hello()
hello Team

[ ]
def my_day(say_hello):
  def wrapper():
    print("Before calling Say hello")
    say_hello()
    print("After Calling say Hello")
  return wrapper

@my_day
def say_hello():




# 45)convert lower to upper by decorator
def uppercase_decorator(greet):
    def wrapper():
        result = greet()
        print(result.upper())
    return wrapper

@uppercase_decorator
def greet():
    return "Hello"

greet()





# 46)Multiplication of two number
def multiplication(get_input):
    def wrapper():
        a, b = get_input()
        print("Multiplication is", a * b)
    return wrapper

@multiplication
def get_input():
  a = 10
  b = 5
  return a, b
get_input()




# 47)create decorator that allow a function to execute only if user is login
def login(user):
  def wrapper():
    if(True==user()):
      print("Login Successfull")
    else:
      print("Login Failed")
  return wrapper

@login
def user():
  return False
user()




def login_required(func):
    def wrapper():
        is_logged_in = True

        if is_logged_in:
            func()
        else:
            print("Please login first")
    return wrapper

@login_required
def show_profile():
    print("Welcome to your profile")





def password_required(func):
    def wrapper():
        password = "aryan123"

        if password == "admin123":
            func()
        else:
            print("Wrong Password")
    return wrapper

@password_required
def welcome():
    print("Login Successful")

welcome()






# 48)Create a decorator and accept only positive number
def number(func):
    def wrapper():
        number= -1

        if number > 0:
            func()
        elif number==0:
          print("number is zero")
        else:
            print("number is negative")

    return wrapper

@number
def positive():
    print("Number is Positive")

positive()
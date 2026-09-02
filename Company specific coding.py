#Table of 2
# for i in range(1,11):
#     print(" 2 X ",i,"=",2*i)


#Printing all table from 1-10
# n=int(input("enter the number"))
# for i in range(1, 11):
#   print(n,"x", i, "=", n * i)

# for i in range(1, 11):
#     print("")
#     for j in range(1, 11):
#         print(i, "x", j, "=", i * j,end="\t")


#program to generate and stores all prime number upto given number in list

# primes = []

# for num in range(2, 101):
#     is_prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         primes.append(num)
# print("Prime Numbers:", primes)


#in other way by incramenting
# primes = []
# for num in range(2, 101):      # num = 2 to 100
#     count = 0
#     for i in range(1, num + 1):   # i = 1 to num
#         if num % i == 0:
#             count += 1
#     if count == 2:
#         primes.append(num)
# print("Prime Numbers:", primes)

# sum of digit of given positive number
# n=int(input("Enter the number : "))
# sum=0
# while n>0:
#     digit = n%10
#     sum = sum + digit
#     n=n//10
# print("Sum of Number is : ",sum)     


#Palindrrome
# n=int(input("Enter the number : ")) 
# rev=0
# temp=n
# while n>0:
#     digit=n%10
#     rev=rev*10 + digit
#     n= n//10

# if rev==temp:
#     print("Palindrome")
# else:
#     print("not Palindrome")


#Palindrome with Stack

# n=input("enter the num/str : ")

# stack=[]

# for ch in n:
#     stack.append(ch)

# rev=''
# while len(stack)>0:
#     rev+=stack.pop()


# 7)count of number of vowels in string

# str=input("Enter String : ")

# count=0
# for ch in str:
#     if ch in "aeiouAEIOU":
#         count+=1
# print(count)


# take number N and prints sum of all even number from 1 to N
# n = int(input("Enter a number: "))
# sum = 0
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         sum += i

# print("Sum of even numbers =", sum)
                

#give for target like  nums=[2,7,11,15]  TARGET=9
#by neste loop means 2 for loops
# n = [8, 9, 11, 6]
# target = 17

# for i in range(len(n)):
#     for j in range(i + 1, len(n)):
#         if n[i] + n[j] == target:
#             print("True -","Numbers are:", n[i], n[j])
#             break
    

# by one loop
# n = [8, 9, 11, 6]
# target = 17

# seen = {}

# for num in n:
#     complement = target - num

#     if complement in seen:
#         print("True")
#         print("Numbers are:", complement, num)
#         break

#     seen[num] = True


#return integer where each digit is increment by one

# n = int(input("Enter number: "))

# result = 0
# place = 1
# while n > 0:
#     digit = n % 10
#     digit = digit + 1

#     result = result + digit * place

#     place = place * 10
#     n = n // 10

# print(result)

#to find the longest common prefix sring among array of string and if not then write empty
# strs = ["flower", "flow", "flight"]

# prefix = strs[0]

# for s in strs[1:]:
#     while s[:len(prefix)] != prefix:
#         prefix = prefix[:-1]

#         if prefix == "":
#             break

# print(prefix)


#array of n integer where each value represent height of vertical line drawn that index find two lines that together with x-axis form container that hold most water
# height = [1,8,6,2,5,4,8,3,7]

# max_area = 0

# for i in range(len(height)):
#     for j in range(i + 1, len(height)):
#         area = min(height[i], height[j]) * (j - i)

#         if area > max_area:
#             max_area = area

# print(max_area)


# 12)Program to take input from user and then find square root of it without using Math Function

# n=int(input("Enter number"))

# for i in range(1,n-1):
#     if i*i==n:
#         print("square root of Number is",i)


# n = int(input("Enter number: "))

# found = False

# for i in range(1, n + 1):
#     if i * i == n:
#         print("Square root is", i)
#         found = True
#         break

# if not found:
#     print("Not a perfect square")



# Define Class named Book represents book in library with attribute titile(String), authour(String), year(integer), availible(Boolean) 
# with methods like Constructor and display

# class Book:

#     def __init__(self, title, author, year, available):
#         self.title = title
#         self.author = author
#         self.year = year
#         self.available = available

#     def display(self):
#         print("Title :", self.title)
#         print("Author :", self.author)
#         print("Year :", self.year)

#         if self.available:
#             print("Status : Available")
#         else:
#             print("Status : Not Available")

#         print("...................................................")

# # Create Objects
# obj1 = Book("Python", "Guido", 2020, True)
# obj2 = Book("Java", "James Gosling", 1995, False)
# obj3 = Book("C++", "Bjarne Stroustrup", 1985, True)
# obj4 = Book("Django", "Adrian Holovaty", 2005, False)

# # Store objects in a list
# arrBooks = [obj1, obj2, obj3, obj4]


# for book in arrBooks:
#     book.display()



#To check the which book have height price
# class Book:

#     def __init__(self, title, author, year, price):
#         self.title = title
#         self.author = author
#         self.year = year
#         self.price = price

#     def display(self):
#         print("Title :", self.title)
#         print("Author :", self.author)
#         print("Year :", self.year)
#         print("Price :", self.price)


# obj1 = Book("Python", "Guido", 2020, 500)
# obj2 = Book("Java", "James Gosling", 1995, 700)
# obj3 = Book("C++", "Bjarne", 1985, 600)
# obj4 = Book("Django", "Adrian", 2005, 900)

# arrBooks = [obj1, obj2, obj3, obj4]

# highest = arrBooks[0]

# for book in arrBooks:
#     if book.price > highest.price:
#         highest = book

# print("Book with Highest Price:")
# highest.display()


#Linked List create 5 nodes for linked list stored head and display it

# class Node:

#     def __init__(self, data):
#         self.data = data
#         self.next = None


# # Create 5 nodes
# n1 = Node(10)
# n2 = Node(20)
# n3 = Node(30)
# n4 = Node(40)
# n5 = Node(50)

# # Link nodes
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5

# # Store head
# head = n1
# # Display linked list
# temp = head

# while temp is not None:
#     print(temp.data, end="-")
#     temp = temp.next


# reverse a linked list
# class Node:

#     def __init__(self, data):
#         self.data = data
#         self.next = None


# # Create nodes
# n1 = Node(10)
# n2 = Node(20)
# n3 = Node(30)
# n4 = Node(40)
# n5 = Node(50)

# # Link nodes
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5

# head = n1

# prev = None
# curr = head

# while curr is not None:
#     next_node = curr.next
#     curr.next = prev
#     prev = curr
#     curr = next_node

# head = prev

# temp = head

# while temp:
#     print(temp.data, end=" -> ")
#     temp = temp.next

# print("None")



# Merging two Sorted Linked list

        
        
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# def merge(l1, l2):
#     dummy = Node(0)
#     tail = dummy

# a = Node(10)
# b = Node(20)
# c = Node(30)

# a.next = b
# b.next = c

# d = Node(15)
# e = Node(25)
# f = Node(35)

# d.next = e
# e.next = f
# while l1 and l2:

#         if l1.data < l2.data:
#             tail.next = l1
#             l1 = l1.next
#         else:
#             tail.next = l2
#             l2 = l2.next

#         tail = tail.next

#     if l1:
#         tail.next = l1

#     if l2:
#         tail.next = l2

#     return dummy.next


# head = merge(a, d)

# temp = head




#Removing a duplicate element from sorted linked list


# class Node:

#     def __init__(self, data):
#         self.data = data
#         self.next = None


# n1 = Node(10)
# n2 = Node(20)
# n3 = Node(30)
# n4 = Node(30)
# n5 = Node(20)

# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5

# head = n1
# temp = head
# while temp and temp.next:
#     if temp.data == temp.next.data:
#         temp.next = temp.next.next
        
#     else:
#         temp = temp.next

# temp = head

# while temp:
#     print(temp.data, end=" -> ")
#     temp = temp.next


#valid Parenthesis




#Write program that takes sentence input and prints langest word

# str = input("Enter a sentence: ")
# words = str.split()
# default = words[0]
# for word in words:
#     if len(word) > len(default):
#         default=word
# print("Longest word in sentence : ",default)



# Program to check if number is armstrong or not
# n = int(input("Enter number :"))
# temp=n
# sum = 0
# order = len(str(n))
# while(n > 0):
#     digit = n % 10
#     sum = sum + digit ** order
#     n = n // 10
# print("armstrong sum is :", sum)

# if temp == sum:
#     print("number is armstrong")
# else:
#     print("not Armstrong")



#from given range of an array return(output) only not present in array  
# arr= [1,2,4,5,6,8]
# for i in range(arr[0],arr[-1]+1):
#     if i not in arr:
#         print(i)



#given square matrix return sum of diagonla of matrix and include sum of all elements of the primery diagonal and slement on secondary that are not part of primary diagonal







#write program checks wheather two strkngs are anagrams of each other

# n1 = input("Enter String 1: ")
# n2 = input("Enter String 2: ")

# if sorted(n1) == sorted(n2):
#     print("Anagrams")
# else:
#     print("Not Anagrams")



# average of N numbers
nums = [10, 20, 30, 40, 50]
sum = 0

for i in nums:
    sum += i
print("Average =", sum / len(nums))
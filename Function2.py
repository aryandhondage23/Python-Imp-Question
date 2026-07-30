# 20) find second highest number in list without using inbuild
arr=[10,20,50,30,40]
n=len(arr)

for i in range(n):
    for j in range(i+1,n):
        if arr[i]<arr[j]:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp

print("The second highest number is:", arr[1])  # Output: The second highest number is: 40


# 21)Reverse a String without inbuiled function
def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

print(reverse_string("Hello, World!"))  # Output: !dlroW ,olleH


string = "Hello, World!"
rev=""

for ch in string:
    rev=ch+rev

print("Reverse of String is: ",rev)  # Output: Reverse of String is: !dlroW ,olleH



# 22)take string from user and how many vowels in string

String = input("Enter a string: ")
count=0
for ch in String:
    if ch in "aeiouAEIOU":
        count+=1
        print(ch, "is a vowel")
print("Total number of vowels in the string is:", count) #output: Total number of vowels in the string is: 3 (if user input is "Hello, World!") 



# 23)convert the upper case into lower case
string = input("Enter a string: ")
result="" 

for ch in string:
    if ch.isupper():
        result+=ch.lower()
    else:
        result+=ch

print("String in lower case is:", result)



string = input("Enter a string: ")
result = ""
for ch in string:
    if 'A'<=ch<='Z':
        result+=chr(ord(ch)+32)

print("String in lower case is:", result)


# Lower case to upper case
string = input("Enter a string: ")
result = ""
for ch in string:
    if 'a'<=ch<='z':
        result+=chr(ord(ch)-32)

print("String in upper case is:", result)



# 24)Fibonaci
n=int(input("Enter the number of terms: "))
a=0
b=1

for i in range(n):
    print(a,end='')
    c=a+b
    a=b
    b=c



# 25)Factorial of a number
num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("The factorial of", num, "is", factorial) #output: The factorial of 5 is 120 (if user input is 5)
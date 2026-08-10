# 30)sort List without using sort function
arr=[5, 2, 8, 1, 9]
n=len(arr)

for i in range(n):
    for j in range(i+1,n):
        if arr[i]>arr[j]:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp

print("List after sorting:", arr)  # Output: List after sorting: [1, 2, 5, 8, 9]



# 31)FizzBuzz

# Rules:
# If a number is divisible by 3, print "Fizz"
# If a number is divisible by 5, print "Buzz"
# If a number is divisible by both 3 and 5, print "FizzBuzz"
# Otherwise, print the number

for i in range(1,20):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3 ==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")

    else:
        print(i)



# 32)Palindrome

s=input("enter string")
rev=""

for i in s:
    rev=i+rev

if s==rev:
    print("string is palindrome")
else:   
    print("string is not palindrome")


# 33)Passward Authentication
password= input("Enter your Password: ")
if len(password)>=8 and any(c.isdigit() for c in password):
  print("Password is valid")
else:
  print("Password is not valid")
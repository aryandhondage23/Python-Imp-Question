# 26)remove duplicate from list
lst=[1,2,3,2,4,3,5,1]
new_list=[]

for i in lst:
    if i not in list:
        new_list.append(i)

print("List after removing duplicates:", new_list) #output: List after removing duplicates: [1, 2, 3, 4, 5]




# 27)Global

a=10
def my function():
    global a
    b=10+a
    print(b)
my_function() #output: 20
print(a) #output: 10
print(b) #output: NameError: name 'b' is not defined  




# 28)Break, Continue and Pass

# 1. break
# break is used to exit the loop immediately.
for i in range(6):
    if i==4:
        break
    print(i) #output: 0 1 2 3


# 2.continue
# continue is used to skip the current iteration and move to the next iteration of the loop.
for i in range(6):
    if i==4:
        continue
    print(i) #output: 0 1 2 3 5

# 3. pass
# pass is used as a placeholder for future code. When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.
for i in range(6):
    if i==4:
        pass
    print(i) #output: 0 1 2 3 4 5


#without pass
def my_function():
     for i in range(10):
      if i%2==0:
        print(i)
      else:
        print("odd")
my_function()  #output: 0 odd 2 odd 4 odd 6 odd 8 odd


#pass
def my_function():
     for i in range(10):
      if i%2==0:
        print(i)
      else:
        pass
my_function() # output: 0 2 4 6 8




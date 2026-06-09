# Q1)print list with index 1 to -1 and with step 1(by skeeping one)
lst = [10, 20, 30, 40, 50, 60, 70]

print(lst[1:-1:2])

# Q2) Difference Beteween Append and incert
lst = [1, 2, 3]
lst.append(4)
print(lst)
#

lst = [1, 2, 3]
lst.insert(1, 10)   # Insert 10 at index 1
print(lst)

lst = [1, 2, 3]
lst.extend([4, 5, 6])
print(lst)

# Q3) average of List
lst=[1,4,5,6,7,8]
average=sum(lst)/len(lst)
print(average)

# Q4) pop remove
lst=[1,4,5,6,7]
x=lst.pop()
print(x) #we dont specify the index so it remove last element only


lst = [10, 20, 30, 40]
x = lst.pop(1)
print("Removed:", x)

# Q5) print list from right to left with step one
lst = [1, 3, 2, 4, 6, 0]

print(lst[-1:-7:-2])



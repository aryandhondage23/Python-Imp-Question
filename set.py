# Q9) how to define set and empty set
s = {10, 20, 30, 40}

print(s)
print(type(s))


#emptSet
s = set()

print(s)
print(type(s))

s = {}
print(type(s))
# {} creates an empty dictionary, not an empty set.

# 10) discard in set
s = {10, 20, 30, 40}
s.discard(20)
print(s)


s = {10, 20, 30}
s.discard(50)
print(s)  #it not show error like remove funtion

# Method	If Element Exists	If Element Does Not Exist
# remove()	Removes element	Raises KeyError
# discard()	Removes element	No error

# 11) Intersection of set
# The intersection of two sets contains the elements that are common in both sets.
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
result = s1.intersection(s2)
print(result)


s1 = {1, 2, 3, 4}
s2 = {2, 3, 4, 5}
s3 = {3, 4, 5, 6}
print(s1.intersection(s2, s3))


# Using & Operator
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(s1 & s2)

# 12)by taking two set make one set (union)
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}       
result = s1.union(s2)
print(result)


s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print(s1|s2)

# 13)pop operation in set
# ans+ it remove randome element becuase it is randome set

s = {10, 20, 30, 40}
x = s.pop()
print("Removed:", x)
print("Set:", s)


s = {"apple", "banana", "mango"}
print(s.pop())
print(s)

# 14)can set store diff diff dataset
# ans=Yes, a set can store different types of data, including integers, floats, strings, and even other sets. However, all elements in a set must be immutable (i.e., they cannot be changed after they are created). This means that you cannot have a set that contains mutable types like lists or dictionaries.

s = {"apple", "banana", "mango",3,4,5,True}
print(s)


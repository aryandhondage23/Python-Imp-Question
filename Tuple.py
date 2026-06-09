# Q6) how to define empty tuple
t = ()
print(t)

t = ()
print(type(t))

t = (5,)
print(type(t))

t = (5)
print(type(t))# it not consider tuple becuase it not have "," so it show int

t = (5,)
print(type(t))

# Q7) is it possible to change tuple to list
# ans=we can do it forcefully by typecasting means changing it data type


# Q8) want find index of value in tuple
t = (10, 20, 30, 40, 50)
print(t.index(30))


# if value not present
t = (10, 20, 30)

print(t.index(50)) # it give error


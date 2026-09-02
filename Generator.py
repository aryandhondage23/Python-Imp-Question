# generator is special type of function that alows you to generate a value one at a time instead of returning all at one.
# ex: when i only want 200 bu range is 1000 priviously it give me all 1000 but in generator it give me 200 only for now

# def my_gen():
#     for i in range(1,6):
#         yield i

# g = my_gen()
# for i in g:
#     print(i)



# 49)Even number by generator

def even(n):
    for i in range(n):
        if i%2==0:
            yield i

g = even(10)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g)) 
print(next(g)) # output: 0,2,4,6,8 still it will give error because we have only 5 even numbers in range of 10





# 50)generate a square of a number using generator

def square(n):
    for i in range(n,n+1):
        yield i*i

g = square(5)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# output: 1,4,9,16,25



# 51)take emoloyee id and increse one by one by generator
def employee_id(n):
    for i in range(50,n+1):
        yield i

g = employee_id(60)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
# output: 50,51,52,53



# 52)Fibonachi by generator
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        yield a
        a,b = b,a+b

g = fibonacci(10)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# output: 0,1,1,2,3


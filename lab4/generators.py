#1
def squares_generator(N):
    for i in range(1, N+1):
        yield i ** 2

squares = squares_generator(5)
for square in squares:
    print(square)
print()

#2
def even_generator(n):
    for i in range(n+1):
        if i%2==0:
            yield i

n = int(input("Enter n: "))
even_nums = even_generator(n)
for n in even_nums:
    print(n, end=", ")
print()
print()

#3
def divisibility_generator(n):
    for i in range(n+1):
        if i %3==0 and i%4==0:
            yield i

n = int(input("Enter n: "))
d_nums = divisibility_generator(n)
for n in d_nums:
    print(n, end=" ")
print()
print()

#4
def squares(a,b):
    for i in range(a,b+1):
        yield i**2

square_nums = squares(2,6)
for square in square_nums:
    print(square)
print()

#5
def reversed_generator(n):
    for i in range(n,-1,-1):
        yield i

nums = reversed_generator(5)
for n in nums:
    print(n)

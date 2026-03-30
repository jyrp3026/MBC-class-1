'''
a, b = map(int, input().split())

print(max(a, b))


def ex():
    message = "Hello World"
    print(message)

def please():
    message = "Hello World"
    print(message)

message2 = "Hello"
print(message2)
ex()
please()


message = "Hello World"
print(message)

def ex():
    global message
    message = "Hello"
    print(message)
    
ex()
print(message)


for i in range(2,51,2):
    print(i)
'''
'''
f = open("test.txt", "a")
f.write("김xx\n")
f.write("정xx\n")
f.write("허xx\n")
f.close()


f = open("test.txt", "r")
for line in f:
    print(line, end="")
f.close()

A = input()
for i in A:
    print(i, end=" ")


X = int(input())

N = int(input())

c = []
for i in range(N):
    a, b = map(int, input().split())
    c.append(a * b)

if X == sum(c):
    print("Yes")
else:
    print("No")

    
X = int(input())
N = int(input())

total_price = sum(a * b for _ in range(N) for a, b in [map(int, input().split())])
print("Yes" if total_price == X else "No")

a,b = map(int, input().split())


num = int(input())

def ex():
    print(f"{num} + 10 = {num + 10}")
    print(f"{num} - 10 = {num - 10}")
ex()

a , b = map(int, input().split())
def num1():
    return a + b
def num2():
    if a > b:
        return a - b
    else:
        return b - a
def num3():
    print("두 수의 합 =",num1())
    print("두 수의 차 =",num2())
num3()

num = float(input())

def ex():
    print(f"{num*num*3.14:.2f}")

ex()

class BlackBox:
    pass

b1 = BlackBox()
b1.name = "까망이"
print(b1.name)
print(isinstance(b1, BlackBox))

class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price 
b1 = BlackBox("까망이", 200000)
print(b1.name, b1.price)
b2 = BlackBox("하양이", 100000)
print(b2.name, b2.price)

class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price  
    def mode(self, min):
        print(str(min) +"분 동안 여행 모드 ON")

b1 = BlackBox("까망이", 200000)
b1.mode(20)

name,age = map(str, input().split())
class ex():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"My name is {self.name}.")
        print(f"I am {self.age} years old.")

ex(name, age)

name2,age2 = map(str, input().split())

class ex1():
    print(f"My name is {name2}.")
    print(f"I am {age2} years old.")

ex1()

class ex():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"My name is {self.name}.")
        print(f"I am {self.age} years old.")

name,age = input().split()

ex1 = ex(name, age)

class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price 

    def mode(self, min):
        print(f"{self.name} {min}분 동안 여행 모드 ON")

b1 = BlackBox("까망이", 200000)
b2 = BlackBox("하양이", 100000)

b1.mode(20)
b2.mode(10)
BlackBox.mode(b1, 20)

import random
N, X = map(int, input().split())

A = [1]
A.extend(random.randint(1, N) for i in range(N-1))

for i in A:
    if i < X:
        print(i, end=" ")
        '''


N, X = map(int, input().split())
A = input().split()

res = [x for x in A if int(x)<X]

for i in range(len(A)):
    if int(A[i]) < X:
        print(A[i], end=' ')
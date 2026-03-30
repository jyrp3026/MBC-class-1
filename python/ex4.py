'''num1 = int(input())
num2 = input()

print(num1 * int(num2[2]))
print(num1 * int(num2[1]))
print(num1 * int(num2[0]))
print(num1 * int(num2))

A = int(input())

print(A)'''

#print("5 + 7 = 5 + 7\n""5 + 7 = 12")

#print("꿀꽈배기"*2)

'''A = int(input())
B = int(input())

print(f"{A} + {B} = {A + B}")
print(f"{A} - {B} = {A - B}")
print(f"{A} * {B} = {A * B}")
print(f"{A} / {B} = {A / B}")
print(f"{A} // {B} = {A // B}")
print(f"{A} % {B} = {A % B}")
print(f"{A} ** {B} = {A ** B}")
    
C = int(input())
D = int(input())

print(C,"+",D, "=", C + D) 
print(C,"-",D, "=", C - D) 
print(C,"*",D, "=", C * D) 
print(C,"/",D, "=", C / D) 
print(C,"//",D, "=", C // D) 
print(C,"%",D, "=", C % D) 
print(C,"**",D, "=", C ** D)

E = int(input())
F = int(input())
G = ["+", "-", "*", "/", "//", "%", "**"]

for i in range(7):
    print(E, G[i], F, "=", eval(f"{E} {G[i]} {F}"))


a=input()
b = input()
sign=["+","-","*","/","//","%","**"]
i = 0
while(i < len(sign)):
    hap=f"{a} {sign[i]} {b}"
    result=eval(hap)
    print(f"{hap} = {result})")
    i = i + 1
name = "Kim"; age = 15

print(f"{name} is {age} years old.")

print("5 + 10 =", 5 + 10)

tuple = (1,2,3,4,5,6,7,8,9,10)
(one,two,*aaa) = tuple
print(aaa)


tuple = ("오예스","몽쉘","초코파이")
print(tuple[1])

set1 = {1,2,3,4,5}
set2 = {3,4,4,5,6,7,8}

set1.discard(7)
print(set1)

num1, num2 = map(int, input().split())

print(f"{num1} / {num2} = {num1 //num2} ... {num1 % num2}")

num1, num2, num3 = map(int, input().split())

print(f"sum = {num1 + num2 + num3}")
print(f"avg = {(num1 + num2 + num3) // 3}")

num1 = int(input())
num2 = int(input())

num3 = num1 - 10; num4 = num2 *2 ; num5 = num3+num4

print(f"{num3} + {num4} = {num5}")'''

'''num = []
for i in range(7):
    i = int(input())
    num.append(i)

print( f"{num[0]+2} {num[1]-2} {num[2]*2} {num[3]/2} {num[4]//2} {num[5]%2} {num[6]**2}")

for i in range(7):
    i = int(input())

    print(i+1,end='')

max = 25
weight = 0
item = 3

while weight + item <=max:
    weight +=item
    print('짐추가')
print(f'총 무게는 {weight}입니다')


drama = ['시즌1', '시즌2', '시즌3', '시즌4', '시즌5']

for x in drama:
    if x == '시즌3':
        print("그만보자")
        continue
    print(f"{x} 시청")

for x in range(10):
    if x % 2 ==1:
        continue
    print(x)

for i in range(1,5001):
    print(i,end=' ')

pro = ['JOA-2020','JOA-2021','SIRO-2021', 'SIRO-2022']
rec = []
for p in pro:
    if p.startswith('SIRO'):
        rec.append(p)
print(rec)

num = input()

def pu():
    print(f"{num} 고객님")
    print("만원인디요")

pu()

def ex():
    print('='*25, end='\n')

ex()
print('line 함수를 호출하였습니다.')
print('line 함수를 다시 호출합니다.')
ex()

num = int(input())

def ex():
    print("~!@#$%^&*()_+")

for i in range(num):
    ex()


N, M = map(int,input().split())

def ex():
    print("Hello")

for i in range(N):
    ex()

for i in range(M):
    ex()

def ex():
    print('='*25)

ex()
print('line 함수를 호출하였습니다.')
print('line 함수를 다시 호출합니다.')
ex()


def ex():
    return 15000
ex1 = ex()

print(f"커트 가격은{ex1}입니다.")


def ex(is_vip):
    if is_vip == True:
        return 10000
    else:
        return 15000
ex1 = ex(True)
print(f"커트 가격은 {ex1}입니다")
ex2 = ex(False)
print(f"커트 가격은 {ex2}입니다")

N, M = map(int,input().split())

def ex():
    print("Hello")

for i in range(N):
    ex()
    if N==i+1:
        print("\n")

for i in range(M):
    ex()

def ex(is_vip=False):
    if is_vip == True:
        return 10000
    else:
        return 15000

price1 = ex(True)
print(price1)
price2 = ex()
print(price2)
price3 = ex()
print(price3)
price4 = ex()
print(price4)

def ex(today,*cust):
    print(today)
    for i in cust:
        print(i)

ex("2026년 3월 27일", "나장발")
ex("2026년 3월 27일", "나장발", "나수염")
ex("2026년 3월 27일", "나장발", "나수염", "나김리")
ex("2026년 3월 27일", "나장발", "나수염", "나김리", "나장발")


num = int(input())

if num >= 90:
    print("A")
elif num >= 80:
    print("B")
elif num >= 70:
    print("C")
elif num >= 60:
    print("D")
else:
    print("F")

score = int(input())
print({10:'A', 9:'A', 8:'B', 7:'C', 6:'D'}.get(score // 10, 'F'))

num = int(input())

if num % 4 == 0 and num % 100 != 0 or num % 400 ==0:
    print(1)
else :
    print(0)

'''
N, M = map(int,input().split())

def ex():
    print("Hello")

for i in range(N):
    ex()
    if N==i+1:
        print()

for i in range(M):
    ex()



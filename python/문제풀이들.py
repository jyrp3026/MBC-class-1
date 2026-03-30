'''person = {'이름': ['홍길동', '박준이'], '나이': 30, '성별': '남성'}

print(person['이름'])
print(person['나이'])
print(person)
person['이름'].append('김철수')
print(person)
person.pop('성별')
print(person)

my_list = [1,2,3,4,5]
my_dic = dict.fromkeys(my_list)
print(my_dic)

a = "일요일"
if a == "월요일":
    print("dd")
else:
    print("ddd")
print("ddasdasd")
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

# 9223문제
num = int(input())
if num > 10:
    print("Big")

#9224문제
num = int(input())
print(num)
if num < 0:
    print("MINUS")

#9225문제
num = int(input())
num2 = int(input())
print(num+num2)
if num % 2 == 1:
    print("ODD")
elif num2 % 2 == 1:
    print("ODD")

#9226문제
num1,num2 = map(int, input().split())

if num1 > num2:
    print(f"{num2}\n{num1}")
else:
    print(f"{num1}\n{num2}")

Yc = 0
fo = True
for Yc in range(0,10):
    if fo:
        Yc +=1
        if Yc %2==0:
            print("퇴장")
        else:
            print("안전")

yellow_card=0
foul=True
if foul:
    yellow_card+=1
    if yellow_card==2:
        print('경고 누적 퇴장')
    else:
        print('휴..조심해야지')
else:
    print('반칙이 없네')

min = 4
if min>20:
    print('게임많이')
    if min >40:
        print("ddsa")
else:
    print("ddd")

num1 = int(input())
num2 = int(input())
print(num1+num2)
if num1 % 2 == 1:
    print("ODD")
elif num2 % 2 == 1:
    print("ODD")

for i in range(10):
    print(f"팔 벌려 뛰기{i+1}")

list = ["asd","sdf","dfg\n"]

for i in list:
    print(i)
tuple = ("asd","sdf","dfg\n")

for i in tuple:
    print(i)

person = {'이름':'나나',"나이":7,"키":120,"몸무게":20}

for i in person.values():
    print(i)

for j in person:
    print(j)

for i, j in person.items():
    print(i,j)



for i in range(100):
    print(f"{i+1} ", end="")

print(*range(5,2001,5))


N = int(input())

for i in range(1,N+1):
    print(i)

N = int(input())

for i in range(N,0,-1):
    print(i)

N = int(input())

for i in range(5,N+1):
    print(i)


N = int(input())

for i in range(2,N+1,2):
    print(i, end=" ")

'''

num1 = int(input())
num2 = int(input())

print(f"{num1 - 10} + {num2 * 2} = {(num1-10)+(num2*2)}")
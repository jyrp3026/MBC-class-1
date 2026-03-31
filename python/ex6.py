'''
#정올 9695
class ex():
    def __init__(self, lo, be, ba):
        self.lo = lo
        self.be = be
        self.ba = ba
        print(f"location: {self.lo}")
        print(f"bedrooms: {self.be}")
        print(f"bathrooms: {self.ba}")

lo, be, ba = map(str, input().split())

ex1 = ex(lo,be,ba)

#정올 9696
class ex():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print(self):
        if self.age <= 18:
            print(f"{self.name}({self.age}) : child")
        else:
            print(f"{self.name}({self.age}) : adult")

name, age = map(str, input().split())
name1, age1 = map(str, input().split())

ex1 = ex(name, int(age))
ex2 = ex(name1, int(age1))
ex1.print()
ex2.print()

#정올 9697
class ex():
    def __init__(self, name, age, AB, H):
        self.name = name
        self.age = age
        self.AB = AB
        self.H = H
    def print(self):
        print(f"name:{self.name}, AVG:{round(self.H / self.AB, 3):.3f}, AB:{self.AB}, H:{self.H}")

name, AB, H = map(str, input().split())
name1, AB1, H1 = map(str, input().split())
ex1 = ex(name, 0, int(AB), int(H))
ex1.print()
ex2 = ex(name1, 0, int(AB1), int(H1))
ex2.print()
#---------------
name, age = map(str, input().split())
name1, age1 = map(str, input().split())

ex1 = ex(name, int(age))
ex2 = ex(name1, int(age1))
ex1.print()
ex2.print()
'''
'''class Parent():
    def method_a(self):
        print("method_a")

class Children(Parent):
    def method_b(self):
        super().method_a()
        print("method_b")

p1 = Parent()
p1.method_a()

c1 = Children()
c1.method_a()
c1.method_b()
'''

'''class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class VideoMaker:
    def make(self):
        print("추억용 여행 영상 제작")

class MailSender:
    def send(self):
        print("메일 발송")

class TraverBlackBox(BlackBox, VideoMaker, MailSender):
    def __init__(self, name, price, sd):
        super().__init__(name, price)
        self.sd = sd
    def set_travel_mode(self, min):
        print(str(min) + "분 동안 여행 모드 ON")

class AdvancedTraverBlackBox(TraverBlackBox):
    def set_travel_mode(self, min):
        print(str(min) + "분 동안 여행 모드 ON")
        self.make()
        self.send()


b1 = TraverBlackBox("하양이", 100000, 64)
b1.set_travel_mode(10)
print()
b2 = AdvancedTraverBlackBox("검정이", 200000, 128)
b2.set_travel_mode(15)
'''

#정올 9698
'''class ex9698():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def print(self):
        for i in range(num):
            if num2[i][0] >= Y and num2[i][1] <= P:
                print(num2[i][0], num2[i][1])
num2 = []
num = int(input())
for i in range(num):
    A, B = map(int, input().split())
    num2.append((A, B))
Y, P = map(int, input().split())


ex1 = ex9698(A, B)
ex1.print()
'''

'''
#정올 9351
A = []
for i in range(30):
    B = int(input())
    A.append(B)
    print(A[i], end=' ')
#--- 간단
print(*[int(input()) for _ in range(30)])
'''

char = []

for i in range(9):
    a = int(input())
    char.append(a)
    
if (char[0] + char[1] + char[2] + char[3] + char[4] + char[5] + char[6]) == 100:
        print(f"{char[0]}\n{char[1]}\n{char[2]}\n{char[3]}\n{char[4]}\n{char[5]}\n{char[6]}")
elif (char[0] + char[1] + char[2] + char[3] + char[4] + char[5] + char[7]) == 100:
        print(f"{char[0]}\n{char[1]}\n{char[2]}\n{char[3]}\n{char[4]}\n{char[5]}\n{char[7]}")
elif (char[0] + char[1] + char[2] + char[3] + char[4] + char[5] + char[8]) == 100:
        print(f"{char[0]}\n{char[1]}\n{char[2]}\n{char[3]}\n{char[4]}\n{char[5]}\n{char[8]}")
elif (char[0] + char[1] + char[2] + char[3] + char[4] + char[6] + char[7]) == 100:
        print(f"{char[0]}\n{char[1]}\n{char[2]}\n{char[3]}\n{char[4]}\n{char[6]}\n{char[7]}")
elif (char[0] + char[1] + char[2] + char[3] + char[4] + char[6] + char[8]) == 100:
        print(f"{char[0]}\n{char[1]}\n{char[2]}\n{char[3]}\n{char[4]}\n{char[6]}\n{char[8]}")
elif (char[0] + char[1] + char[2] + char[3] + char[4] + char[7] + char[8]) == 100:
        print(f"{char[0]}\n{char[1]}\n{char[2]}\n{char[3]}\n{char[4]}\n{char[7]}\n{char[8]}")
elif (char[0] + char[1] + char[2] + char[3] + char[5] + char[6] + char[7]) == 100:
        print(f"{char[0]}\n{char[1]}\n{char[2]}\n{char[3]}\n{char[5]}\n{char[6]}\n{char[7]}")
elif (char[0] + char[1] + char[2] + char[3] + char[5] + char[6] + char[8]) == 100:
        print(f"{char[0]}\n{char[1]}\n{char[2]}\n{char[3]}\n{char[5]}\n{char[6]}\n{char[8]}")
elif (char[0] + char[1] + char[2] + char[3] + char[5] + char[7] + char[8]) == 100:
        print(f"{char[0]}\n{char[1]}\n{char[2]}\n{char[3]}\n{char[5]}\n{char[7]}\n{char[8]}")
elif (char[0] + char[1] + char[2] + char[4] + char[5] + char[6] + char[7]) == 100:
        print(f"{char[0]}\n{char[1]}\n{char[2]}\n{char[4]}\n{char[5]}\n{char[6]}\n{char[7]}")
elif (char[0] + char[1] + char[2] + char[4] + char[5] + char[6] + char[8]) == 100:
        print(f"{char[0]}\n{char[1]}\n{char[2]}\n{char[4]}\n{char[5]}\n{char[6]}\n{char[8]}")
elif (char[0] + char[1] + char[2] + char[4] + char[5] + char[7] + char[8]) == 100:
        print(f"{char[0]}\n{char[1]}\n{char[2]}\n{char[4]}\n{char[5]}\n{char[7]}\n{char[8]}")
elif (char[0] + char[1] + char[3] + char[4] + char[5] + char[6] + char[7]) == 100:
        print(f"{char[0]}\n{char[1]}\n{char[3]}\n{char[4]}\n{char[5]}\n{char[6]}\n{char[7]}")
elif (char[0] + char[1] + char[3] + char[4] + char[5] + char[6] + char[8]) == 100:
        print(f"{char[0]}\n{char[1]}\n{char[3]}\n{char[4]}\n{char[5]}\n{char[6]}\n{char[8]}")
elif (char[0] + char[1] + char[3] + char[4] + char[5] + char[7] + char[8]) == 100:
        print(f"{char[0]}\n{char[1]}\n{char[3]}\n{char[4]}\n{char[5]}\n{char[7]}\n{char[8]}")
elif (char[0] + char[1] + char[3] + char[4] + char[6] + char[7] + char[8]) == 100:
        print(f"{char[0]}\n{char[1]}\n{char[3]}\n{char[4]}\n{char[5]}\n{char[6]}\n{char[8]}")
elif (char[0] + char[1] + char[4] + char[5] + char[6] + char[7] + char[8]) == 100:
        print(f"{char[0]}\n{char[1]}\n{char[4]}\n{char[5]}\n{char[6]}\n{char[7]}\n{char[8]}")
elif (char[0] + char[2] + char[3] + char[4] + char[5] + char[6] + char[7]) == 100:
        print(f"{char[0]}\n{char[2]}\n{char[3]}\n{char[4]}\n{char[5]}\n{char[6]}\n{char[7]}")
elif (char[0] + char[2] + char[3] + char[4] + char[5] + char[6] + char[8]) == 100:
        print(f"{char[0]}\n{char[2]}\n{char[3]}\n{char[4]}\n{char[5]}\n{char[6]}\n{char[8]}")
elif (char[0] + char[2] + char[3] + char[4] + char[5] + char[7] + char[8]) == 100:
        print(f"{char[0]}\n{char[2]}\n{char[3]}\n{char[4]}\n{char[5]}\n{char[7]}\n{char[8]}")
elif (char[0] + char[2] + char[3] + char[4] + char[6] + char[7] + char[8]) == 100:
        print(f"{char[0]}\n{char[2]}\n{char[3]}\n{char[4]}\n{char[6]}\n{char[7]}\n{char[8]}")
elif (char[0] + char[2] + char[3] + char[5] + char[6] + char[7] + char[8]) == 100:
        print(f"{char[0]}\n{char[2]}\n{char[3]}\n{char[5]}\n{char[6]}\n{char[7]}\n{char[8]}")
elif (char[0] + char[2] + char[4] + char[5] + char[6] + char[7] + char[8]) == 100:
        print(f"{char[0]}\n{char[2]}\n{char[4]}\n{char[5]}\n{char[6]}\n{char[7]}\n{char[8]}")
elif (char[0] + char[3] + char[4] + char[5] + char[6] + char[7] + char[8]) == 100:
        print(f"{char[0]}\n{char[3]}\n{char[4]}\n{char[5]}\n{char[6]}\n{char[7]}\n{char[8]}")
elif (char[1] + char[2] + char[3] + char[4] + char[5] + char[6] + char[7]) == 100:
        print(f"{char[1]}\n{char[2]}\n{char[3]}\n{char[4]}\n{char[5]}\n{char[6]}\n{char[7]}")
elif (char[1] + char[2] + char[3] + char[4] + char[5] + char[6] + char[8]) == 100:
        print(f"{char[1]}\n{char[2]}\n{char[3]}\n{char[4]}\n{char[5]}\n{char[6]}\n{char[8]}")
elif (char[1] + char[2] + char[3] + char[4] + char[5] + char[7] + char[8]) == 100:
        print(f"{char[1]}\n{char[2]}\n{char[3]}\n{char[4]}\n{char[5]}\n{char[7]}\n{char[8]}")
elif (char[1] + char[2] + char[3] + char[4] + char[6] + char[7] + char[8]) == 100:
        print(f"{char[1]}\n{char[2]}\n{char[3]}\n{char[4]}\n{char[6]}\n{char[7]}\n{char[8]}")
elif (char[1] + char[2] + char[3] + char[5] + char[6] + char[7] + char[8]) == 100:
        print(f"{char[1]}\n{char[2]}\n{char[3]}\n{char[5]}\n{char[6]}\n{char[7]}\n{char[8]}")
elif (char[1] + char[2] + char[4] + char[5] + char[6] + char[7] + char[8]) == 100:
        print(f"{char[1]}\n{char[2]}\n{char[4]}\n{char[5]}\n{char[6]}\n{char[7]}\n{char[8]}")
elif (char[1] + char[3] + char[4] + char[5] + char[6] + char[7] + char[8]) == 100:
        print(f"{char[1]}\n{char[3]}\n{char[4]}\n{char[5]}\n{char[6]}\n{char[7]}\n{char[8]}")
elif (char[2] + char[3] + char[4] + char[5] + char[6] + char[7] + char[8]) == 100:
        print(f"{char[2]}\n{char[3]}\n{char[4]}\n{char[5]}\n{char[6]}\n{char[7]}\n{char[8]}")


'''
char = []

for a in range(9):
    b = int(input())
    char.append(b)

#for i in char:
#    print(i,end='')            
nsum = sum(char)
A1 = 0
A2 = 0
#print("\n",sum(char),"\n")

for i in range(9):
    for j in range(9):
        #print(char[i],char[j])
        if i == j:
            continue
        nsum -= (int(char[i])+int(char[j]))
        #print(char[i],char[j],nsum)

        if nsum ==100:
            A1 = i
            A2 = j
            break
        nsum += (int(char[i])+int(char[j]))
       
#print(A1,A2)

for i in range(len(char)):
    if i ==A1 or i ==A2:
        continue
    print(char[i])


#for i in range(num):
 #           if num2[i][0] >= Y and num2[i][1] <= P:
  #              print(num2[i][0], num2[i][1])





str = str(input())
for i in range(len(str)):
    if i%2 ==0:
        print(str[i],end=" ")

'''
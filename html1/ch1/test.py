'''
num,num1 = input().split()

def ex9459(s,a):
    if s == 'M' or s == 'm':
        if int(a) >= 20:
            print('MAN')
        else:
            print('BOY')
    if s == 'F' or s =='f':
        if int(a) >= 20:
            print('WOMAN')
        else:
            print('GIRL')

ex9459(num,num1)'''


'''
B1 , N1 = input().split()

len = 0
for i in B1:
    len +=1
#C = ord(B1)-55
print(len)


print(ord("A")-55)

for i in range(len):
    i += i*36
    print(i)
    
'''


#36
#36*36 1296
#36*36*36 46656
#36*36*36*36 1679616
#36*36*36*36*36 60466176

'''
N, B = input().split()

res = 0;

for idx, ch in enumerate(N):
    if ch.isdigit():
        res += int(B)

''''''
n, b = input().split()
print(int(n, int(b)))
'''
'''
N = int(input())
sum = 0
i=1
while i<=N:
    sum +=i
    i+=1

print(sum)

'''
'''name = input()
age = int(input())
'''
print("%s is %d years old."%(input(), int(input())))
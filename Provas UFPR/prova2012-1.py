#Questão 1
a=100
b=1
s=0
for i in range(100):
    s=s+(b/a)
    print (s)
    a-=1
    b+=1


#Questão 2
n=int(input())
a=1
b=n-1
for i in range (n-1):
    print(a, "e", b)
    a+=1
    b-=1


#Questão 3
a=0
b=0
soma=0
count=0

while a==b:
    a = int(input())
    b = int(input())

if a<b:
    while a<=b:
        if a%2==1:
            soma=soma+a
        a+=1

if b<a:
    while b<=a:
        if b%3==0:
            soma=soma+b
            count+=1
        b+=1
    soma=soma/count

print (soma)

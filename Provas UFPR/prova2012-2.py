#Questão 1
h=int(input())
m=int(input())
s=int(input())
soma=((h*60*60)+(m*60)+s)
print(soma)

#Questão 2
s=1
p=1
for i in range (100):
    p=p*2
    q=1/p
    s+=q
print (s)

#Questão 3
n=-1
maior=0
while n!=0:
    n=int(input())
    if n%7==0 and n>maior:
        maior=n
print(maior)

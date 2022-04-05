#Questão 1 [losely based on it]
n = int(input())
numant=0
numatu=1
print (numant)
print (numatu)
for i in range (n-2):
    numnext=numant+numatu
    print (numnext)
    numant=numatu
    numatu=numnext


#Questão 2 
n = int(input())
x1 = -1000
y1 = 1000
x2 = 1000
y2 = -1000
while n!=0:
    newx1 = float(input("X1:"))
    newy1 = float(input("Y1:"))
    newx2 = float(input("X2:"))
    newy2 = float(input("Y2:"))
    if newx1 > x1:
        x1 = newx1
    if newx2 < x2:
        x2 = newx2
    if newy1 < y1:
        y1 = newy1
    if newy2 > y2:
        y2 = newy2
    n-=1
if x1<x2 and y1>y2:
    print(x1, y1, x2, y2)
else:
    print("Nenhum")
         
         
#Questão 3
n = int(input())
m = int(input())
p = int(input())
pa = [1,1]
pb = [n,m]
for i in range(p): 
    a = int(input())
    b = int(input())

    if a == 1:
        pa[1]=int(pa[1])+1
    elif a == 2:
        pa[1]=int(pa[1])-1
    elif a == 3:
        pa[0]=int(pa[0])+1
    elif a == 4:
        pa[0]=int(pa[0])-1

    if b == 1:      
        pb[1]=int(pb[1])+1
    elif b == 2:
        pb[1]=int(pb[1])-1
    elif b == 3:
        pb[0]=int(pb[0])+1
    elif b == 4:
        pb[0]=int(pb[0])-1

    if pa == pb:
        print("Se encontraram no passo", i+1 ,"na posição", pa)
    elif pa[0]<1 or pa[0]>n or pa[1]<1 or pa[1]>m:
        print("PA saiu na posição", pa, "no passo", i+1)
    elif pb[0]<1 or pb[0]>n or pb[1]<1 or pb[1]>m:
        print("PB saiu na posição", pb, "no passo", i+1)
    elif i==(p-1) and pa != pb:
        print("Não se encontraram")

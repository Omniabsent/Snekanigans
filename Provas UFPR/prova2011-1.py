#questão 1
numanterior = -1
numatual = -1
count = 0
soma = 0
while (numatual!=numanterior*2) and (numatual!=numanterior/2):
    numanterior = numatual
    numatual = int(input())
    count += 1
    soma = soma + numatual
print ("count:", count, "soma:", soma, "numanterior:", numanterior, "numatual:", numatual)

#questão 2 
a = 15
b = 23
a = a+b
b = a-b
a = a-b
print (a, b)

#questão 3
n=-1
while n!=0:
    n = int(input())
    if n>0:
        print(n*0, n*1, n*2, n*3, n*4, n*5, n*6, n*7, n*8, n*9)
#só funciona com números inteiros e menores que 4K, porque romanos eram burros
#não tem como fazer a operação inversa, porque eu sou burra

arabic=int(input("Insira o número arábico [max 3999] "))

milhar=arabic//1000
centena=(arabic-(milhar*1000))//100
dezena=(arabic-(centena*100)-(milhar*1000))//10  
unidade=arabic%10

roman=""
for i in range(milhar): 
    roman=roman+"M"

if centena==9:
    roman=roman+"CM"    
elif centena==5:
    roman=roman+"D"
elif centena==4:
    roman=roman+"CD"
else:
    for i in range(centena): 
        roman=roman+"C"

if dezena==9:
    roman=roman+"XC"
elif dezena==5:
    roman=roman+"L"
elif dezena==4:
    roman=roman+"XL"
else:
    for i in range(dezena): 
        roman=roman+"X"

if unidade==9:
    roman=roman+"IX"
elif unidade==5:
    roman=roman+"V"
elif unidade==4:
    roman=roman+"IV"
else:
    for i in range(unidade): 
        roman=roman+"I"

print("O número", arabic, "em romano é", roman)

    

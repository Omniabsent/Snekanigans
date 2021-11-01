print("Insira a data por partes")
dia = int(input("Dia:"))
mes = int(input("Mês:"))
ano = int(input("Ano:"))

chavesMes = {1: 1, 2: 4, 3: 4, 4: 0, 5: 2, 6: 5, 7: 0, 8: 3, 9: 6, 10: 1, 11: 4, 12: 6}
valorMes = chavesMes.get(mes)

valorAno = 4
for i in range(ano+1): 
    if valorAno < 6:
        valorAno +=1
    else: 
        valorAno = 0
    if (i%400 == 0) or (i%4 == 0 and not(i%100 == 0 and i%400 != 0)):
        if valorAno < 6:
            valorAno +=1
        else: 
            valorAno = 0

if mes <= 2:
    valorAno -= 1

valorSemana = (dia + valorMes + valorAno)%7 

nomeDia = {1: "Domingo", 2: "Segunda", 3: "Terça", 4: "Quarta", 5: "Quinta", 6: "Sexta", 0: "Sábado"}
resultado = nomeDia.get(valorSemana)

print (resultado)

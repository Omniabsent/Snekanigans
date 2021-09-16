#só sabe dizer o dia da semana que cai a data em 2021 porque eu não entendi como calcular a chave do ano

print("Insira a data por partes")
dia = int(input("Dia:"))
mes = int(input("Mês:"))
ano = int(input("Ano:"))

chavesMes = {1: 1, 2: 4, 3: 4, 4: 0, 5: 2, 6: 5, 7: 0, 8: 3, 9: 6, 10: 1, 11: 4, 12: 6}
valorMes = chavesMes.get(mes)

valorSemana = (dia + valorMes + 4)%7  #4 é a chave de 2021

nomeDia = {1: "Domingo", 2: "Segunda", 3: "Terça", 4: "Quarta", 5: "Quinta", 6: "Sexta", 0: "Sábado"}
resultado = nomeDia.get(valorSemana)

print (resultado)
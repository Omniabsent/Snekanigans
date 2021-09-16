escolha = (input("Deseja inserir um número em [b]inário ou em [d]ecimal?"))

if escolha == "b":
    binario=int(input("Insira o número em binário para ser convertido em decimal:"))
    nextdigit=binario
    lastdigit=0
    posicao=1
    valor=0
    while nextdigit>0:
        lastdigit=nextdigit%2
        nextdigit=int(nextdigit/10)
        if lastdigit==1:
            valor=valor+posicao
        posicao=posicao*2
    print(valor)

else:

    decimal=int(input("Insira o número em decimal para ser convertido em binário:"))
    valor = ""
    while decimal>=1:
        if decimal%2==1:
            valor="1"+valor
        elif decimal==1:
            valor="1"+valor
        else:
            valor="0"+valor
        decimal=int(decimal/2)
    print(valor)
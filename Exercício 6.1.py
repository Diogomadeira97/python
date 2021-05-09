Vetor=input(">Digite as 5 coordenads de um vetor separadas por espaço:").split()

Valor=input("\n>Digite um valor qualquer e eu digo a posição ou digito '-1' se o valor não pertencer ao vetor:")

if Valor in Vetor:

    for p in range(len(Vetor)):

        if (Vetor[p]==Valor):

            print("\n>O Valor",Valor,"está na posição",p)

else:

    print("\n>-1")

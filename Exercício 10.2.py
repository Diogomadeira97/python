palavra1=input(">Digite a primeira palavra desejada: ").split()

palavra2=input("\n>Digite a segunda palavra desejada: ").split()

if (len(palavra1)>0):
    palavra1_junta=palavra1[0]
    for i in range(len(palavra1)):
        if (i!=0):                       
            palavra1_junta=palavra1_junta+palavra1[i]
    palavra1_organizada=list(palavra1_junta.upper())
    palavra1_organizada.sort()    
else:
    palavra1_organizada=palavra1

if (len(palavra2)>0):
    palavra2_junta=palavra2[0]
    for i in range(len(palavra2)):
        if (i!=0):                    
            palavra2_junta=palavra2_junta+palavra2[i]
    palavra2_organizada=list(palavra2_junta.upper())
    palavra2_organizada.sort()    
else:
    palavra2_organizada=palavra1


if (palavra1_organizada==palavra2_organizada) and (len(palavra1)>0) and (len(palavra2)>0):
    print("\n>É um anagrama")

else:
    print("\n>Não é um anagrama")



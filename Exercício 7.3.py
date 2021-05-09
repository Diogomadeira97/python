A=[]

AT=[]

O=(int(input(">Informe a ordem da sua matriz até 100:")))

if 0<O<=100:

    print("")
    
    for i in range (O):
    
        linha=[]
    
        for j in range (O):

            linha.append(int(input(">Digite as coordenada ["+str(i+1)+","+str(j+1)+"]:")))  

        A.append(linha)

        print("")

    print(">A matriz está representada por:\n")
        
    for l in range(O):

        print(A[l])
    
    for i in range (O):
    
        linha=[]
    
        for j in range (O):

            linha.append(A[j][i])  

        AT.append(linha)
    
    print("\n>A sua transposta está representada por:\n")
        
    for l in range(O):

        print(AT[l])
    
else:

    print("\n>ERRO.")

    

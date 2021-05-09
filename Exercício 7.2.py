A=[]
B=[]
C=[]

for i in range (5):

    linha=[]

    for j in range (5):
    
        linha.append(int(input(">Digite as coordenada ["+str(i+1)+","+str(j+1)+"] da matriz A:")))

    A.append(linha)

    print("")

for l in range(5):
    
    print(A[l])

print("")

for i in range (5):
    
    linha=[]
    
    for j in range (5):

        linha.append(int(input(">Digite as coordenada ["+str(i+1)+","+str(j+1)+"] da matriz B:")))  

    B.append(linha)

    print("")

for l in range(5):

    print(B[l])

for i in range(5):

    C.append([0]*5)

for i in range (5):

    for j in range (5):

        C[i][j]=((A[i][j])+(B[i][j]))
        
print("\n>A matriz C é igual a A + B, sendo representada por:\n")

for l in range(5):

    print(C[l])        

    

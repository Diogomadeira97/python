matriz=[]

for i in range (5):

    linha=[]

    for j in range (5):
    
        linha.append(int(input(">Digite a a coordenada ["+str(i+1)+","+str(j+1)+"]:")))

    matriz.append(linha)

    print("")
    
for l in range(5):

    print(matriz[l])
    
K=(int(input("\n>Digite um número para multiplicar a diagonal da matiz:")))


for l in range(5):

    matriz[l][l]=(matriz[l][l])*K
    
print("")

for l in range(5):

    print(matriz[l])

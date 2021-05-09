vet=input(">Digite as 20 coordenadas de um vetor separadas por espaço:").split()

pos=[]

semdup=[]

for w in range(len(vet)):

    vet[w]=float(vet[w])

    if vet[w]>=0:

        pos.append(vet[w])

    while (vet[w] not in semdup) and (vet[w]>=0):

        semdup.append(vet[w])

print("\n>O vetor está representado por vet=",vet,"\n\n>O vetor apenas com as coordenadas positivas de x está reporesentado por pos=",pos,"\n\n>E o vetor com apenas uma ocorrência de y está representado por semdup=",semdup)

        
    

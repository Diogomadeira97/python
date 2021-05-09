import math

vetor=[]

v=input(">Informe os valores do vetor separados por espaço:").split()

for i in range(len(v)):
    
    vetor.append(float(v[i]))
    
print("\n>O vetor é:",vetor)

soma=0

for i in range(len(vetor)):

    soma=soma+vetor[i]

media=soma/len(vetor)

teste=media in vetor

if teste:

    print("\n>A média vale",media,", e o valor mais próximo é",media,".")

else:

    maisperto=math.fabs(vetor[0]-media)

    pos=0

    valores=[]

    for i in range(len(vetor)):

        if math.fabs(vetor[i]-media)<maisperto:

            maisperto=math.fabs(vetor[i]-media)

            pos=i
            
    valores.append(vetor[pos])

    for i in range(len(vetor)):

        if math.fabs(vetor[i]-media)==math.fabs(vetor[pos]-media) and vetor[i]!=vetor[pos]:

            valores.append(vetor[i])
    
    if len(valores)==1:                   

        print("\n>A média vale",media,", e o valor mais próximo é",valores,".")

    elif len(valores)>1:

        for i in range(len(valores)):

            if valores.count(i)>1:

                valores.remove(i)

        print("\n>A média vale",media,", e os valores mais próximos são",valores,".")
                       



from random import randint

jogadas=[]

contador=[]

for i in range(10):

    j=randint(1,6)

    jogadas.append(j)

for i in range(1,7):

    contador.append(jogadas.count(i))

print(">O vetor que representa as jogadas é:",jogadas,"\n\n>O vetor que conta quantas vezes cada número apareceu é:",contador)


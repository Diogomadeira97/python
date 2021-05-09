import random

print(">Vou lançar um dado 50 vezes para listar os valores e dizer quantas vezes o número 6 aparece...")

Valores=[0]*50

V6=0

for lançamento in range(50):

    Valores[lançamento]=random.randint(1,6)

    if (Valores[lançamento]==6):

         V6=V6+1

Porcentagem=(V6/50)*100

print("\n>A lista de valores é:",Valores,"\n\n>O número 6 aparece",V6,"Vezes,sendo",'%.2f'%Porcentagem,"% do número de vezes que o dado foi lançado.")

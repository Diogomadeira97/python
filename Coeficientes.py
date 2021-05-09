import math

def força_ionica(lista):
    a=0
    for ion in lista:
        a=(dic[ion][0]*dic[ion][1]**2) + a
    força_ionica=a/2
    return força_ionica

def coeficiente_de_atividade(lista,FI):
    for ion in lista:
        x=(lista[ion][0])**2
        y=math.sqrt(FI)
        z=lista[ion][1]
        a=10**(-((0.51*x*y)/(1+(z*(y/305)))))
        lista[ion].append(a)
    return lista

dic={}

dic2={}

n_ions=int(input(">Digite quantos íons estão presentes na solução: "))

print("\n>Digite o íon, sua concentração e sua carga (separados por espaços.\n")

for i in range(n_ions):
    a=[0,0,0]
    valores=input(">íon"+str(i+1)+": ").split()
    a[0]=float(valores[1])
    a[1]=int(valores[2])
    dic[valores[0]]=a

mi=força_ionica(dic)

n_ions2=int(input("\n>Digite quantos coeficientesa você quer descobrir: "))

print("\n>Digite o íon, sua carga eseu raio iônico (separados por espaços.\n")

for i in range(n_ions2):
    a=[0,0]
    valores2=input(">íon"+str(i+1)+": ").split()
    a[0]=int(valores2[1])
    a[1]=int(valores2[2])
    dic2[valores2[0]]=a

coeficiente=coeficiente_de_atividade(dic2,mi)

dic2.update(coeficiente)

print("\n>Força iônica: ","%.3f" %mi,"\n")

for ion in dic2:
    print(">Coeficiente de atividade do",ion,": ","%.3f" %dic2[ion][2])
         

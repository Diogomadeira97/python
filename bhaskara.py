import math

def valor_de_x(a,b,c):
    delta=(b**2)-(4*a*c)
    x1=(-(b)+(math.sqrt(delta)))/(2*a)
    x2=(-(b)-(math.sqrt(delta)))/(2*a)
    return (x1,x2,delta)

valores=input("Digite a, b e c separados por espaço").split()

a=float(valores[0])
b=float(valores[1])
c=float(valores[2])

resposta=valor_de_x(a,b,c)

print("\n>Delta=",resposta[2],"\n>X1=",resposta[0],"\n>X2=",resposta[1])



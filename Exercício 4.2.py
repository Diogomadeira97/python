import math

x1=(float(input(">Digite a coordenada x do ponto 1 com duas casas decimais => ")))
y1=(float(input(">Digite a coordenada y do ponto 1 com duas casas decimais => ")))

x2=(float(input("\n>Digite a coordenada x do ponto 2 com duas casas decimais => ")))
y2=(float(input(">Digite a coordenada y do ponto 2 com duas casas decimais => ")))

x3=(float(input("\n>Digite a coordenada x do ponto 3 com duas casas decimais => ")))
y3=(float(input(">Digite a coordenada y do ponto 3 com duas casas decimais => ")))


a=(math.sqrt((x2-x1)**2 + (y2-y1)**2))
b=(math.sqrt((x2-x3)**2 + (y2-y3)**2))
c=(math.sqrt((x1-x3)**2 + (y1-y3)**2))


if (math.fabs(b-c)<a<(b+c)) and (math.fabs(a-c)<b<(a+c)) and (math.fabs(a-b)<c<(a+b)):
    
    A=(math.degrees(math.acos(((((b)**2)+((c)**2)-((a)**2))/((2)*(b)*(c))))))
    B=(math.degrees(math.acos(((((c)**2)+((a)**2)-((b)**2))/((2)*(c)*(a))))))
    C=(math.degrees(math.acos(((((b)**2)+((a)**2)-((c)**2))/((2)*(b)*(a))))))
    
    
    A1=(math.fmod(A,1)*100)
    A2=(math.fmod(A1,1)*100)
    if 56<=A2:
        A=(math.trunc(A)+(math.trunc(A1+1))/100)
    else:
        A=(math.trunc(A)+(math.trunc(A1))/100)

        
    B1=(math.fmod(B,1)*100)
    B2=(math.fmod(B1,1)*100)
    if 56<=B2:
        B=(math.trunc(B)+(math.trunc(B1+1))/100)
    else:
        B=(math.trunc(B)+(math.trunc(B1))/100)


    C1=(math.fmod(C,1)*100)
    C2=(math.fmod(C1,1)*100)
    if 56<=C2:
        C=(math.trunc(C)+(math.trunc(C1+1))/100)
    else:
        C=(math.trunc(C)+(math.trunc(C1))/100) 


        
    a1=(math.fmod(a,1)*100)
    a2=(math.fmod(a1,1)*100)
    if 56<=a2:
        a=(math.trunc(a)+(math.trunc(a1+1))/100)
    else:
        a=(math.trunc(a)+(math.trunc(a1))/100)

        
    b1=(math.fmod(b,1)*100)
    b2=(math.fmod(b1,1)*100)
    if 56<=b2:
        b=(math.trunc(b)+(math.trunc(b1+1))/100)
    else:
        b=(math.trunc(b)+(math.trunc(b1))/100)


    c1=(math.fmod(c,1)*100)
    c2=(math.fmod(c1,1)*100)
    if 56<=c2:
        c=(math.trunc(c)+(math.trunc(c1+1))/100)
    else:
        c=(math.trunc(c)+(math.trunc(c1))/100) 

        
    if (A==B) and (B==C)and(C==A):
        T=(str("equilátero"))
           
    elif(A!=B) and (B!=C) and (C!=A):
        T=(str("escaleno"))
           
    elif (A!=B) or (B!=C) or (C!=A) and (A==B) or (B==C) or (C==A):
        T=(str("isósceles"))

    print("\n>O triângulo é",T,"e os seus catetos são:\n\n>Cateto a:",'%.2f'%a,"\n>Cateto b:",'%.2f'%b,"\n>Cateto c:",'%.2f'%c,"\n\n>Os seus ângulos são:\n\n>Ângulo oposto ao cateto a:",'%.2f'%A,"\n>Ângulo oposto ao cateto b:",'%.2f'%B,"\n>Ângulo oposto ao cateto c:",'%.2f'%C)


else:
    print("\n>As coordenada não formam um triângulo.")
           


V1=[]

V2=[]

V3=[]

x=input(">Digite os valores da lista 1:").split()

for i in range(len(x)):
    
    V1.append(float(x[i]))

y=input("\n>Digite os valores da lista 2:").split()

for i in range(len(y)):
    
    V2.append(float(y[i]))
    
print("\n>Lista 1:",V1,"\n\n>Lista 2:",V2)



if  len(V1) == len(V2) :
    
    for i in range(len(V1)):
        
      V3.append(V1[i])
      
      V3.append(V2[i])

if len(V1) > len(V2):

    for i in range(len(V2)):

        V3.append(V2[i])
        
        V3.append(V1[i])
        
    V3=V3+V1[len(V2):]

if len(V2) > len(V1):

    for i in range(len(V1)):
        
        V3.append(V1[i])
        
        V3.append(V2[i])
        
    V3=V3+V2[len(V1):]
        
print("\n>Lista intercalada:",V3)

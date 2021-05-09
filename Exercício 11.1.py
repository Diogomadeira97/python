def lerCorredores():

    dic={}

    lista=["0","1","2","3","4","5","6","7","8","9","."]

    for i in range(6):

        print("\n>Corredor",i+1)
        
        nome=str(input("\n>Digite o nome do corredor: "))
        
        voltas=input("\n>Digite o tempo das 10 voltas em ordem, em segundos e separados por espaço: ").split()        
        teste1=0
        for i in range(len(voltas)):
            teste2=0
            for digito in voltas[i]:
                if digito not in lista:
                    teste2=teste2+1
            if (teste2==0):
                teste1=teste1+1
                voltas[i]=float(voltas[i])

        while (teste1!=10): 
            voltas=input("\n>Valores inválidos. Digite os 10 valores em ordem, em segundos e separados por espaço: ").split()        
            teste1=0
            for i in range(len(voltas)):
                teste2=0
                for digito in voltas[i]:
                    if digito not in lista:
                        teste2=teste2+1
                if (teste2==0):
                    teste1=teste1+1
                    voltas[i]=float(voltas[i])
                    
        dic[nome]=voltas

    print("")
    
    for corredor in dic:
        print(corredor,"=",dic.get(corredor))

    return dic

def determinarResultados(dic):

    resultados=[0,0]

    menores_voltas=[]

    menores_tempos=[]
    
    for corredor in dic:

        tempo_medio=sum(dic[corredor])/len(dic[corredor])
        menores_tempos.append(tempo_medio)
        
        voltas=dic.get(corredor)
        tempo_volta=voltas[0]
        numero_volta=1
        for i in range(len(voltas)):
            if (voltas[i]<tempo_volta):
                tempo_volta=voltas[i]
                numero_volta=i+1
        menores_voltas.append(tempo_volta)
                
        dic[corredor]=[tempo_medio,numero_volta,tempo_volta]

    menores_voltas.sort()

    menores_tempos.sort()

    for corredor in dic:
        lista=dic.get(corredor)
        
        if lista[0]==menores_tempos[0]:
            resultados[1]=(corredor,lista[0])
        
        if lista[2]==menores_voltas[0]:
            resultados[0]=(corredor,lista[1],lista[2])

    return resultados

def imprimirResultados(menor_volta,campeão):

    print("\n>campeão\n>Corredor:",campeão[0],"\n>Tempo:",campeão[1],"segundos")
    print("\n>Menor volta \n>Tempo:",menor_volta[2],"segundos \n>Corredor:",menor_volta[0],"\n>Volta:",menor_volta[1])
        

a=lerCorredores()

b=determinarResultados(a)

imprimirResultados(b[0],b[1])

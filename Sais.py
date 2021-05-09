import math

def forte_forte(C,cargaA,cargaB):
    return (1e-7,7,1e-7,7,(C*cargaB),(C*cargaA),"Como estamos tratando de um sal proveniente de um ácido e de uma base fortes, o pH não será alterado pois um neutralizará o outro.")

def fraco_forte(C,K,resposta):
        x=math.sqrt((K*1e-14)/C)
        y=-(math.log(x,10))
        z=(1e-14)/(x)
        w=-(math.log(z,10))
        if (resposta=="A"):
            return (x,y,z,w,z,C,C,"Primeiro utilizamos as equações dos BMs no BC. Feito isso, podemos igualar a concentração da forma ionizada do ácido à concentração de OH- pois a solução é básica (aproximação 1). Como a concentração da forma ionizada do ácido é bem menor que sua forma não ionizada, podemos desprezar ela no BM do ácido, igualando assim a forma não ionizada à concentração analítica (aproximação 2). Considerando que [OH-]=Kw/[H+], jogamos os valores obtido no Ka e obtemos então a seguinte expressão Ka=([H+]*C)/(Kw/[H+]).")
        if (resposta=="B"):
            return (z,w,x,y,z,C,C,"Primeiro utilizamos as equações dos BMs no BC. Feito isso, podemos igualar a concentração da forma ionizada da base à concentração de H+ pois a solução é ácida(aproximação 1). Como a concentração da forma ionizada da base é bem menor que sua forma não ionizada, podemos desprezar ela no BM da base, igualando assim a forma não ionizada à concentração analítica (aproximação 2). Considerando que [H+]=Kw/[OH-], jogamos os valores obtido no Kb e obtemos então a seguinte expressão Kb=([OH-]*C)/(Kw/[OH-]).")

def fraco_forte_força_ionica(C,K,resposta,Ca,Cc):
        x=math.sqrt((K*1e-14)/C*Cc*(Ca**2))
        Ax=x*Ca
        y=-(math.log(Ax,10))
        z=(1e-14)/(Ax)
        w=-(math.log(z,10))
        if (resposta=="A"):
            return (x,y,z,w,z,C,C,"Primeiro utilizamos as equações dos BMs no BC. Feito isso, podemos igualar a concentração da forma ionizada do ácido à concentração de OH- pois a solução é básica (aproximação 1). Como a concentração da forma ionizada do ácido é bem menor que sua forma não ionizada, podemos desprezar ela no BM do ácido, igualando assim a forma não ionizada à concentração analítica (aproximação 2). Considerando que [OH-]=Kw/[H+], jogamos os valores obtido no Ka e obtemos então a seguinte expressão Ka=([H+]*C)/(Kw/[H+]).")
        if (resposta=="B"):
            return (z,w,x,y,z,C,C,"Primeiro utilizamos as equações dos BMs no BC. Feito isso, podemos igualar a concentração da forma ionizada da base à concentração de H+ pois a solução é ácida(aproximação 1). Como a concentração da forma ionizada da base é bem menor que sua forma não ionizada, podemos desprezar ela no BM da base, igualando assim a forma não ionizada à concentração analítica (aproximação 2). Considerando que [H+]=Kw/[OH-], jogamos os valores obtido no Kb e obtemos então a seguinte expressão Kb=([OH-]*C)/(Kw/[OH-]).")

def fraco_fraco(C,Ka,Kb):
        x=math.sqrt((Ka*1e-14)/Kb)
        y=-(math.log(x,10))
        z=(1e-14)/(x)
        w=-(math.log(z,10))
        AP=(x*C)/(Ka+x)
        A=C-AP
        return (x,y,z,w,AP,A,AP,A,"Primeiro utilizamos as equações dos BMs no BC. Feito isso, podemos desprezar as concentrações de H+ e OH- na equação do BC e na equação que acabamos de obter para igualar as formas ionizadas do ácido com a da base, e as não ionizadas do ácido com a da base (aproximção 1). Multiplicando o Ka pelo Kw e depois dividindo pelo Kb, chegamos na seguinte expressão: [H+]^2=(Ka*Kw)/Kb.")


def fraco_fraco_força_ionica(C,Ka,Kb,Ca):
        x=math.sqrt((Ka*1e-14)/Kb*(Ca**2))
        Ax=x*Ca
        y=-(math.log(Ax,10))
        z=(1e-14)/(Ax)
        w=-(math.log(z,10))
        AP=(Ax*C)/(Ka+Ax)
        A=C-AP
        return (x,y,z,w,AP,A,AP,A,"Primeiro utilizamos as equações dos BMs no BC. Feito isso, podemos desprezar as concentrações de H+ e OH- na equação do BC e na equação que acabamos de obter para igualar as formas ionizadas do ácido com a da base, e as não ionizadas do ácido com a da base (aproximção 1). Multiplicando o Ka pelo Kw e depois dividindo pelo Kb, chegamos na seguinte expressão: [H+]^2=(Ka*Kw)/Kb.")


def menu():
    print("(a)Ácido forte e base forte")
    print("(b)Ácido forte e base fraca/ácido fraco e base forte")
    print("(c)Ácido fraco e base fraca")
    
menu()

M=input()

if (M=="a"):
    CA=float(input("\n>Digite a concetração analítica: "))
    c_iona=int(input("\n>Digite a carga do íon ácido: "))
    c_ionb=int(input("\n>Digite a carga do íon básico: "))
    R=forte_forte(CA,c_iona,c_ionb)
    print("\n>Concentração de H+=",R[0],"\n>pH=","%.2f" %R[1],"\n\n>Concentração de OH-=",R[2],"\n>pOH=","%.2f" %R[3],"\n\n>Concentração do íon ácido=",R[4],"\n\n>Concentração do íon básico=",R[5],"\n\n>Explicação: ",R[6])

if (M=="b"):
    CA=float(input("\n>Digite a concetração analítica: "))
    A_ou_B=input("\n>Quem é fraco (A/B)? ")
    pergunta=input("\n>Deseja considerar a força iônica(S/N)? ")
    if (A_ou_B=="A"):
        if (pergunta=="S"):
            ka=float(input("\n>Digite o Ka: "))
            Ca1=float(input("\n>Digite o coeficiente de atividade do H+: "))
            Cc1=float(input("\n>Digite o coeficiente de atividade do íon da base: "))
            R=fraco_forte_força_ionica(CA,ka,A_ou_B,Ca1,Cc1)
            print("\n>Concentração de H+=",R[0],"\n>pH=","%.2f" %R[1],"\n\n>Concentração de OH-=",R[2],"\n>pOH=","%.2f" %R[3],"\n\n>Concentração do ácido não ionizado=",R[4],"\n\n>Concentração do íon ácido=",R[5],"\n\n>Concentração do íon básico=",R[6],"\n\n>Explicação: ",R[7])
        if (pergunta=="N"):
            ka=float(input("\n>Digite o Ka: "))
            R=fraco_forte(CA,ka,A_ou_B)
            print("\n>Concentração de H+=",R[0],"\n>pH=","%.2f" %R[1],"\n\n>Concentração de OH-=",R[2],"\n>pOH=","%.2f" %R[3],"\n\n>Concentração do ácido não ionizado=",R[4],"\n\n>Concentração do íon ácido=",R[5],"\n\n>Concentração do íon básico=",R[6],"\n\n>Explicação: ",R[7])


    if (A_ou_B=="B"):
        if (pergunta=="S"):
            kb=float(input("\n>Digite o Kb: "))
            Ca1=float(input("\n>Digite o coeficiente de atividade do OH-: "))
            Cc1=float(input("\n>Digite o coeficiente de atividade do íon do ácido: "))
            R=fraco_forte_força_ionica(CA,kb,A_ou_B,Ca1,Cc1)
            print("\n>Concentração de H+=",R[0],"\n>pH=","%.2f" %R[1],"\n\n>Concentração de OH-=",R[2],"\n>pOH=","%.2f" %R[3],"\n\n>Concentração da base não ionizada=",R[4],"\n\n>Concentração do íon básico=",R[5],"\n\n>Concentração do íon ácido=",R[6],"\n\n>Explicação: ",R[7])

        if (pergunta=="N"):
            kb=float(input("\n>Digite o Kb: "))
            R=fraco_forte(CA,kb,A_ou_B)
            print("\n>Concentração de H+=",R[0],"\n>pH=","%.2f" %R[1],"\n\n>Concentração de OH-=",R[2],"\n>pOH=","%.2f" %R[3],"\n\n>Concentração da base não ionizada=",R[4],"\n\n>Concentração do íon básico=",R[5],"\n\n>Concentração do íon ácido=",R[6],"\n\n>Explicação: ",R[7])

if (M=="c"):
    CA=float(input("\n>Digite a concetração analítica: "))
    ka=float(input("\n>Digite o Ka: "))
    kb=float(input("\n>Digite o Kb: "))
    if (pergunta=="S"):
        Ca1=float(input("\n>Digite o coeficiente de atividade do H+: "))
        R=fraco_fraco_força_ionica(CA,ka,kb,Ca1)
    if (pergunta=="N"):
        R=fraco_fraco(CA,ka,kb)
    print("\n>Concentração de H+=",R[0],"\n>pH=","%.2f" %R[1],"\n\n>Concentração de OH-=",R[2],"\n>pOH=","%.2f" %R[3],"\n\n>Concentração do ácido não ionizado=",R[4],"\n\n>Concentração do íon ácido=",R[5],"\n\n>Concentração da base não ionizada=",R[6],"\n\n>Concentração do íon básico=",R[7],"\n\n>Explicação: ",R[8])

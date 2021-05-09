import math

def valor_de_x(a,b,c):
    delta=(b**2)-(4*a*c)
    x1=(-(b)+(math.sqrt(delta)))/(2*a)
    return (x1,delta)

def acidos_e_bases_fortes(C,carga,resposta):
    if (C<1e-8):
        return (1e-7,7,1e-7,7,"Não foi adicionado ácido ou base suficiente para alterar o pH da água.")
    if (1e-8<=C<=1e-6):
        K=-((C)*carga)
        x=valor_de_x(1,K,-1e-14)
        y=-(math.log(x[0],10))
        z=(1e-14)/(x[0])
        w=-(math.log(z,10))
        if (resposta=="A"):
            return (x[0],y,z,w,("Foi necessário fazer o tratamento sistemático poís a quantidade de ácido adicionada se apróxima dos valores de H+ proveniente da ionização da água.\n\n>Delta="+str(x[1])))
        if (resposta=="B"):
            return (z,w,x[0],y,("Foi necessário fazer o tratamento sistemático poís a quantidade de base adicionada se apróxima dos valores de OH- proveniente da ionização da água.\n\n>Delta="+str(x[1])))
    if (C>1e-6):
        x=((C)*carga)
        y=-(math.log(x,10))
        z=(1e-14)/(x)
        w=-(math.log(z,10))
        if (resposta=="A"):
            return (x,y,z,w,"Não foi necessário fazer o tratamento sistemático poís a quantidade de ácido adicionada é maior que os valores de H+ proveniente da ionização da água.")
        if (resposta=="B"):
            return (z,w,x,y,"Não foi necessário fazer o tratamento sistemático poís a quantidade de base adicionada é maior que os valores de OH- proveniente da ionização da água.")

def acidos_e_bases_fortes_força_ionica(C,carga,resposta,CH,COH):
    if (C<1e-8):
        return (1e-7,7,1e-7,7,"Não foi adicionado ácido ou base suficiente para alterar o pH da água.")
    if (1e-8<=C<=1e-6):
        K=-((C)*carga)
        x=valor_de_x(1,K,(-1e-14/(CH*COH)))
        if (resposta=="A"):
            Ax=CH*x[0]
            y=-(math.log(Ax,10))
            z=(1e-14)/(Ax)
            w=-(math.log(z,10))
            return (x[0],y,z,w,("Foi necessário fazer o tratamento sistemático poís a quantidade de ácido adicionada se apróxima dos valores de H+ proveniente da ionização da água.\n\n>Delta="+str(x[1])))
        if (resposta=="B"):
            Ax=COH*x[0]
            y=-(math.log(Ax,10))
            z=(1e-14)/(Ax)
            w=-(math.log(z,10))
            return (z,w,x[0],y,("Foi necessário fazer o tratamento sistemático poís a quantidade de base adicionada se apróxima dos valores de OH- proveniente da ionização da água.\n\n>Delta="+str(x[1])))
    if (C>1e-6):
        if (resposta=="A"):
            x=((C)*carga)*CH
            y=-(math.log(x,10))
            z=(1e-14)/(x)
            w=-(math.log(z,10))
            return (x,y,z,w,"Não foi necessário fazer o tratamento sistemático poís a quantidade de ácido adicionada é maior que os valores de H+ proveniente da ionização da água.")
        if (resposta=="B"):
            x=((C)*carga)*COH
            y=-(math.log(x,10))
            z=(1e-14)/(x)
            w=-(math.log(z,10))
            return (z,w,x,y,"Não foi necessário fazer o tratamento sistemático poís a quantidade de base adicionada é maior que os valores de OH- proveniente da ionização da água.")

A_ou_B=input("\n>É um ácido ou uma base (A/B)? ")
CA=float(input("\n>Digite a concetração analítica: "))
c_ion=int(input("\n>Digite a carga do íon: "))

pergunta=input("\n>Deseja considerar a força iônica(S/N)? ")

if (pergunta=="S"):
    Ch=float(input("\n>Digite o coeficiente de atividade de H+: "))
    Coh=float(input("\n>Digite o coeficiente de atividade de OH-: "))
    R=acidos_e_bases_fortes_força_ionica(CA,c_ion,A_ou_B,Ch,Coh)

if (pergunta=="N"):
    R=acidos_e_bases_fortes(CA,c_ion,A_ou_B)

print("\n>Concentração de H+=",R[0],"\n>pH=","%.2f" %R[1],"\n\n>Concentração de OH-=",R[2],"\n>pOH=","%.2f" %R[3],"\n\n>Explicação: ",R[4])


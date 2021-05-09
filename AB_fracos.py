import math

def valor_de_x(a,b,c):
    delta=(b**2)-(4*a*c)
    x1=(-(b)+(math.sqrt(delta)))/(2*a)
    return (x1,delta)

def acidos_e_bases_fracos(C,carga,K,resposta):
    if (K<1e-4):
        x=math.sqrt((C*K)/carga)
        y=-(math.log(x,10))
        z=(1e-14)/(x)
        w=-(math.log(z,10))
        if (resposta=="A"):
            return (x,y,z,w,C,(carga*x),"Como a solução é ácida, podemos desprezar a concentração de OH- no BC (aproximação 1). Coomo o ácido é fraco, podemos desprezar no BM o íon produzido (aproximação 2). Ka=(carga*([H+]^2))/C)")
        if (resposta=="B"):
            return (z,w,x,y,C,(carga*x),"Como a solução é básica, podemos desprezar a concentração de H+ no BC (aproximação 1). Coomo a base é fraca, podemos desprezar no BM o íon produzido (aproximação 2). Kb=(carga*([OH-]^2))/C)")
    if (K>=1e-4):
        x=valor_de_x(carga,K,-(K*C))
        y=-(math.log(x[0],10))
        z=(1e-14)/(x[0])
        w=-(math.log(z,10))
        if (resposta=="A"):
            return (x[0],y,z,w,(C-x[0]),(carga*x[0]),("Como a solução é ácida, podemos desprezar a concentração de OH- no BC (aproximação 1). Como o Ka não é tão baixo, teremos então que fazer o tratamento sistemático. Ka=(carga*([H+]^2))/(C-[H+])\n\n>Delta="+str(x[1])))
        if (resposta=="B"):
            return (z,w,x[0],y,(C-x[0]),(carga*x[0]),("Como a solução é básica podemos desprezar a concentração de H+ no BC (aproximação 1). Como o Kb não é tão baixo, teremos então que fazer o tratamento sistemático. Kb=(carga*([OH-]^2))/(C-[OH-])\n\n>Delta="+str(x[1])))

def acidos_e_bases_fracos_força_ionica(C,carga,K,resposta,CH,COH,Cc):
    if (K<1e-4):
        x=math.sqrt((C*K)/carga)
        y=-(math.log(x,10))
        z=(1e-14)/(x)
        w=-(math.log(z,10))
        if (resposta=="A"):
            x=math.sqrt((C*K)/carga*CH*Cc)
            Ax=(CH*x)
            y=-(math.log(Ax,10))
            z=(1e-14)/(Ax)
            w=-(math.log(z,10))
            return (x,y,z,w,C,(carga*x),"Como a solução é ácida, podemos desprezar a concentração de OH- no BC (aproximação 1). Coomo o ácido é fraco, podemos desprezar no BM o íon produzido (aproximação 2). Ka=(carga*([H+]^2))/C)")
        if (resposta=="B"):
            x=math.sqrt((C*K)/carga*COH*Cc)
            Ax=(COH*x)
            y=-(math.log(Ax,10))
            z=(1e-14)/(Ax)
            w=-(math.log(z,10))
            return (z,w,x,y,C,(carga*x),"Como a solução é básica, podemos desprezar a concentração de H+ no BC (aproximação 1). Coomo a base é fraca, podemos desprezar no BM o íon produzido (aproximação 2). Kb=(carga*([OH-]^2))/C)")
    if (K>=1e-4):
        if (resposta=="A"):
            x=valor_de_x(carga*CH*Cc,K,-(K*C))
            Ax=x*CH
            y=-(math.log(Ax,10))
            z=(1e-14)/(Ax)
            w=-(math.log(z,10))
            return (x[0],y,z,w,(C-x[0]),(carga*x[0]),("Como a solução é ácida, podemos desprezar a concentração de OH- no BC (aproximação 1). Como o Ka não é tão baixo, teremos então que fazer o tratamento sistemático. Ka=(carga*([H+]^2))/(C-[H+])\n\n>Delta="+str(x[1])))
        if (resposta=="B"):
            x=valor_de_x(carga*CH*Cc,K,-(K*C))
            Ax=x*CH
            y=-(math.log(Ax,10))
            z=(1e-14)/(Ax)
            w=-(math.log(z,10))
            return (z,w,x[0],y,(C-x[0]),(carga*x[0]),("Como a solução é básica podemos desprezar a concentração de H+ no BC (aproximação 1). Como o Kb não é tão baixo, teremos então que fazer o tratamento sistemático. Kb=(carga*([OH-]^2))/(C-[OH-])\n\n>Delta="+str(x[1])))

A_ou_B=input("\n>É um ácido ou uma base (A/B)? ")
CA=float(input("\n>Digite a concetração analítica: "))
c_ion=int(input("\n>Digite a carga do íon: "))
Ka_ou_Kb=float(input("\n>Digite o Ka ou o Kb: "))

pergunta=input("\n>Deseja considerar a força iônica(S/N)? ")

if (pergunta=="S"):
    Ch=float(input("\n>Digite o coeficiente de atividade de H+: "))
    Coh=float(input("\n>Digite o coeficiente de atividade de OH-: "))
    CC=float(input("\n>Digite o coeficiente do conjugado: "))
    R=acidos_e_bases_fracos(CA,c_ion,Ka_ou_Kb,A_ou_B,Ch,Coh,CC)

if (pergunta=="N"):
    R=acidos_e_bases_fracos(CA,c_ion,Ka_ou_Kb,A_ou_B)

print("\n>Concentração de H+=",R[0],"\n>pH=","%.2f" %R[1],"\n\n>Concentração de OH-=",R[2],"\n>pOH=","%.2f" %R[3],"\n\n>Concentração da forma não ionizada=",R[4],"\n\n>Concentração da forma ionizada=",R[5],"\n\n>Explicação: ",R[6])

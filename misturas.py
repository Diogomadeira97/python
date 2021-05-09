import math

def valor_de_x(a,b,c):
    delta=(b**2)-(4*a*c)
    x1=(-(b)+(math.sqrt(delta)))/(2*a)
    return (x1,delta)

def forte_e_fraco(C1,C2,K,carga,resposta):
    x=valor_de_x(1,-(C2*carga),-(C1*K))
    y=-(math.log(x[0],10))
    z=(1e-14)/(x[0])
    w=-(math.log(z,10))
    if (resposta=="A"):
        return (x[0],y,z,w,C1,(x[0]-(C2*carga)),C2,"Como a solução é ácida, desprezamos o OH- no BC (aproximação 1) e depois substituimos o BM do ion na expressão encontrada. Em seguida, desprezxamos a forma ionizada no BM do ácido fraco, igualando o ácido fraco à concentração analítica do ácido fraco (aproximação 2). Substituindos os valores em Ka, vamos chegar a uma função do segundo grau que aplicaremos bhaskara para resolver. Utilizamos o valor de H+ encontrado para descobrir a concentração da parte ionizada do ácido fraco (utilizamos a primeira aproximação)")
    if (resposta=="B"):
        return (z,w,x[0],y,C1,(x[0]-(C2*carga)),C2,"Como a solução é básica, desprezamos o H+ no BC (aproximação 1) e depois substituimos o BM do ion na expressão encontrada. Em seguida, desprezxamos o ácido conjugado no BM da base fraca, igualando a base fraca à concentração analítica da base fraca (aproximação 2). Substituindos os valores em Kb, vamos chegar a uma função do segundo grau que aplicaremos bhaskara para resolver. Utilizamos o valor de OH- encontrado para descobrir a concentração do ácido conugado (utilizamos a primeira aproximação)")

def fraco_e_fraco(C1,C2,K1,K2,resposta):
    x=math.sqrt(K1*C1)
    y=-(math.log(x,10))
    z=(1e-14)/(x)
    w=-(math.log(z,10))
    ion=(K2*C2)/x
    if (resposta=="A"):
        return (x,y,z,w,C1,x,C2,ion,"Como a solução é ácida, então o OH- é desprezível em BC (aproximação 1). Comparamos os Kas, o ácido que tiver o Ka menor terá sua parte ionizada desprezada em BC, sendo assim H+ se iguala a parte ionizada do ácido de Ka maior(aproximação 2). Em seguida desconsideramosa a parte ionizada nos BMs, igualando o ácido à sua respectiva concentração analítica (aproximações 4 e 5). Utilizamos os valores encontrados no Ka mais alto para descobrir H+, e em seguida utilizamos o Ka mais baixo para descobrir a concentração da parte ionizada do ácido que falta.")
    if (resposta=="B"):
        return (z,w,x,y,C1,z,C2,ion,"Como a solução é básica, então o H+ é desprezível em BC (aproximação 1). Comparamos os Kbs, a base que tiver o Kb menor terá seu ácido conjugado desprezado em BC, sendo assim OH- se iguala ao ácido conjugado da base de Kb maior(aproximação 2). Em seguida desconsideramosa os ácidos conjugados nos BMs, igualando a base à sua respectiva concentração analítica (aproximações 4 e 5). Utilizamos os valores encontrados no Kb mais alto para descobrir OH-, e em seguida utilizamos o Kb mais baixo para descobrir a concentração do ácido conjugado que falta.")

def menu():
    print("(a)Ácido forte com ácido fraco/base forte com base fraca")
    print("(b)Dois ácido fracos/duas bases fracas")

menu()

M=input()

A_ou_B=input("\n>São ácidos ou bases(A/B)? ")

if (M=="a"):
    if (A_ou_B=="A"):
        Ka=float(input("\n>Digite o Ka: "))
        Ca1=float(input("\n>Digite a concetração analítica referente ao ácido fraco: "))
        Ca2=float(input("\n>Digite a concetração analítica referente ao ácido forte: "))
        c_ion=int(input("\n>Digite a carga do íon do ácido forte: "))
        R=forte_e_fraco(Ca1,Ca2,Ka,c_ion,A_ou_B)
        print("\n>Concentração de H+=",R[0],"\n>pH=","%.2f" %R[1],"\n\n>Concentração de OH-=",R[2],"\n>pOH=","%.2f" %R[3],"\n\n>Concentração do ácido fraco=",R[4],"\n\n>Concentração da base conjugada do ácido fraco=",R[5],"\n\n>Concentração do íon do ácido forte=",R[6],"\n\n>Explicação: ",R[7])
    if (A_ou_B=="B"):
        Kb=float(input("\n>Digite o Kb: "))
        Cb1=float(input("\n>Digite a concetração analítica referente a base fraca: "))
        Cb2=float(input("\n>Digite a concetração analítica referente a base forte: "))
        c_ion=int(input("\n>Digite a carga do íon da base forte: "))
        R=forte_e_fraco(Cb1,Cb2,Kb,c_ion,A_ou_B)
        print("\n>Concentração de H+=",R[0],"\n>pH=","%.2f" %R[1],"\n\n>Concentração de OH-=",R[2],"\n>pOH=","%.2f" %R[3],"\n\n>Concentração da base fraca=",R[4],"\n\n>Concentração do ácido conjugado da base fraca=",R[5],"\n\n>Concentração do íon da base forte=",R[6],"\n\n>Explicação: ",R[7])


if (M=="b"):
    if (A_ou_B=="A"):
        Ka1=float(input("\n>Digite o Ka mais alto: "))
        Ca1=float(input("\n>Digite a concetração analítica referente ao Ka mais alto: "))
        Ka2=float(input("\n>Digite o Ka mais baixo: "))
        Ca2=float(input("\n>Digite a concetração analítica referente ao Ka mais baixo: "))
        R=fraco_e_fraco(Ca1,Ca2,Ka1,Ka2,A_ou_B)
        print("\n>Concentração de H+=",R[0],"\n>pH=","%.2f" %R[1],"\n\n>Concentração de OH-=",R[2],"\n>pOH=","%.2f" %R[3],"\n\n>Concentração do ácido com Ka maior=",R[4],"\n\n>Concentração da base conjugada Ka maior=",R[5],"\n\n>Concentração do ácido com Ka menor=",R[6],"\n\n>Concentração da base conjugada Ka menor=",R[7],"\n\n>Explicação: ",R[8])
    if (A_ou_B=="B"):
        Kb1=float(input("\n>Digite o Kb mais alto: "))
        Cb1=float(input("\n>Digite a concetração analítica referente ao Kb mais alto: "))
        Kb2=float(input("\n>Digite o Kb mais baixo: "))
        Cb2=float(input("\n>Digite a concetração analítica referente ao Kb mais baixo: "))
        R=fraco_e_fraco(Cb1,Cb2,Kb1,Kb2,A_ou_B)
        print("\n>Concentração de H+=",R[0],"\n>pH=","%.2f" %R[1],"\n\n>Concentração de OH-=",R[2],"\n>pOH=","%.2f" %R[3],"\n\n>Concentração da base com Kb maior=",R[4],"\n\n>Concentração do ácido conjugado Kb maior=",R[5],"\n\n>Concentração da base com Kb menor=",R[6],"\n\n>Concentração do ácido conjugado Kb menor=",R[7],"\n\n>Explicação: ",R[8])



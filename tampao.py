import math

def pH_tampao(C,Cs,K,resposta):
    
    if (resposta=="A"):
        x=K*(C/Cs)
        y=-(math.log(x,10))
        z=(1e-14)/(x)
        w=-(math.log(z,10))
        return (x,y,z,w,C,Cs,Cs,"Primeiro utilizamos as equações dos BMs no BC. Feito isso, vemos que as concentrações de H+ e OH- serão despreziveis na equação que acabamos de encontrar e no BC. Dessa forma, o ácido se iguala a concentração analítica do ácido e a base conjugada se iguala a concentração analítica do sal que à possuí. Substituímos os valores no Ka, chegamos na seguinte expresão: [H+] = Ka * (C/Csal), que se desdobra na equação de Henderson-Hasselbalch para cálculo de pH de solução tampão de ácido fraco pH = pKa + log(Csal/C).")
    
    if (resposta=="B"):
        x=K*(Cs/C)
        y=-(math.log(x,10))
        z=(1e-14)/(x)
        w=-(math.log(z,10))
        return (x,y,z,w,C,Cs,Cs,"Primeiro passamos o Kb para Ka usando a relação Ka=Kw/Kb. Utilizamos as equações dos BMs no BC. Feito isso, vemos que as concentrações de H+ e OH- serão despreziveis na equação que acabamos de encontrar e no BC. Dessa forma, a base se iguala a concentração analítica da base e a ácido conjugado se iguala a concentração analítica do sal que à possuí. Substituímos os valores no Ka, chegamos na seguinte expresão: [H+] = Ka * (Csal/C), que se desdobra na equação de Henderson-Hasselbalch para cálculo de pH de solução tampão de base fraca pH = pKa + log(C/Csal).")

def preparo_tampao(C,K,pH,V,P,resposta):

    if (resposta=="A"):
        x=(-math.log(K,10))
        x=pH-x
        x=(10**x)
        y=(C/x)
        mols=(y*V)/1000
        gramas=(mols*P)
        return (y,mols,gramas,"Primeiro descobrimos a concentração de H+ através do pH. Sabendo que a concentração do ácido será igual a concentração analítica, utilizamos o Ka para descobrir a quantidade necessária de base conjugada em mol/L. Feito isso, fazemos umas regra de 3 para descobrir quantos mols são necessários e depois multiplicamos esse valor pelo peso molécular do sal.")

    if (resposta=="B"):
        x=(-math.log(K,10))
        x=pH-x
        x=(10**x)
        y=(x*C)
        mols=((y*V)/1000)
        gramas=(mols*P)
        return (y,mols,gramas,"Primeiro passamos o Kb para Ka usando a relação Ka=Kw/Kb. Depois utilizamos a equação de Henderson-Hasselbalch para descobrir a quantidade necessária de ácido conjugado em mol/L. Feito isso, fazemos umas regra de 3 para descobrir quantos mols são necessários e depois multiplicamos esse valor pelo peso molécular do sal.")

def menu():
    print("(a)pH tampão")
    print("(b)Preparo tampão")

menu()

M=input()

if (M=="a"):
    A_ou_B=input("\n>Tampão de ácido ou base (A/B)? ")
    if (A_ou_B=="A"):
        Ca=float(input("\n>Digite a concetração analítica do ácido: "))
        Cs=float(input("\n>Digite a concetração analítica do sal que possuí a base conjugada: "))
        ka=float(input("\n>Digite o Ka: "))
        R=pH_tampao(Ca,Cs,ka,A_ou_B)
        print("\n>Concentração de H+=",R[0],"\n>pH=","%.2f" %R[1],"\n\n>Concentração de OH-=",R[2],"\n>pOH=","%.2f" %R[3],"\n\n>Concentração do ácido=",R[4],"\n\n>Concentração da base conjugada=",R[5],"\n\n>Concentração do íon do sal=",R[6],"\n\n>Explicação: ",R[7])
        pergunta=input("\n>Deseja adicionar um ácido ou uma base (A/B)? ")
        if (pergunta=="A"):
            Ca2=float(input("\n>Digite a concetração analítica do ácido: "))
            carga=int(input("\n>Digite a carga do íon"))
            C2=Ca+(carga*Ca2)
            Cs2=(Cs+Ca)-(C2)
            R=pH_tampao(C2,Cs2,ka,A_ou_B)
            print("\n>Concentração de H+=",R[0],"\n>pH=","%.2f" %R[1],"\n\n>Concentração de OH-=",R[2],"\n>pOH=","%.2f" %R[3],"\n\n>Concentração do ácido=",R[4],"\n\n>Concentração da base conjugada=",R[5],"\n\n>Concentração do íon do sal=",Cs,"\n\n>Explicação: A adição de um ácido na solução tampão altera o BC, fazendo com que a concentração do ácido aumente e dessa forma a concentração da sua base conjugada diminuí. Isso ocorre poís alteramos o equilíbrio químico no sentido de consumir o H+ adicionado, aumentando assim a forma não ionizada na solução.")
        if (pergunta=="B"):
            Cb2=float(input("\n>Digite a concetração analítica da base: "))
            carga=int(input("\n>Digite a carga do íon"))
            C2=Ca-(carga*Cb2)
            Cs2=(Cs+Ca)-(C2)
            R=pH_tampao(C2,Cs2,ka,A_ou_B)
            print("\n>Concentração de H+=",R[0],"\n>pH=","%.2f" %R[1],"\n\n>Concentração de OH-=",R[2],"\n>pOH=","%.2f" %R[3],"\n\n>Concentração do ácido=",R[4],"\n\n>Concentração da base conjugada=",R[5],"\n\n>Concentração do íon do sal=",Cs,"\n\n>Explicação: A adição de uma base na solução tampão altera o BC, fazendo com que a concentração do ácido diminua e dessa forma a concentração da sua base conjugada aumenta. Isso ocorre poís alteramos o equilíbrio químico no sentido de consumir o OH- adicionado, aumentando assim a forma ionizada na solução.")

    if (A_ou_B=="B"):
        Cb=float(input("\n>Digite a concetração analítica da base: "))
        Cs=float(input("\n>Digite a concetração analítica do sal que possuí o ácido conjugado: "))
        kb=float(input("\n>Digite o Kb: "))
        ka=(1e-14)/kb
        R=pH_tampao(Cb,Cs,ka,A_ou_B)
        print("\n>Concentração de H+=",R[0],"\n>pH=","%.2f" %R[1],"\n\n>Concentração de OH-=",R[2],"\n>pOH=","%.2f" %R[3],"\n\n>Concentração da base=",R[4],"\n\n>Concentração do ácido conjugada=",R[5],"\n\n>Concentração do íon do sal=",R[6],"\n\n>Explicação: ",R[7])
        pergunta=input("\n>Deseja adicionar um ácido ou uma base (A/B)? ")
        if (pergunta=="A"):
            Ca2=float(input("\n>Digite a concetração analítica do ácido: "))
            carga=int(input("\n>Digite a carga do íon"))
            C2=Cb-(carga*Ca2)
            Cs2=(Cs2+Cb)-(C2)
            R=pH_tampao(C2,Cs,ka,A_ou_B)
            print("\n>Concentração de H+=",R[0],"\n>pH=","%.2f" %R[1],"\n\n>Concentração de OH-=",R[2],"\n>pOH=","%.2f" %R[3],"\n\n>Concentração do ácido=",R[4],"\n\n>Concentração da base conjugada=",R[5],"\n\n>Concentração do íon do sal=",Cs,"\n\n>Explicação: A adição de um ácido na solução tampão altera o BC, fazendo com que a concentração da base diminua e dessa forma a concentração de seu ácido conjugado aumenta. Isso ocorre poís alteramos o equilíbrio químico no sentido de consumir o H+ adicionado, aumentando assim o ácido conjugado na solução.")
        if (pergunta=="B"):
            Cb2=float(input("\n>Digite a concetração analítica da base: "))
            carga=int(input("\n>Digite a carga do íon"))
            Cb=Cb+(carga*Cb2)
            Cs2=(Cs+Cb)-(C2)
            R=pH_tampao(C2,Cs2,ka,A_ou_B)
            print("\n>Concentração de H+=",R[0],"\n>pH=","%.2f" %R[1],"\n\n>Concentração de OH-=",R[2],"\n>pOH=","%.2f" %R[3],"\n\n>Concentração do ácido=",R[4],"\n\n>Concentração da base conjugada=",R[5],"\n\n>Concentração do íon do sal=",Cs,"\n\n>Explicação: A adição de uma base na solução tampão altera o BC, fazendo com que a concentração da base aumente e dessa forma a concentração de seu ácido conjugado diminui. Isso ocorre poís alteramos o equilíbrio químico no sentido de consumir o OH- adicionado, aumentando assim a base na solução.")

if (M=="b"):
    A_ou_B=input("\n>Tampão de ácido ou base (A/B)? ")
    if (A_ou_B=="A"):
        Ca=float(input("\n>Digite a concetração analítica da base conjugada: "))
        ka=float(input("\n>Digite o Ka: "))
        PH=float(input("\n>Digite o PH: "))
        volume=float(input("\n>Digite o volume em ml: "))
        peso=float(input("\n>Digite o Peso molecular do sal: "))
        R=preparo_tampao(Ca,ka,PH,volume,peso,A_ou_B)
        print("\n>Concentração=",R[0],"\n\n>Quantidade em mols=",R[1],"\n\n>Quantidade em gramas=",R[2],"\n\n>Explicação: ",R[3])
    if (A_ou_B=="B"):
        Cb=float(input("\n>Digite a concetração analítica do ácido conjugado: "))
        kb=float(input("\n>Digite o Kb: "))
        ka=(1e-14)/kb
        PH=float(input("\n>Digite o PH: "))
        volume=float(input("\n>Digite o volume em ml: "))
        peso=float(input("\n>Digite o Peso molecular do sal: "))
        R=preparo_tampao(Cb,ka,PH,volume,peso,A_ou_B)
        print("\n>Concentração=",R[0],"\n\n>Quantidade em mols=",R[1],"\n\n>Quantidade em gramas=",R[2],"\n\n>Explicação: ",R[3])






    

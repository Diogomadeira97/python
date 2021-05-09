import random

import estrategias1

import estrategias2

def tabuleiro(a,b,c,d,e,f,g,h,i):

    print("")
    print(" ""%s | %s | %s"%(a,b,c))
    print("---+---+---")
    print(" ""%s | %s | %s"%(d,e,f))
    print("---+---+---")
    print(" ""%s | %s | %s"%(g,h,i))

def atacar(x,y,z,pc,player):
    
    if (x==y==pc) and ((z!=pc) and (z!=player)):
        return int(z)-1
    elif (x==z==pc) and ((y!=pc) and (y!=player)):
        return int(y)-1
    elif (y==z==pc) and ((x!=pc) and (x!=player)):
        return int(x)-1
    else:
        return -1
    
def defender(x,y,z,pc,player):
    
    if (x==y==player) and ((z!=pc) and (z!=player)):
        return int(z)-1
    elif (x==z==player) and ((y!=pc) and (y!=player)):
        return int(y)-1
    elif (y==z==player) and ((x!=pc) and (x!=player)):
        return int(x)-1
    else:
        return -1
    
def jogadas_pc(a,b,c,d,e,f,g,h,i,pc,player,rodada):

    tabuleiro=[a,b,c,d,e,f,g,h,i]
    
    if atacar(a,b,c,pc,player) != -1:
        return atacar(a,b,c,pc,player)
    elif atacar(a,d,g,pc,player) != -1:
        return atacar(a,d,g,pc,player)
    elif atacar(a,e,i,pc,player) != -1:
        return atacar(a,e,i,pc,player)
    elif atacar(b,e,h,pc,player) != -1:
        return atacar(b,e,h,pc,player)
    elif atacar(c,f,i,pc,player) != -1:
        return atacar(c,f,i,pc,player)
    elif atacar(c,e,g,pc,player) != -1:
        return atacar(c,e,g,pc,player)
    elif atacar(d,e,f,pc,player) != -1:
        return atacar(d,e,f,pc,player)
    elif atacar(g,h,i,pc,player) != -1:
        return atacar(g,h,i,pc,player)

    elif defender(a,b,c,pc,player) != -1:
        return defender(a,b,c,pc,player)
    elif defender(a,d,g,pc,player) != -1:
        return defender(a,d,g,pc,player)
    elif defender(a,e,i,pc,player) != -1:
        return defender(a,e,i,pc,player)
    elif defender(b,e,h,pc,player) != -1:
        return defender(b,e,h,pc,player)
    elif defender(c,f,i,pc,player) != -1:
        return defender(c,f,i,pc,player)
    elif defender(c,e,g,pc,player) != -1:
        return defender(c,e,g,pc,player)
    elif defender(d,e,f,pc,player) != -1:
        return defender(d,e,f,pc,player)
    elif defender(g,h,i,pc,player) != -1:
        return defender(g,h,i,pc,player)

    elif ((rodada==2) or (rodada==4) or (rodada==6)) and (estrategias1.estrategia(a,b,c,d,e,f,g,h,i,pc,player,rodada) != -1):
            return estrategias1.estrategia(a,b,c,d,e,f,g,h,i,pc,player,rodada)
    elif ((rodada==3) or (rodada==5) or (rodada==7)) and (estrategias2.estrategia(a,b,c,d,e,f,g,h,i,pc,player,rodada) != -1):
            return estrategias2.estrategia(a,b,c,d,e,f,g,h,i,pc,player,rodada)
    
    else:
        r=str(random.randint(1,9))
        while r not in tabuleiro: 
            r=str(random.randint(1,9))
        r=int(r)-1
        return r

def analise(a,b,c,d,e,f,g,h,i,rodada2,jogadainicial2):
    j=[a,b,c,d,e,f,g,h,i]
    casaslivres=0
    for i in range(len(j)):
        if str(i+1) in j:
            casaslivres=casaslivres+1
            
    if (j[0]==j[1]==j[2]) or (j[0]==j[3]==j[6]) or (j[0]==j[4]==j[8]) or (j[1]==j[4]==j[7]) or (j[2]==j[5]==j[8]) or (j[2]==j[4]==j[6]) or (j[3]==j[4]==j[5]) or (j[6]==j[7]==j[8]):
        if (jogadainicial2=="N"):
            if (rodada2==1) or (rodada2==3) or (rodada2==5) or (rodada2==7) or (rodada2==9):
                return 0
            elif (rodada2==2) or (rodada2==4) or (rodada2==6) or (rodada2==8):
                return 1
        elif (jogadainicial2=="S"):
            if (rodada2==1) or (rodada2==3) or (rodada2==5) or (rodada2==7) or (rodada2==9):
                return 1
            elif (rodada2==2) or (rodada2==4) or (rodada2==6) or (rodada2==8):
                return 0
        
    elif (casaslivres==0) and (rodada2==9):
        return 2
    
    else:
        return -1
    

import random

def jogada2_canto_central(x,y,z,w,k,pc,player):
    r=[y,z,w,k]
    r1=r[random.randint(0,3)]
    if(x==player):
        return int(r1)-1
    else:
        return -1
    
def jogada2_canto(x,y,z,w,k,player):
    if (x==player) or (y==player) or (z==player) or (w==player):
        return int(k)-1
    else:
        return -1

def jogada2_centro(x,y,z,w,k,player):
    
    r=[x,z,w,k]
    r1=r[random.randint(0,3)]
    if (y==player):
        return int(r1)-1
    else:
        return -1

def jogada4_canto_central1(x,y,z,w,k,pc,player):
    r=[w,k]
    r1=r[random.randint(0,1)]
    if (x==player) and (y==player) and (z==pc):
        return int(r1)-1
    else:
        return -1
    
def jogada4_canto_central2(x,y,z,w,k,pc,player):
    r=[w,k]
    r1=r[random.randint(0,1)]    
    if (x==player) and (y==pc) and (z==player):
        return int(r1)-1
    else:
        return -1
    
def jogada4_canto_central3(x,y,z,w,k,pc,player):
    if (x==player) and (y==player) and (z==pc):
        return int(k)-1
    if (x==player) and (w==player) and (k==pc):
        return int(z)-1
    else:
        return -1
    
def jogada4_canto_central4(a,b,c,d,e,f,g,h,pc,player):
    r=[e,f,g,h]
    r1=r[random.randint(0,1)]
    r2=r[random.randint(2,3)]
    if (a==player) and (b==pc) and (c==player):
        return int(r1)-1
    if (a==player) and (b==pc) and (d==player):
        return int(r2)-1
    else:
        return -1
    
def jogada4_canto_central5(x,y,z,w,k,pc,player):
    if (x==player) and (y==player) and (z==pc):
        return int(w)-1
    if (x==pc) and (y==player) and (z==player):
        return int(k)-1
    else:
        return -1
def jogada4_canto_central6(x,y,z,w,k,pc,player):
    if (x==player) and (y==player) and (z==pc):
        return int(w)-1
    if (x==player) and (z==player) and (y==pc):
        return int(k)-1
    else:
        return -1

def jogada4_canto_central7(x,y,z,w,pc,player):
    if (x==player) and (y==player) and (z==pc):
        return int(w)-1
    else:
        return -1
    
def jogada4_canto_central8(x,y,z,w,k,pc,player):
    if (x==player) and (y==player) and (w==pc):
        return int(z)-1
    elif (x==player) and (k==pc) and (z==player):
        return int(y)-1
    else:
        return -1

def jogada4_canto_central9(x,y,z,w,k,j,pc,player):
    if (x==player) and (y==player) and (z==pc):
        return int(w)-1
    elif (x==player) and (k==player) and (j==pc):
        return int(w)-1
    else:
        return -1

def jogada4_canto_central10(x,y,z,w,k,j,pc,player):
    if (x==player) and (y==player) and (z==pc):
        return int(w)-1
    elif (x==player) and (k==player) and (z==pc):
        return int(j)-1
    else:
        return -1

def jogada4_canto1(x,y,z,w,k,pc,player):
    if ((x==player) and (z==pc)) and ((y==player) or (w==player)):
        return int(k)-1
    else:
        return -1
    
def jogada4_canto2(a,b,c,d,e,f,g,h,i,pc,player):
    r=[b,d,f,h]
    r1=r[random.randint(0,3)]
    if ((a==player) and (e==pc) and (i==player)) or ((g==player) and (e==pc) and (c==player)):
        return int(r1)-1
    else:
        return -1
    

def jogada4_centro(x,y,z,w,k,pc,player):
    r=[x,z,w,k]
    r1=r[random.randint(2,3)]
    r2=r[random.randint(0,1)]
    if ((x==pc) and (y==player) and (z==player)) or ((x==player) and (y==player) and (z==pc)):
        return int(r1)-1
    elif ((k==pc) and (y==player) and (w==player)) or ((k==player) and (y==player) and (w==pc)):
        return int(r2)-1
    else:
        return -1
    
def jogada6_canto_central1(a,b,c,d,e,f,g,pc,player):
    r=[f,g]
    r1=r[random.randint(0,1)]
    if(a==player)and (b==player) and (c==player) and (d==pc) and (e==pc):
        return int(r1)-1
    else:
        return -1

def jogada6_canto_central2(a,b,c,d,e,f,g,h,pc,player):
    r=[f,g]
    r1=r[random.randint(0,1)]
    p=[f,e]
    p1=p[random.randint(0,1)]
    if(a==player)and (b==player) and (c==pc) and (d==pc) and (e==player):
        return int(r1)-1
    if(a==player)and (b==pc) and (c==player) and (h==pc) and (g==player):
        return int(p1)-1
    else:
        return -1

def jogada6_canto_central3(x,y,z,w,k,j,pc,player):
    if(x==player)and (y==player) and (z==pc) and (w==pc) and (k==player):
        return int(j)-1
    if(x==pc)and (y==pc) and (z==player) and (w==player) and (k==player):
        return int(j)-1
    else:
        return -1

def jogada2(a,b,c,d,e,f,g,h,i,pc,player):

    if (jogada2_canto(a,c,g,i,e,player))!= -1:
        return jogada2_canto(a,c,g,i,e,player)
    
    elif (jogada2_centro(a,e,i,c,g,player)) != -1:
        return jogada2_centro(a,e,i,c,g,player)

    elif (jogada2_canto_central(d,a,e,f,g,pc,player)) != -1:
        return jogada2_canto_central(d,a,e,f,g,pc,player)
    elif (jogada2_canto_central(b,c,e,h,a,pc,player)) != -1:
        return jogada2_canto_central(b,c,e,h,a,pc,player)
    elif (jogada2_canto_central(f,i,e,d,c,pc,player)) != -1:
        return jogada2_canto_central(f,i,e,d,c,pc,player)
    elif (jogada2_canto_central(h,g,e,b,i,pc,player)) != -1:
        return jogada2_canto_central(h,g,e,b,i,pc,player)

    else:
        return -1
    
def jogada4(a,b,c,d,e,f,g,h,i,pc,player):
    
    if (jogada4_canto1(a,h,e,f,i,pc,player)) != -1:
        return jogada4_canto1(a,h,e,f,i,pc,player)
    elif (jogada4_canto1(c,h,e,d,g,pc,player)) != -1:
        return jogada4_canto1(c,h,e,d,g,pc,player)
    elif (jogada4_canto1(i,b,e,d,a,pc,player)) != -1:
        return jogada4_canto1(i,b,e,d,a,pc,player)
    elif (jogada4_canto1(g,b,e,f,c,pc,player)) != -1:
        return jogada4_canto1(g,b,e,f,c,pc,player)

    elif (jogada4_canto2(a,b,c,d,e,f,g,h,i,pc,player)) != -1:
        return jogada4_canto2(a,b,c,d,e,f,g,h,i,pc,player)


    elif (jogada4_centro(a,e,i,c,g,pc,player)) != -1:
        return jogada4_centro(a,e,i,c,g,pc,player)

    elif (jogada4_canto_central1(d,e,f,a,g,pc,player)) != -1:
        return jogada4_canto_central1(d,e,f,a,g,pc,player)
    elif (jogada4_canto_central1(b,e,h,a,c,pc,player)) != -1:
        return jogada4_canto_central1(b,e,h,a,c,pc,player)
    elif (jogada4_canto_central1(f,e,d,c,i,pc,player)) != -1:
        return jogada4_canto_central1(f,e,d,c,i,pc,player)
    elif (jogada4_canto_central1(h,e,b,g,i,pc,player)) != -1:
        return jogada4_canto_central1(h,e,b,g,i,pc,player)

    elif (jogada4_canto_central2(d,e,f,b,h,pc,player)) != -1:
        return jogada4_canto_central2(d,e,f,b,h,pc,player)
    elif (jogada4_canto_central2(b,e,h,d,f,pc,player)) != -1:
        return jogada4_canto_central2(b,e,h,d,f,pc,player)

    elif (jogada4_canto_central3(d,b,c,h,i,pc,player)) != -1:
        return jogada4_canto_central3(d,b,c,h,i,pc,player)
    elif (jogada4_canto_central3(b,f,i,d,g,pc,player)) != -1:
        return jogada4_canto_central3(b,f,i,d,g,pc,player)
    elif (jogada4_canto_central3(f,h,g,b,a,pc,player)) != -1:
        return jogada4_canto_central3(f,h,g,b,a,pc,player)
    elif (jogada4_canto_central3(h,d,a,f,c,pc,player)) != -1:
        return jogada4_canto_central3(h,d,a,f,c,pc,player)

    elif (jogada4_canto_central4(d,e,b,h,a,c,g,i,pc,player)) != -1:
        return jogada4_canto_central4(d,e,b,h,a,c,g,i,pc,player)
    elif (jogada4_canto_central4(b,e,f,d,c,i,a,g,pc,player)) != -1:
        return jogada4_canto_central4(b,e,f,d,c,i,a,g,pc,player)
    elif (jogada4_canto_central4(f,e,h,b,i,g,c,a,pc,player)) != -1:
        return jogada4_canto_central4(f,e,h,b,i,g,c,a,pc,player)
    elif (jogada4_canto_central4(h,e,d,f,g,a,i,c,pc,player)) != -1:
        return jogada4_canto_central4(h,e,d,f,g,a,i,c,pc,player)

    elif (jogada4_canto_central5(d,h,f,g,i,pc,player)) != -1:
        return jogada4_canto_central5(d,h,f,g,i,pc,player)
    elif (jogada4_canto_central5(b,d,h,a,g,pc,player)) != -1:
        return jogada4_canto_central5(b,d,h,a,g,pc,player)
    elif (jogada4_canto_central5(f,b,d,c,a,pc,player)) != -1:
        return jogada4_canto_central5(f,b,d,c,a,pc,player)
    elif (jogada4_canto_central5(h,f,b,i,c,pc,player)) != -1:
        return jogada4_canto_central5(h,f,b,i,c,pc,player)

    elif (jogada4_canto_central6(d,g,a,b,h,pc,player)) != -1:
        return jogada4_canto_central6(d,g,a,b,h,pc,player)
    elif (jogada4_canto_central6(b,a,c,f,d,pc,player)) != -1:
        return jogada4_canto_central6(b,a,c,f,d,pc,player)
    elif (jogada4_canto_central6(f,c,i,h,b,pc,player)) != -1:
        return jogada4_canto_central6(f,c,i,h,b,pc,player)
    elif (jogada4_canto_central6(h,i,g,d,f,pc,player)) != -1:
        return jogada4_canto_central6(h,i,g,d,f,pc,player)

    elif (jogada4_canto_central7(d,b,a,e,pc,player)) != -1:
        return jogada4_canto_central7(d,b,a,e,pc,player)
    elif (jogada4_canto_central7(b,f,c,e,pc,player)) != -1:
        return jogada4_canto_central7(b,f,c,e,pc,player)
    elif (jogada4_canto_central7(f,h,i,e,pc,player)) != -1:
        return jogada4_canto_central7(f,h,i,e,pc,player)
    elif (jogada4_canto_central7(h,d,g,e,pc,player)) != -1:
        return jogada4_canto_central7(h,d,g,e,pc,player)

    elif (jogada4_canto_central8(d,c,i,g,a,pc,player)) != -1:
        return jogada4_canto_central8(d,c,i,g,a,pc,player)
    elif (jogada4_canto_central8(b,i,g,a,c,pc,player)) != -1:
        return jogada4_canto_central8(b,i,g,a,c,pc,player)
    elif (jogada4_canto_central8(f,g,a,c,i,pc,player)) != -1:
        return jogada4_canto_central8(f,g,a,c,i,pc,player)
    elif (jogada4_canto_central8(h,a,c,i,g,pc,player)) != -1:
        return jogada4_canto_central8(h,a,c,i,g,pc,player)

    elif (jogada4_canto_central9(d,c,a,e,i,g,pc,player)) != -1:
        return jogada4_canto_central9(d,c,a,e,i,g,pc,player)
    elif (jogada4_canto_central9(b,i,c,e,g,a,pc,player)) != -1:
        return jogada4_canto_central9(b,i,c,e,g,a,pc,player)
    elif (jogada4_canto_central9(f,g,i,e,a,c,pc,player)) != -1:
        return jogada4_canto_central9(f,g,i,e,a,c,pc,player)
    elif (jogada4_canto_central9(h,a,g,e,c,i,pc,player)) != -1:
        return jogada4_canto_central9(h,a,g,e,c,i,pc,player)

    elif (jogada4_canto_central10(d,c,f,a,i,g,pc,player)) != -1:
        return jogada4_canto_central10(d,c,f,a,i,g,pc,player)
    elif (jogada4_canto_central10(b,i,h,c,g,a,pc,player)) != -1:
        return jogada4_canto_central10(b,i,h,c,g,a,pc,player)
    elif (jogada4_canto_central10(f,g,d,i,a,c,pc,player)) != -1:
        return jogada4_canto_central10(f,g,d,i,a,c,pc,player)
    elif (jogada4_canto_central10(h,a,b,g,c,i,pc,player)) != -1:
        return jogada4_canto_central10(h,a,b,g,c,i,pc,player)
    
    else:
        return -1
    
def jogada6(a,b,c,d,e,f,g,h,i,pc,player):

    if (jogada6_canto_central1(d,b,f,e,h,g,i,pc,player)) != -1:
        return jogada6_canto_central1(d,b,f,e,h,g,i,pc,player)
    if (jogada6_canto_central1(b,f,h,e,d,a,g,pc,player)) != -1:
        return jogada6_canto_central1(b,f,h,e,d,a,g,pc,player)
    if (jogada6_canto_central1(f,h,d,e,b,a,c,pc,player)) != -1:
        return jogada6_canto_central1(f,h,d,e,b,a,c,pc,player)
    if (jogada6_canto_central1(b,d,h,e,f,c,i,pc,player)) != -1:
        return jogada6_canto_central1(b,d,h,e,f,c,i,pc,player)

    elif (jogada6_canto_central2(d,c,i,g,h,e,b,a,pc,player)) != -1:
        return jogada6_canto_central2(d,c,i,g,h,e,b,a,pc,player)
    elif (jogada6_canto_central2(b,i,g,a,d,e,f,c,pc,player)) != -1:
        return jogada6_canto_central2(b,i,g,a,d,e,f,c,pc,player)
    elif (jogada6_canto_central2(f,g,a,c,b,e,h,i,pc,player)) != -1:
        return jogada6_canto_central2(f,g,a,c,b,e,h,i,pc,player)
    elif (jogada6_canto_central2(h,a,c,i,f,e,d,g,pc,player)) != -1:
        return jogada6_canto_central2(h,a,c,i,f,e,d,g,pc,player)

    elif (jogada6_canto_central3(d,c,a,f,h,e,pc,player)) != -1:
        return jogada6_canto_central3(d,c,a,f,h,e,pc,player)
    elif (jogada6_canto_central3(b,i,c,h,d,e,pc,player)) != -1:
        return jogada6_canto_central3(b,i,c,h,d,e,pc,player)
    elif (jogada6_canto_central3(f,g,i,d,b,e,pc,player)) != -1:
        return jogada6_canto_central3(f,g,i,d,b,e,pc,player)
    elif (jogada6_canto_central3(h,a,g,b,f,e,pc,player)) != -1:
        return jogada6_canto_central3(h,a,g,b,f,e,pc,player)
    
    else:
        return -1
    
def estrategia(a,b,c,d,e,f,g,h,i,pc,player,rodada):
    
    if (rodada==2) and (jogada2(a,b,c,d,e,f,g,h,i,pc,player)) != -1:
        return jogada2(a,b,c,d,e,f,g,h,i,pc,player)
    
    elif (rodada==4) and (jogada4(a,b,c,d,e,f,g,h,i,pc,player)) != -1:
        return jogada4(a,b,c,d,e,f,g,h,i,pc,player)
    
    elif (rodada==6) and (jogada6(a,b,c,d,e,f,g,h,i,pc,player)) != -1:
        return jogada6(a,b,c,d,e,f,g,h,i,pc,player)
    
    else:
        return -1

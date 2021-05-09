import random

def jogada3_centro1(x,y,z,pc,player):
    if (x==player) and (y==pc):
        return int(z)-1
    else:
        return -1

def jogada3_centro2(x,y,z,w,pc,player):
    r=[z,w]
    r1=r[random.randint(0,1)]
    if (x==player) and (y==pc):
        return int(r1)-1
    else:
        return -1

def jogada3_canto1(a,b,c,d,e,f,g,h,i,pc,player):
    if ((a==pc) or (c==pc) or (g==pc) or (i==pc)) and ((b==player) or (d==player) or (f==player) or (h==player)):
        return int(e)-1
    else:
        return -1

def jogada3_canto2(x,y,z,pc,player):
    if (x==pc) and (y==player):
        return int(z)-1
    else:
        return -1

def jogada3_canto3(x,y,z,w,pc,player):
    if (x==pc) and ((z==player) or (w==player)):
        return int(y)-1
    else:
        return -1

def jogada3_canto4(x,y,z,pc,player):
    if (x==pc) and (z==player):
        return int(y)-1
    else:
        return -1

def jogada3_canto_central1(x,y,z,w,pc,player):
    if ((x==pc) and (y==player)) or ((x==pc) and (z==player)):
        return int(w)-1
    else:
        return -1

def jogada3_canto_central2(x,y,z,w,k,pc,player):
    if (x==pc) and (w==player):
        return int(y)-1
    if (x==pc) and (k==player):
        return int(z)-1
    else:
        return -1

def jogada3_canto_central3(x,y,z,w,k,pc,player):
    if (x==pc) and (y==player):
        return int(w)-1
    if (x==pc) and (z==player):
        return int(k)-1
    else:
        return -1

def jogada3_canto_central4(x,y,z,w,pc,player):
    r=[z,w]
    r1=r[random.randint(0,1)]
    if (x==pc) and (y==player):
        return int(r1)-1
    else:
        return -1
    
def jogada3_canto_central5(x,y,z,w,pc,player):
    r=[z,w]
    r1=r[random.randint(0,1)]
    if (x==pc) and (y==player):
        return int(r1)-1
    else:
        return -1
    
def jogada5_centro(a,b,c,d,e,f,g,pc,player):
    if (a==player) and (b==pc) and (c==pc) and (d==player):
        return int(e)-1
    elif (f==player) and (b==pc) and (e==pc) and (g==player):
        return int(c)-1
    else:
        return -1

def jogada5_canto_central1(a,b,c,d,e,f,g,pc,player):
    if (a==pc) and (b==pc) and (e==player) and (f==player):
        return int(c)-1
    elif (a==pc) and (b==pc) and (g==player) and (f==player):
        return int(d)-1
    else:
        return -1

def jogada5_canto_central2(a,b,c,d,e,f,g,h,i,pc,player):
    r=[e,f]
    r1=r[random.randint(0,1)] 
    if ((d==pc) and (c==pc) and (a==player) and (b==player)) or ((d==pc) and (i==pc) and (g==player) and (h==player)):
        return int(r1)-1
    else:
        return -1

def jogada5_canto_central3(a,b,c,d,e,f,g,h,i,pc,player):
    r=[e,f]
    r1=r[random.randint(0,1)] 
    if ((d==pc) and (c==pc) and (a==player) and (h==player)) or ((d==pc) and (i==pc) and (g==player) and (b==player)):
        return int(r1)-1
    else:
        return -1

def jogada5_canto_central4(x,y,z,w,k,j,pc,player):
    if ((x==pc) and (w==player) and (k==player)) and ((y==pc) or (z==pc)):
        return int(j)-1
    else:
        return -1

def jogada5_canto_central5(a,b,c,d,e,f,g,pc,player):
    if ((a==pc) and (b==pc) and (c==player)) and ((d==player) or (e==player)):
        return int(f)-1
    elif ((a==pc) and (e==pc) and (c==player)) and ((d==player) or (b==player)):
        return int(g)-1
    else:
        return -1

def jogada5_canto_central6(a,b,c,d,e,f,g,h,pc,player):
    if (a==pc) and (b==player) and (c==pc) and (d==player):
        return int(e)-1
    elif (a==pc) and (b==player) and (f==pc) and (f==player):
        return int(h)-1
    else:
        return -1

def jogada5_canto_central7(a,b,c,d,e,f,g,h,i,pc,player):
    if ((c==pc) and (d==pc) and (f==player)) and ((e==player) or (h==player) or (i==player)):
        return int(a)-1
    elif ((d==pc) and (f==pc) and (i==player)) and ((e==player) or (b==player) or (c==player)):
        return int(g)-1
    else:
        return -1

def jogada5_canto_central8(a,b,c,d,e,f,g,pc,player):
    if (a==pc) and (b==pc) and (c==player) and (d==player):
        return int(e)-1
    elif (a==pc) and (f==pc) and (c==player) and (g==player):
        return int(e)-1
    else:
        return -1

def jogada7_canto_central1(a,b,c,d,e,f,g,h,i,pc,player):
    if (d==pc) and (e==pc) and (c==pc) and (f==player) and (h==player) and (g==player):
        return int(a)-1
    elif (d==pc) and (e==pc) and (i==pc) and (f==player) and (b==player) and (a==player):
        return int(g)-1
    else:
        return -1

def jogada7_canto_central2(a,b,c,d,e,f,g,h,i,pc,player):
    if (d==pc) and (e==pc) and (c==pc) and (f==player) and (i==player) and (g==player):
        return int(b)-1
    elif (d==pc) and (e==pc) and (i==pc) and (f==player) and (c==player) and (a==player):
        return int(h)-1
    else:
        return -1
    
def jogada3(a,b,c,d,e,f,g,h,i,pc,player):

    if (jogada3_centro1(a,e,i,pc,player)) != -1:
        return jogada3_centro1(a,e,i,pc,player)
    elif (jogada3_centro1(c,e,g,pc,player)) != -1:
        return jogada3_centro1(c,e,g,pc,player) 
    elif (jogada3_centro1(i,e,a,pc,player)) != -1:
        return jogada3_centro1(i,e,a,pc,player)
    elif (jogada3_centro1(g,e,c,pc,player)) != -1:
        return jogada3_centro1(g,e,c,pc,player)

    elif (jogada3_centro2(b,e,g,i,pc,player)) != -1:
        return jogada3_centro2(b,e,g,i,pc,player)
    elif (jogada3_centro2(f,e,a,g,pc,player)) != -1:
        return jogada3_centro2(f,e,a,g,pc,player) 
    elif (jogada3_centro2(h,e,c,a,pc,player)) != -1:
        return jogada3_centro2(h,e,c,a,pc,player)
    elif (jogada3_centro2(d,e,i,c,pc,player)) != -1:
        return jogada3_centro2(d,e,i,c,pc,player)

    elif (jogada3_canto1(a,b,c,d,e,f,g,h,i,pc,player)) != -1:
        return jogada3_canto1(a,b,c,d,e,f,g,h,i,pc,player)

    elif (jogada3_canto2(a,i,e,pc,player)) != -1:
        return jogada3_canto2(a,i,e,pc,player)
    elif (jogada3_canto2(c,g,e,pc,player)) != -1:
        return jogada3_canto2(c,g,e,pc,player)
    elif (jogada3_canto2(i,a,e,pc,player)) != -1:
        return jogada3_canto2(i,a,e,pc,player)
    elif (jogada3_canto2(g,c,e,pc,player)) != -1:
        return jogada3_canto2(g,c,e,pc,player)

    elif (jogada3_canto3(a,i,c,g,pc,player)) != -1:
        return jogada3_canto3(a,i,c,g,pc,player)
    elif (jogada3_canto3(c,g,i,a,pc,player)) != -1:
        return jogada3_canto3(c,g,i,a,pc,player)
    elif (jogada3_canto3(i,a,g,c,pc,player)) != -1:
        return jogada3_canto3(i,a,g,c,pc,player)
    elif (jogada3_canto3(g,c,a,i,pc,player)) != -1:
        return jogada3_canto2(g,c,e,pc,player)

    elif (jogada3_canto4(a,i,e,pc,player)) != -1:
        return jogada3_canto4(a,i,e,pc,player)
    elif (jogada3_canto4(c,g,e,pc,player)) != -1:
        return jogada3_canto4(c,g,e,pc,player)
    elif (jogada3_canto4(i,a,e,pc,player)) != -1:
        return jogada3_canto4(i,a,e,pc,player)
    elif (jogada3_canto4(g,c,e,pc,player)) != -1:
        return jogada3_canto4(g,c,e,pc,player)

    elif (jogada3_canto_central1(d,b,h,e,pc,player)) != -1:
        return jogada3_canto_central1(d,b,h,e,pc,player)
    elif (jogada3_canto_central1(b,d,f,e,pc,player)) != -1:
        return jogada3_canto_central1(b,d,f,e,pc,player)
    elif (jogada3_canto_central1(f,b,h,e,pc,player)) != -1:
        return jogada3_canto_central1(f,b,h,e,pc,player)
    elif (jogada3_canto_central1(h,f,d,e,pc,player)) != -1:
        return jogada3_canto_central1(h,f,d,e,pc,player)

    elif (jogada3_canto_central2(d,c,i,a,g,pc,player)) != -1:
        return jogada3_canto_central2(d,c,i,a,g,pc,player)
    elif (jogada3_canto_central2(b,i,g,c,a,pc,player)) != -1:
        return jogada3_canto_central2(b,i,g,c,a,pc,player)
    elif (jogada3_canto_central2(f,g,a,i,c,pc,player)) != -1:
        return jogada3_canto_central2(f,g,a,i,c,pc,player)
    elif (jogada3_canto_central2(h,a,c,g,i,pc,player)) != -1:
        return jogada3_canto_central2(h,a,c,g,i,pc,player)

    elif (jogada3_canto_central3(d,c,i,a,g,pc,player)) != -1:
        return jogada3_canto_central3(d,c,i,a,g,pc,player)
    elif (jogada3_canto_central3(b,i,g,c,a,pc,player)) != -1:
        return jogada3_canto_central3(b,i,g,c,a,pc,player)
    elif (jogada3_canto_central3(f,g,a,i,c,pc,player)) != -1:
        return jogada3_canto_central3(f,g,a,i,c,pc,player)
    elif (jogada3_canto_central3(h,a,c,g,i,pc,player)) != -1:
        return jogada3_canto_central3(h,a,c,g,i,pc,player)

    elif (jogada3_canto_central4(d,e,b,h,pc,player)) != -1:
        return jogada3_canto_central4(d,e,b,h,pc,player)
    elif (jogada3_canto_central4(b,e,f,d,pc,player)) != -1:
        return jogada3_canto_central4(b,e,f,d,pc,player)
    elif (jogada3_canto_central4(f,e,h,b,pc,player)) != -1:
        return jogada3_canto_central4(f,e,h,b,pc,player)
    elif (jogada3_canto_central4(h,e,d,f,pc,player)) != -1:
        return jogada3_canto_central4(h,e,d,f,pc,player)

    elif (jogada3_canto_central5(d,f,c,i,pc,player)) != -1:
        return jogada3_canto_central5(d,f,c,i,pc,player)
    elif (jogada3_canto_central5(b,h,i,g,pc,player)) != -1:
        return jogada3_canto_central5(b,h,i,g,pc,player)
    elif (jogada3_canto_central5(f,d,g,a,pc,player)) != -1:
        return jogada3_canto_central5(f,d,g,a,pc,player)
    elif (jogada3_canto_central5(h,b,a,c,pc,player)) != -1:
        return jogada3_canto_central5(h,b,a,c,pc,player)

    else:
        return -1

def jogada5(a,b,c,d,e,f,g,h,i,pc,player):
    
    if (jogada5_centro(a,e,i,h,c,g,b,pc,player)) != -1:
        return jogada5_centro(a,e,i,h,c,g,b,pc,player)
    elif (jogada5_centro(c,e,g,d,i,a,f,pc,player)) != -1:
        return jogada5_centro(c,e,g,d,i,a,f,pc,player) 
    elif (jogada5_centro(i,e,a,b,g,c,h,pc,player)) != -1:
        return jogada5_centro(i,e,a,b,g,c,h,pc,player)
    elif (jogada5_centro(g,e,c,f,a,i,d,pc,player)) != -1:
        return jogada5_centro(g,e,c,f,a,i,d,pc,player)

    elif (jogada5_canto_central1(d,e,a,g,b,f,h,pc,player)) != -1:
        return jogada5_canto_central1(d,e,a,g,b,f,h,pc,player)
    elif (jogada5_canto_central1(b,e,c,a,f,h,d,pc,player)) != -1:
        return jogada5_canto_central1(b,e,c,a,f,h,d,pc,player)
    elif (jogada5_canto_central1(f,e,i,c,h,d,b,pc,player)) != -1:
        return jogada5_canto_central1(f,e,i,c,h,d,b,pc,player)
    elif (jogada5_canto_central1(h,e,g,i,d,b,f,pc,player)) != -1:
        return jogada5_canto_central1(h,e,g,i,d,b,f,pc,player)

    elif (jogada5_canto_central2(a,b,c,d,e,f,g,h,i,pc,player)) != -1:
        return jogada5_canto_central2(a,b,c,d,e,f,g,h,i,pc,player)
    elif (jogada5_canto_central2(c,f,i,b,e,h,a,d,g,pc,player)) != -1:
        return jogada5_canto_central2(c,f,i,b,e,h,a,d,g,pc,player)
    elif (jogada5_canto_central2(i,h,g,f,e,d,c,b,a,pc,player)) != -1:
        return jogada5_canto_central2(i,h,g,f,e,d,c,b,a,pc,player)
    elif (jogada5_canto_central2(g,d,a,h,e,b,i,f,c,pc,player)) != -1:
        return jogada5_canto_central2(g,d,a,h,e,b,i,f,c,pc,player)

    elif (jogada5_canto_central3(a,b,c,d,e,f,g,h,i,pc,player)) != -1:
        return jogada5_canto_central3(a,b,c,d,e,f,g,h,i,pc,player)
    elif (jogada5_canto_central3(c,f,i,b,e,h,a,d,g,pc,player)) != -1:
        return jogada5_canto_central3(c,f,i,b,e,h,a,d,g,pc,player)
    elif (jogada5_canto_central3(i,h,g,f,e,d,c,b,a,pc,player)) != -1:
        return jogada5_canto_central3(i,h,g,f,e,d,c,b,a,pc,player)
    elif (jogada5_canto_central3(g,d,a,h,e,b,i,f,c,pc,player)) != -1:
        return jogada5_canto_central3(g,d,a,h,e,b,i,f,c,pc,player)

    elif (jogada5_canto_central4(d,c,i,a,g,f,pc,player)) != -1:
        return jogada5_canto_central4(d,c,i,a,g,f,pc,player)
    elif (jogada5_canto_central4(b,i,g,c,a,h,pc,player)) != -1:
        return jogada5_canto_central4(b,i,g,c,a,h,pc,player)
    elif (jogada5_canto_central4(f,g,a,i,c,d,pc,player)) != -1:
        return jogada5_canto_central4(f,g,a,i,c,d,pc,player)
    elif (jogada5_canto_central4(h,a,c,g,i,b,pc,player)) != -1:
        return jogada5_canto_central4(h,a,c,g,i,b,pc,player)

    elif (jogada5_canto_central5(d,b,e,f,h,a,g,pc,player)) != -1:
        return jogada5_canto_central5(d,b,e,f,h,a,g,pc,player)
    elif (jogada5_canto_central5(b,f,e,h,d,c,a,pc,player)) != -1:
        return jogada5_canto_central5(b,f,e,h,d,c,a,pc,player)
    elif (jogada5_canto_central5(f,h,e,d,b,i,c,pc,player)) != -1:
        return jogada5_canto_central5(f,h,e,d,b,i,c,pc,player)
    elif (jogada5_canto_central5(h,d,e,b,f,g,i,pc,player)) != -1:
        return jogada5_canto_central5(h,d,e,b,f,g,i,pc,player)

    elif (jogada5_canto_central6(d,f,c,b,g,i,h,a,pc,player)) != -1:
        return jogada5_canto_central6(d,f,c,b,g,i,h,a,pc,player)
    elif (jogada5_canto_central6(b,h,i,f,a,g,d,c,pc,player)) != -1:
        return jogada5_canto_central6(b,h,i,f,a,g,d,c,pc,player)
    elif (jogada5_canto_central6(f,d,g,h,c,a,b,i,pc,player)) != -1:
        return jogada5_canto_central6(f,d,g,h,c,a,b,i,pc,player)
    elif (jogada5_canto_central6(h,b,a,d,i,c,f,g,pc,player)) != -1:
        return jogada5_canto_central6(h,b,a,d,i,c,f,g,pc,player)

    elif (jogada5_canto_central7(a,b,c,d,e,f,g,h,i,pc,player)) != -1:
        return jogada5_canto_central7(a,b,c,d,e,f,g,h,i,pc,player)
    elif (jogada5_canto_central7(c,f,i,b,e,h,a,d,g,pc,player)) != -1:
        return jogada5_canto_central7(c,f,i,b,e,h,a,d,g,pc,player)
    elif (jogada5_canto_central7(i,h,g,f,e,d,c,b,a,pc,player)) != -1:
        return jogada5_canto_central7(i,h,g,f,e,d,c,b,a,pc,player)
    elif (jogada5_canto_central7(g,d,a,h,e,b,i,f,c,pc,player)) != -1:
        return jogada5_canto_central7(g,d,a,h,e,b,i,f,c,pc,player)

    elif (jogada5_canto_central8(d,c,f,g,e,i,a,pc,player)) != -1:
        return jogada5_canto_central8(d,c,f,g,e,i,a,pc,player)
    elif (jogada5_canto_central8(b,i,h,a,e,g,c,pc,player)) != -1:
        return jogada5_canto_central8(b,i,h,a,e,g,c,pc,player)
    elif (jogada5_canto_central8(f,g,d,c,e,a,i,pc,player)) != -1:
        return jogada5_canto_central8(f,g,d,c,e,a,i,pc,player)
    elif (jogada5_canto_central8(h,a,b,i,e,c,g,pc,player)) != -1:
        return jogada5_canto_central8(h,a,b,i,e,c,g,pc,player)
    
    else:
        return -1

def jogada7(a,b,c,d,e,f,g,h,i,pc,player):

    if (jogada7_canto_central1(a,b,c,d,e,f,g,h,i,pc,player)) != -1:
        return jogada7_canto_central1(a,b,c,d,e,f,g,h,i,pc,player)
    elif (jogada7_canto_central1(c,f,i,b,e,h,a,d,g,pc,player)) != -1:
        return jogada7_canto_central1(c,f,i,b,e,h,a,d,g,pc,player)
    elif (jogada7_canto_central1(i,h,g,f,e,d,c,b,a,pc,player)) != -1:
        return jogada7_canto_central1(i,h,g,f,e,d,c,b,a,pc,player)
    elif (jogada7_canto_central1(g,d,a,h,e,b,i,f,c,pc,player)) != -1:
        return jogada7_canto_central1(g,d,a,h,e,b,i,f,c,pc,player)

    elif (jogada7_canto_central2(a,b,c,d,e,f,g,h,i,pc,player)) != -1:
        return jogada7_canto_central2(a,b,c,d,e,f,g,h,i,pc,player)
    elif (jogada7_canto_central2(c,f,i,b,e,h,a,d,g,pc,player)) != -1:
        return jogada7_canto_central2(c,f,i,b,e,h,a,d,g,pc,player)
    elif (jogada7_canto_central2(i,h,g,f,e,d,c,b,a,pc,player)) != -1:
        return jogada7_canto_central2(i,h,g,f,e,d,c,b,a,pc,player)
    elif (jogada7_canto_central2(g,d,a,h,e,b,i,f,c,pc,player)) != -1:
        return jogada7_canto_central2(g,d,a,h,e,b,i,f,c,pc,player)

    else:
        return -1

def estrategia(a,b,c,d,e,f,g,h,i,pc,player,rodada):
    
    if (rodada==3) and (jogada3(a,b,c,d,e,f,g,h,i,pc,player)) != -1:
        return jogada3(a,b,c,d,e,f,g,h,i,pc,player)
    
    elif (rodada==5) and (jogada5(a,b,c,d,e,f,g,h,i,pc,player)) != -1:
        return jogada5(a,b,c,d,e,f,g,h,i,pc,player)

    elif (rodada==7) and (jogada7(a,b,c,d,e,f,g,h,i,pc,player)) != -1:
        return jogada5(a,b,c,d,e,f,g,h,i,pc,player)

    else:
        return -1

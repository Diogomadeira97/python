def alphas_mono(Ka,H):
    alpha0=(H)/(Ka + H)
    alpha1=(Ka)/(Ka + H)
    return (alpha0,alpha1)

def alphas_di(Ka1,Ka2,H):
    x=(H**2) + (Ka1*H) + (Ka1*Ka2)
    alpha0=(H**2)/x
    alpha1=(H*Ka1)/x
    alpha2=(Ka1*Ka2)/x
    return(alpha0,alpha1,alpha2,x)

def alphas_tri(Ka1,Ka2,Ka3,H):
    x=(H**3) + (Ka1*(H**2)) + (Ka1*Ka2*H) + (Ka1*Ka2*Ka3)
    alpha0=(H**3)/x
    alpha1=(Ka1*(H**2))/x
    alpha2=(Ka1*Ka2*H)/x
    alpha3=(Ka1*Ka2*Ka3)/x
    return (alpha0,alpha1,alpha2,alpha3,x)

def alphas_tetra(Ka1,Ka2,Ka3,Ka4,H):
    x=(H**4) + (Ka1*(H**3)) + (Ka1*Ka2*(H**2)) + (Ka1*Ka2*Ka3*H) + (Ka1*Ka2*Ka3*Ka4)
    alpha0=(H**4)/x
    alpha1=(Ka1*(H**3))/x
    alpha2=(Ka1*Ka2*(H**2))/x
    alpha3=(Ka1*Ka2*Ka3*H)/x
    alpha4=(Ka1*Ka2*Ka3*Ka4)/x
    return (alpha0,alpha1,alpha2,alpha3,alpha4,x)

def alphas_EDTA(Ka1,Ka2,Ka3,Ka4,Ka5,Ka6,H):
    x=(H**6) + (Ka1*(H**5)) + (Ka1*Ka2*(H**4)) + (Ka1*Ka2*Ka3*(H**3)) + (Ka1*Ka2*Ka3*Ka4*(H**2)) + (Ka1*Ka2*Ka3*Ka4*Ka5*H) + (Ka1*Ka2*Ka3*Ka4*Ka5*Ka6)
    alpha0=(H**6)/x
    alpha1=(Ka1*(H**5))/x
    alpha2=(Ka1*Ka2*(H**4))/x
    alpha3=(Ka1*Ka2*Ka3*(H**3))/x
    alpha4=(Ka1*Ka2*Ka3*Ka4*(H**2))/x
    alpha5=(Ka1*Ka2*Ka3*Ka4*Ka5*H)/x
    alpha6=(Ka1*Ka2*Ka3*Ka4*Ka5*Ka6)/x
    return (alpha0,alpha1,alpha2,alpha3,alpha4,alpha5,alpha6,x)

def menu():
    print("(a)Alphas monoprótico")
    print("(b)Alphas dipróticos")
    print("(c)Alphas tripróticos")
    print("(d)Alphas tetrapróticos")
    print("(e)Alphas Hexaprótico")
    print("(f)Alphas EDTA")
    
menu()

escolha=input()

if (escolha=="a"):
    valores=input("\n>Digite o Ka e a concentração (separados por espaço): ").split()
    for i in range(len(valores)):
        valores[i]=float(valores[i])
    alphas=alphas_mono(valores[0],valores[1])
    print("\n>alpha0=","%.4f" %alphas[0],"\n>alpha1=","%.4f" %alphas[1])

if (escolha=="b"):
    valores=input("\n>Digite o Ka1, Ka2 e a concentração (separados por espaço): ").split()
    for i in range(len(valores)):
        valores[i]=float(valores[i])
    alphas=alphas_di(valores[0],valores[1],valores[2])
    print("\n>alpha0=","%.4f" %alphas[0],"\n>alpha1=","%.4f" %alphas[1],"\n>alpha2=","%.4f" %alphas[2],"\n\n>D=",alphas[3])

if (escolha=="c"):
    valores=input("\n>Digite o Ka1, Ka2, Ka3 e a concentração (separados por espaço): ").split()
    for i in range(len(valores)):
        valores[i]=float(valores[i])
    alphas=alphas_tri(valores[0],valores[1],valores[2],valores[3])
    print("\n>alpha0=","%.4f" %alphas[0],"\n>alpha1=","%.4f" %alphas[1],"\n>alpha2=","%.4f" %alphas[2],"\n>alpha3=","%.4f" %alphas[3],"\n\n>D=",alphas[4])

if (escolha=="d"):
    valores=input("\n>Digite o Ka1, Ka2, Ka3, Ka4 e a concentração (separados por espaço): ").split()
    for i in range(len(valores)):
        valores[i]=float(valores[i])
    alphas=alphas_tetra(valores[0],valores[1],valores[2],valores[3],valores[4])
    print("\n>alpha0=","%.4f" %alphas[0],"\n>alpha1=","%.4f" %alphas[1],"\n>alpha2=","%.4f" %alphas[2],"\n>alpha3=","%.4f" %alphas[3],"\n>alpha4=","%.4f" %alphas[4],"\n\n>D=",alphas[5])


if (escolha=="e"):
    valores=input("\n>Digite o Ka1, Ka2, Ka3, Ka4, Ka5, Ka6 e a concentração (separados por espaço): ").split()
    for i in range(len(valores)):
        valores[i]=float(valores[i])
    alphas=alphas_EDTA(valores[0],valores[1],valores[2],valores[3],valores[4],valores[5],valores[6])
    print("\n>alpha0=","%.4f" %alphas[0],"\n>alpha1=","%.4f" %alphas[1],"\n>alpha2=","%.4f" %alphas[2],"\n>alpha3=","%.4f" %alphas[3],"\n>alpha4=",alphas[4],"\n>alpha5=",alphas[5],"\n>alpha6=",alphas[6],"\n\n>D=",alphas[7])


if (escolha=="f"):
    valores=[1,0.031622776,0.01,0.002041737,7.4131024e-7,4.265795e-11,0]
    valores[6]=input("\n>Digite a concentração: ")
    for i in range(len(valores)):
        valores[i]=float(valores[i])
    alphas=alphas_EDTA(valores[0],valores[1],valores[2],valores[3],valores[4],valores[5],valores[6])
    print("\n>alpha0=","%.4f" %alphas[0],"\n>alpha1=","%.4f" %alphas[1],"\n>alpha2=","%.4f" %alphas[2],"\n>alpha3=","%.4f" %alphas[3],"\n>alpha4=",alphas[4],"\n>alpha5=",alphas[5],"\n>alpha6=",alphas[6],"\n\n>D=",alphas[7])








    
    

H="continue"

while H==str("continue"):
    
    X=(int(input("\n>Digite um número inteiro positivo para descobrir seus divisores:")))

    W=0
    
    if (X>=1):

        for f in range(1,X+1):
            
            if (X%f==0):
                
                print("\n>",f,"é divisor de",X)

                W=W+1
                
        if (W==2):
            
            print("\n>o número é primo")
                
    else:
        
        print("\n>número inválido")

    Y=(str(input("\n>Gostaria de realizar novamente a operação?(sim/não)")))

    while Y!=("sim") and Y!=("não"):
    
        Y=(str(input("\n>Não entendi o que foi digitado.\n\n>Poderia Digitar novamente?(sim/não)")))

        
    if Y==("sim"):
    
        print("\n>ok, vamos continuar...")


    if Y==("não"):

        H="pare"

        print("\n>Ok, até mais. :)")

    
    
    

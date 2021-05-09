X=(int(input(">Digite um número inteiro positivo sem zeros à esquerda:")))

C=1
       
while X>1:

    X=X/10

    if X>=1:

        C=C+1

print("\n>O numero informado possuí",C,"dígito(s).")

X=(int(input(">Digite um número de 5 digitos:")))

if (10000<=X<=99999):

    X1=(X//10000)

    X2=((X%10000)//1000)

    X3=(((X%10000)%1000)//100)

    X4=((((X%10000)%1000)%100)//10)

    X5=((((X%10000)%1000)%100)%10)

    Z=((X5*10000)+(X4*1000)+(X3*100)+(X2*10)+(X1))

    if (X==Z):

        W=(str("é um palíndromo"))

    else:

        W=(str("não é um palíndromo"))

    print("\n>O inverso do número é",Z,"e ele",W)


else:

    print("\n>O número digitado não possuí 5 digitos.")
        


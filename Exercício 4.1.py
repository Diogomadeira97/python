P=(float(input(">Digite seu peso em quilograma:")))

A=(float(input("\n>Digite sua altura em metros:")))

IMC=(float(P/(A**2)))

if (IMC<18.5):
    X=(str("Abaixo do peso"))

elif (18.5<=IMC<25):
    X=(str("Saúdavel"))

elif (25<=IMC<30):
    X=(str("Peso em excesso"))

elif (30<=IMC<35):
    X=(str("Obesidade grau I"))

elif (35<=IMC<40):
    X=(str("Obesidade grau II"))

elif (40<=IMC):
    X=(str("obesidade grau III"))

    
print("\n\n>O seu IMC é",'%.2f'%IMC,"e você está classificado como",X)

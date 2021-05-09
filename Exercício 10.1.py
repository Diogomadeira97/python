frase=input(">Digite a frase desejada:" ).split()

b=len(frase)

print("\n>A frase tem",b,"palavras\n")

for i in range (len(frase)):

    print(">palavra",i+1,":",frase[i])

    

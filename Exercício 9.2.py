def analise_media(x):
    
    classificaçoes=["Aluno aprovado","Aluno em verificação suplementar","Aluno reprovado"]
    
    if (x>=6):
        return classificaçoes[0]
    elif (x>=4 and media<=6):
        return classificaçoes[1]
    elif (x<4):
        return classificaçoes[2]

teste="sim"

while (teste=="sim"):
    
    media=float(input("\n>Digite a média a ser analisada: "))

    teste2="sim"

    while (teste2=="sim"):

        if (media>10) or (media<0):
            media=float(input("\n>Média inválida. Digite uma média entre 0 e 10: "))
            teste2="sim"
        else:
            teste2="nao"
            
    analise=print("\n>",analise_media(media))
    
    pergunta=input("\n>Você quer analisar outra média? S ou N: ")

    teste3="sim"

    while (teste3=="sim"):

        if (pergunta=="S") or (pergunta=="s"):
            pergunta="S"
            teste3="nao"
        
        elif (pergunta=="N") or (pergunta=="n"):
            pergunta="N"
            teste3="nao"

        else:
            pergunta=input("\n>Opção inválida! Escolha S ou N: ")
            teste3="sim"

    if (pergunta=="S"):
        teste="sim"
    elif (pergunta=="N"):
        teste="nao"
        
print("\n>Finalizado")
                        

    

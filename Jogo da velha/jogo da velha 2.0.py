import funçoes

jogarnovamente="S"

placar=[0,0,0]

partida=1

while (jogarnovamente=="S"):
    
    rodada=1
    
    J=[1,2,3,4,5,6,7,8,9]
    
    for i in range(len(J)):

        J[i]=str(J[i])

    peça_player=(input("\n>Escolha X ou O para jogar: ")).upper()

    while (peça_player!="O" and peça_player!="X"):    
        peça_player=(input("\n>Opção inválida! Escolha X ou O para jogar: ")).upper()
        
    if (peça_player=="O"):          
        print("\n>Você escolheu O!")
        peça_pc="X"

    elif (peça_player=="X"):
        print("\n>Você escolheu X!")
        peça_pc="O"

            
    jogadainicial=(input("\n>Você quer começar? S ou N: ")).upper()

    while (jogadainicial!="S" and jogadainicial!="N"):
        jogadainicial=(input("\n>Opção inválida! Escolha S ou N: ")).upper()

    if (partida==1):
        print("\n>Para jogar escolha um número de acordo com a casa que deseja jogar.")
        funçoes.tabuleiro(J[0],J[1],J[2],J[3],J[4],J[5],J[6],J[7],J[8])
        
    elif (partida!=1):
        print("\n>Tabuleiro atualizado")
        funçoes.tabuleiro(J[0],J[1],J[2],J[3],J[4],J[5],J[6],J[7],J[8])
        
    analise=-1
    
    while (analise==-1):

        if (jogadainicial=="N"):
            
            if (rodada==1) or (rodada==3) or (rodada==5) or (rodada==7) or (rodada==9):
                print("\n>Minha vez.")
                posiçao=funçoes.jogadas_pc(J[0],J[1],J[2],J[3],J[4],J[5],J[6],J[7],J[8],peça_pc,peça_player,rodada)
                J[posiçao]=peça_pc
                
            elif (rodada==2) or (rodada==4) or (rodada==6) or (rodada==8):
                print("\n>Sua vez.")
                jogada=str(input("\n>Digite a coordenada que deseja jogar: "))
                while jogada not in J:
                    jogada=str(input("\n>Coordenada inválida. Digite a coordenada que deseja jogar: "))
                jogada=int(jogada)-1
                J[jogada]=peça_player
            
        if (jogadainicial=="S"):
            
            if (rodada==1) or (rodada==3) or (rodada==5) or (rodada==7) or (rodada==9):
                print("\n>Sua vez.")
                jogada=str(input("\n>Digite a coordenada que deseja jogar: "))
                while jogada not in J:
                    jogada=str(input("\n>Coordenada inválida. Digite a coordenada que deseja jogar: "))
                jogada=int(jogada)-1
                J[jogada]=peça_player
                
            elif (rodada==2) or (rodada==4) or (rodada==6) or (rodada==8):
                print("\n>Minha vez.")
                posiçao=funçoes.jogadas_pc(J[0],J[1],J[2],J[3],J[4],J[5],J[6],J[7],J[8],peça_pc,peça_player,rodada)
                J[posiçao]=peça_pc
                  
        funçoes.tabuleiro(J[0],J[1],J[2],J[3],J[4],J[5],J[6],J[7],J[8])
        analise=funçoes.analise(J[0],J[1],J[2],J[3],J[4],J[5],J[6],J[7],J[8],rodada,jogadainicial)
        
        if (analise!=-1):
            
            if (analise==0):
                print("\n>eu venci")
                
            elif (analise==1):
                print("\n>Parabéns, você venceu!!")
                
            elif (analise==2):
                print("\n>Deu velha!")
                
            placar[analise]=placar[analise]+1
            print("Placar: PC=",placar[0],"Player=",placar[1],"Empate=",placar[2])
            
        elif (analise==-1):
            rodada=rodada+1

    jogarnovamente=input("\n>Você quer jogar novamente? S ou N: ").upper()
    
    while (jogarnovamente!="S" and jogarnovamente!="N"):
        jogarnovamente=input("\n>Opção inválida! Escolha S ou N: ").upper()
        
    if (jogarnovamente=="S"):
        partida=partida+1
    
print("\n>Ok, até mais!!!")

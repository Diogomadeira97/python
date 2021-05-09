def incluirNovoNome(dic,nome,telefones):
    dic[nome]=telefones
    print("\n>Contato adicionado!")
    return dic

def incluirTelefone(dic,nome,telefones):
    if nome in dic:
        for i in range(len(telefones)):
            if telefones[i] not in dic[nome]:
                dic[nome].append(telefones[i])
        print("\n>Contato atualizado!")
        return dic
    else:
        resposta=input("\n>Contato não existente, deseja adicionar?(S/N): ").upper()
        while (resposta!="S") and (resposta!="N"):
            resposta=input("\n>Resposta inválida, digite S ou N: ").upper()
        if (resposta=="S"):
            return incluirNovoNome(dic,nome,telefones)
        elif (resposta=="N"):
            print("\n>OK!")
            return dic

def excluirNome(dic,nome):
    dic.pop(nome)
    print("\n>Contato excluído!")
    return dic

def excluirTelefone(dic,nome,telefone):
    if (len(dic[nome])==1):
        return excluirNome(dic,nome)
    else:
        dic[nome].remove(telefone)
        print("\n>Número excluído!")
        return dic

def consultarTelefone(dic,nome):
    if nome in dic:
        print("\n >>>>",nome,":")            
        for i in range(len(dic[nome])):    
            print("(",i+1,")",dic[nome][i])

def analisetelefones(telefones):
    lista=["0","1","2","3","4","5","6","7","8","9"]
    teste1=0
    for i in range(len(telefones)):
        teste2=0
        for digito in telefones[i]:
            if digito not in lista:
                teste2=teste2+1
        if (teste2==0):
            telefones[i]=int(telefones[i])
        else:
            teste1=teste1+1
    while (teste1!=0):
        telefones=input("\n>Apenas números são aceitos. Digite os números separados por espaço: ").split()
        teste1=0
        for i in range(len(telefones)):
            teste2=0
            for digito in telefones[i]:
                if digito not in lista:
                    teste2=teste2+1
            if (teste2==0):
                telefones[i]=int(telefones[i])
            else:
                teste1=teste1+1
    return telefones

def menu():
    print("\n*********Menu*********")
    print("(1)Adicionar contato")
    print("(2)Adicionar telefone")
    print("(3)Excluir contato")
    print("(4)Excluir telefone")
    print("(5)Consultar contato")
    print("(6)Sair")
    print("**********************")
    
agenda={}

escolha=-1

teste=["1","2","3","4","5","6"]

while (escolha!="6"):

    menu()

    escolha=input("\n>Digite o número referente à sua opção: ")

    while escolha not in teste:
        escolha=input("\n>Opção inválida. Digite o número referente à sua opção : ")

    if (escolha=="1"):
        contato=input("\n>Digite o nome do cantato que deseja incluir: ")
        if contato in agenda:
            resposta=input("\n>Contato existente, deseja adicionar números?(S/N): ").upper()
            while (resposta!="S") and (resposta!="N"):
                resposta=input("\n>Resposta inválida, digite S ou N: ").upper()
            if (resposta=="S"):
                num=input("\n>Digite os números do cantato que deseja incluir separados por espaço: ").split()
                numeros=analisetelefones(num)
                agenda_atualizada=incluirTelefone(agenda,contato,numeros)
                agenda.update(agenda_atualizada)
            elif (resposta=="N"):
                print("\n>OK!")  
        else:      
            num=input("\n>Digite os números do cantato que deseja incluir separados por espaço: ").split()
            numeros=analisetelefones(num)
            agenda_atualizada=incluirNovoNome(agenda,contato,numeros)
            agenda.update(agenda_atualizada)

    if (escolha=="2"):
        contato=input("\n>Digite o nome do cantato que deseja incluir: ")
        num=input("\n>Digite os números do cantato que deseja incluir separados por espaço: ").split()
        numeros=analisetelefones(num)
        agenda_atualizada=incluirTelefone(agenda,contato,numeros)
        agenda.update(agenda_atualizada)

    if (escolha=="3"):
        contato=input("\n>Digite o nome do cantato que deseja excluir: ")
        if contato in agenda:
            agenda_atualizada=excluirNome(agenda,contato)
            agenda.update(agenda_atualizada)
        else:
            print("\n>Contato não existente")

    if (escolha=="4"):
        contato=input("\n>Digite o nome do cantato que deseja excluir o número: ")
        if contato in agenda:
            consultarTelefone(agenda,contato)
            teste1=[]
            for i in range(len(agenda[contato])):
                teste1.append(str(i+1))
            posiçao=input("\n>Digite a posição referente ao número que deseja excluir: ")
            while posiçao not in teste1:
                posiçao=input("\n>Posição inválida. Digite a posição do número que deseja excluir: ")
            numero=agenda[contato][int(posiçao)-1]
            agenda_atualizada=excluirTelefone(agenda,contato,numero)
            agenda.update(agenda_atualizada)
        else:
            print("\n>Contato não existente")
            
    if (escolha=="5"):
        consulta=input("\n>Digite o nome do cantato que deseja consultar: ")
        if consulta in agenda:
            consultarTelefone(agenda,consulta)
        else:
            resposta=input("\n>Contato não existente, deseja adicionar?(S/N): ").upper()
            while (resposta!="S") and (resposta!="N"):
                resposta=input("\n>Resposta inválida, digite S ou N: ").upper()
            if (resposta=="S"):
                num=input("\n>Digite os números do cantato que deseja incluir separados por espaço: ").split()
                numeros=analisetelefones(num)
                agenda_atualizada=incluirNovoNome(agenda,consulta,numeros)
                agenda.update(agenda_atualizada)

print("\n>Até mais!!")
    


def descobrir_mes(x):

    meses=["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
                    
    return meses[x]

mes=int(input(">Digite um número inteiro correspondente a um mês do ano: "))

teste="sim"

while (teste=="sim"):

    if (mes>0 and mes<=12):
        mes=mes-1
        teste="nao"
    else:
        mes=int(input("\n>Número inválido, digite um número entre 1 e 12: "))
        teste="sim"

resposta=descobrir_mes(mes)

print("\n>O mês correspondente é",resposta)

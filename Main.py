from random import randint #Importa da biblioteca random o randit.

t = ["Pedra", "Papel", "Tesoura"] #Lista de opções.

robo = t[randint(0,2)] #Manda uma opção aleatoria, vinda da lista de opções.

jogador = False #Deixa o player falso, para se fazer o loop.

while jogador == False: #Faz o loop
    jogador = input("Pedra, Papel, ou Tesoura? : ") #Pergunta ao jogador oque ele quer.
    if jogador == robo: #Se a jogada for igual
        print("Empate!") #Fica empate!
    elif jogador == "Papel": #Se o jogador disser Papel
        if robo == "Pedra": #Se o robo disser Pedra
            print("Ganhas-te!", jogador, "ganha a", robo) #O jogador ganha
        else: 
            print("Perdes-te!", jogador, "perde para", robo) #O jogador perde
    elif jogador == "Pedra": #Se o jogador disser Pedra
        if robo == "Tesoura": #Se o robo disser Tesoura
            print("Ganhas-te!", jogador, "ganha a", robo) #O jogador ganha
        else:
            print("Perdes-te!", jogador, "perde para", robo) #O jogador perde
    elif jogador == "Tesoura":  #Se o jogador disser Tesoura
        if robo == "Papel": #Se robo disser Papel
            print("Ganhas-te!", jogador, "ganha a", robo) #O jogador ganha
        else:
            print("Perdes-te!", jogador, "perde para", robo) #O jogador perde
    else:
        print("Isso não é nenhuma das três opções, tenta denovo!") #Se ele não disser nenhuma das 3 opçoes isto aparece.

    jogador = False #O player voltou para true mas, para se refazer o loop, temos de deixar falso outra vez.
    robo = t[randint(0,2)] #Refazer o loop.   

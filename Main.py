from random import randint #Importa da biblioteca random o randit.

t = ["Pedra", "Papel", "Tesoura"] #Lista de opções.

robo = t[randint(0,2)] #Manda uma opção aleatoria, vinda da lista de opções.

jogador = False #Deixa o player falso, para se fazer o loop.

while jogador == False: #Faz o loop
    jogador = input("Pedra, Papel, ou Tesoura? : ") #Pergunta ao jogador oque ele quer.
    if jogador == robo: #Se a jogada for igual
        print("Empate!") #Fica empate!
    elif jogador == "Pedra": #Se o jogador disser pedra
        if robo == "Papel": #Se o robo disser papel
            print("Perdes-te", robo, "embrulha", jogador) #O jogador perde
        else: 
            print("Ganhas-te", jogador, "embrulha", robo) #O jogador ganha
    elif jogador == "Tesoura": #Se o jogador disser tesoura
        if robo == "Pedra": #Se o robo disser pedra
            print("Perdes-te", robo, "destruiu", jogador) #O jogador perde
        else:
            print("Ganhas-te", jogador, "destruiu", robo) #O jogador ganha
    elif jogador == "Papel":  #Se o jogador disser papel
        if robo == "Tesoura": #Se robo disser tesoura
            print("Perdes-te", robo, "cortou", jogador) #O jogador perde
        else:
            print("Ganhas-te", jogador, "cortou", robo) #O jogador ganha
    else:
        print("Isso não é nenhuma das três opções, tenta denovo!") #Se ele não disser nenhuma das 3 opçoes isto aparece.

    jogador = False #O player voltou para true mas, para se refazer o loop, temos de deixar falso outra vez.
    robo = t[randint(0,2)] #Refazer o loop.   
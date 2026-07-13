
nome_do_jogador = input("digite seu nome: ")

nivel_do_jogador =input("digite seu nivel: ")
while not nivel_do_jogador.isdigit(): #lembrar de usar mais while not pra entender melhor como funciona#
    print("VOCE PRECISA ESCOLHER UM NUMERO")
    nivel_do_jogador = input("digite seu nivel: ")
  

raca = int(input(
    "escolha sua raça: \n"
    "1 - humano \n"
    "2 - elfo \n"
    "3 - anão \n"
    "> "
))
while raca > 3 or raca < 1:
    print("VOCE PRECISA ESCOLHER! 1, 2 ou 3")
    raca = int(input("escolha sua raça: \n"
    "1 - humano \n"
    "2 -elfo \n"
    "3 - anão \n"
    "> "))
if raca == 1:
    raca = "humano"
elif raca == 2:
    raca = "elfo"
elif raca == 3:
    raca = "anão"    
#--------------------------------------------------------------------------------------------------------------
pontos_de_atributo = 10 + (2 * int(nivel_do_jogador))

forca = 0
destreza = 0
inteligencia = 0

pergunta = input("gostaria de distribuir seus pontos de atributos? (s/n)")
if pergunta == "n":
    print("seus pontos de atributo serão guardados para distribuição futura")
    
if pergunta == "s":
    while True:
        try:
            print("voce tem ",pontos_de_atributo," pontos de atributo")
            forca = int(input("quanto de força voce deseja investir? "))
            if forca < 0:
                print("voce não pode investir pontos negativos")
            elif forca > pontos_de_atributo:
                print("voce não tem pontos suficientes")

            elif forca <= pontos_de_atributo:
                pontos_de_atributo -= forca
                break
            
        except ValueError:
            print("voce precisa digitar um numero inteiro")  

    while True:
        try:
            print("voce tem ",pontos_de_atributo," pontos de atributo")
            destreza = int(input("quanto de destreza voce deseja investir? "))
            if destreza < 0:
                print("voce não pode investir pontos negativos")
            elif destreza > pontos_de_atributo:
                print("voce não tem pontos suficientes")
               
            elif destreza <= pontos_de_atributo:
                pontos_de_atributo -= destreza
                break
            
        except ValueError:
            print("voce precisa digitar um numero inteiro") 

    while True:
        try:
            print("voce tem ",pontos_de_atributo," pontos de atributo")
            inteligencia = int(input("quanto de inteligencia voce deseja investir? "))
            if inteligencia < 0:
                print("voce não pode investir pontos negativos")
            elif inteligencia > pontos_de_atributo:
                print("voce não tem pontos suficientes")
               
            elif inteligencia <= pontos_de_atributo:
                pontos_de_atributo -= inteligencia
                break
           
        except ValueError:
            print("voce precisa digitar um numero inteiro")  





print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* \n"
      "NOME DO JOGADOR: ",nome_do_jogador, "\n"
      "NÍVEL: ",nivel_do_jogador, "\n"
      "RAÇA: ",raca, "\n"
      "--ATRIBUTOS--\n"
      "FORÇA: ",forca, "\n"
      "DESTREZA: ",destreza, "\n"
      "INTELIGÊNCIA: ",inteligencia, "\n"
      "PONTOS DE ATRIBUTO: ",pontos_de_atributo,"\n"
      "-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*"
)

nivel = 0
nickname = "pegasus"
sair_do_programa = "sair"
Liga_de_ferro = 1000
Liga_de_bronze = 2000
Liga_de_plata = 5000
Liga_de_ouro = 7000
Liga_de_platina = 8000
Liga_de_ascendente = 9000
Liga_Imortal = 10000
Liga_radiante = 10001

while  True:
    xp = int(input("XP do Heroi "))

    if xp >= 0:
       
       nivel += xp

       alcancou_liga_de_ferro = xp <= Liga_de_ferro

       alcancou_liga_de_plata = xp <= Liga_de_plata

       alcancou_liga_de_ouro = xp <= Liga_de_ouro

       alcancou_liga_de_platina = xp <= Liga_de_platina

       alcancou_liga_de_ascendente = xp <= Liga_de_ascendente

       alcancou_liga_imortal = xp <= Liga_Imortal
     
       alcancou_liga_radiante = Liga_radiante <= xp
     

       if alcancou_liga_de_ferro:
          print(f"O Herói de nome {nickname}, esta no nivel {nivel}, na liga de ferro")

       elif alcancou_liga_de_plata:
          print(f"O Herói de nome {nickname}, esta no nivel {nivel}, na liga de plata")

       elif alcancou_liga_de_ouro:
          print(f"O Herói de nome {nickname}, esta no nivel {nivel}, na liga de ouro")

       elif alcancou_liga_de_platina:
          print(f"O Herói de nome {nickname}, esta no nivel {nivel}, na liga de platina")

       elif alcancou_liga_de_ascendente:
          print(f"O Herói de nome {nickname}, esta no nivel {nivel}, na liga ascendente")

       elif alcancou_liga_imortal:
          print(f"O Herói de nome {nickname}, esta no nivel {nivel}, na liga imortal")

       elif alcancou_liga_radiante:
          print(f"O Herói de nome {nickname}, esta no nivel {nivel}, na liga de radiante")


    else:
       print("Erro! Xp não pode ser menor que zero")
       



     

        
  









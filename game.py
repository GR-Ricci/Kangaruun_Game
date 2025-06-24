from sys import exit
import time
from classes import * #locals ja esta vindo
import sys
def Reset():
    leveis.__init__()

    canguru.__init__()
    vidas_rosto.__init__()
    vidas_numeros.__init__()
    dano.__init__()
    bumerangue.__init__(canguru)
    colisao.__init__()

    canguru.bumerangue = bumerangue  # reatribui porque __init__ apagou essa ligação

    item_vida.__init__()

    rato.__init__()
    rato2.__init__()
    rato3.__init__()
    rato4.__init__()
    rato5.__init__()
    rato6.__init__()

    osso.__init__( rato, canguru)
    osso2.__init__( rato2, canguru)
    osso3.__init__( rato3, canguru)
    osso4.__init__( rato4, canguru)
    osso5.__init__( rato5, canguru)
    osso6.__init__( rato6, canguru)

    lagarto.__init__( canguru, bumerangue)
    lagarto2.__init__( canguru, bumerangue)
    lagarto3.__init__( canguru, bumerangue)
    lagarto4.__init__( canguru, bumerangue)
    lagarto5.__init__( canguru, bumerangue)

    dingo.__init__( bumerangue, canguru.bumerangue)
    dingo2.__init__( bumerangue, canguru.bumerangue)
    dingo3.__init__( bumerangue, canguru.bumerangue)
    dingo4.__init__( bumerangue, canguru.bumerangue)
    dingo5.__init__( bumerangue, canguru.bumerangue)
    dingo6.__init__( bumerangue, canguru.bumerangue)

    gameover.__init__()
    gameover_continue.__init__()
    gameover_quit.__init__()
    gameover_bumerangue.__init__()

    elementos.__init__()
    elementos2.__init__()
    elementos3.__init__()
    nuvem.__init__()
    nuvem2.__init__()
    nuvem3.__init__()
    nuvem4.__init__()
    nuvem5.__init__()
    fase.__init__()
    chao.__init__()
    chao2.__init__()
    chao3.__init__()
    tufo.__init__()
    grama.__init__()
    grama2.__init__()
    grama3.__init__()
    noite.__init__()
    lua.__init__()
    dia.__init__(noite, lua)
    montanha.__init__()
    sol.__init__()
    chaodia.__init__()
    chaonoite.__init__()
    montanhas.__init__()
    montanhas2.__init__()

    # Reatribui referências que você fez antes (se precisarem)
    canguru.vidas_numeros = vidas_numeros
    montanhas.montanha = montanha
    montanhas2.montanhas = montanhas
    montanhas2.montanha = montanha
    dia.sol = sol
    lua.sol = sol
    sol.dia = dia
    chaodia.dia = dia
    noite.dia = dia


    # ---------junção classes--------------#


jogo_on = False
pause = False

while True:
    tela.fill((250,250,250))
    relogio.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:


            if not menu.menu_on and not canguru.morreu:
                if event.key == K_RETURN and jogo_on:
                    pause = not pause

            if menu.menu_on:

                if event.key == K_DOWN and cursor.cima:
                    cursor.cima = False
                    cursor.meio = True
                    cursor.baixo = False

                elif event.key == K_DOWN and cursor.meio :
                    cursor.cima = False
                    cursor.meio = False
                    cursor.baixo = True

                elif event.key == K_UP and cursor.baixo:
                    cursor.cima = False
                    cursor.meio = True
                    cursor.baixo = False

                elif event.key == K_UP and cursor.meio:
                    cursor.cima = True
                    cursor.meio = False
                    cursor.baixo = False
                if event.key == K_RETURN and cursor.cima:
                    menu.menu_on = False
                    jogo_on = True
                if event.key == K_RETURN and cursor.baixo:
                    pygame.quit()
                    sys.exit()


            if not canguru.morreu and not canguru.loading_battle and jogo_on :

                if event.key == K_RIGHT:
                    canguru.avanco = True
                if event.key == K_LEFT:
                    canguru.volta_rapido = True
                if event.key == K_UP:  # Quando pressionado para pular
                    canguru.agachado = False
                    canguru.pulo = True  # Ativa o pulo
                if event.key == K_DOWN:  # Quando pressionado para agachar
                    if canguru.pulando and not 485 <= canguru.rect.centery <= 530:
                        canguru.queda = True  # Ativa a queda se estiver pulando

                if event.key == K_1 and canguru.cima == True:
                    bumerangue.ataca= True


            if canguru.gameover and canguru.gameover2:
                if event.key == K_DOWN and gameover_bumerangue.bumerangue_cima:
                    gameover_bumerangue.bumerangue_desce = True
                    gameover_bumerangue.bumerangue_sobe = False
                    gameover_bumerangue.bumerangue_cima = False
                    gameover_bumerangue.bumerangue_baixo = True

                if event.key == K_UP and gameover_bumerangue.bumerangue_baixo:
                    gameover_bumerangue.bumerangue_sobe = True
                    gameover_bumerangue.bumerangue_desce = False
                    gameover_bumerangue.bumerangue_cima = True
                    gameover_bumerangue.bumerangue_baixo = False

                if event.key == K_RETURN:
                    gameover_bumerangue.bumerangue_selecionado = True

        if not canguru.morreu:
            if not canguru.pulando and 485 <= canguru.rect.centery <= 530:
                canguru.agachado = pygame.key.get_pressed()[K_DOWN]


    #pontos.update()
    if menu.menu_on:
        menu.update()
        kangaruun.update()
        cursor.update()
        efeitos_menu.update()
        play.update()
        exit.update()
        settings.update()
    else:
        if not pause:
            game.update()
            game.draw(tela)

            if gameover_continue.iniciar_continue:
                Reset()
            if gameover_quit.iniciar_quit:
                pygame.quit()
                sys.exit()

            colisao.update()
            dano.update()
            gameover.update()
            gameover_continue.update()
            gameover_quit.update()
            gameover_bumerangue.update()
            leveis.update()
            if not leveis.boss_perto and not leveis.boss:
                gerenciador.update()
            if leveis.boss:
                tasmania.update()
                machado.update()
                machado2.update()
                machado3.update()
                machado4.update()

        #item_vida.Colisao()
        #bumerangue.Colisao()
        #dingo.Colisao()
        #dingo2.Colisao()
        #dingo3.Colisao()
        #dingo4.Colisao()
        #dingo5.Colisao()
        #dingo6.Colisao()
        #lagarto.Colisao()
        #osso.Colisao()
        #osso3.Colisao()
        #rato.colisao()
        #rato3.colisao()
        #canguru.Colisao()

        if pause:
            game.draw(tela)

    pygame.display.flip()
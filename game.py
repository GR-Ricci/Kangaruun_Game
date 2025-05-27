from sys import exit
from classes import * #locals ja esta vindo

while True:
    tela.fill((250,250,250))
    relogio.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if not canguru.morreu:
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


        if not canguru.gameover:
            if not canguru.pulando and 485 <= canguru.rect.centery <= 530:
                canguru.agachado = pygame.key.get_pressed()[K_DOWN]

    #pontos.update()

    game.update()
    game.draw(tela)
    gerenciador.update()

    bumerangue.Colisao()
    dingo.Colisao()
    dingo2.Colisao()
    dingo3.Colisao()
    dingo4.Colisao()
    dingo5.Colisao()
    dingo6.Colisao()

    lagarto.Colisao()
    osso.Colisao()
    rato.colisao()
    canguru.Colisao()
    colisao.update()
    dano.update()


    gameover.update()
    gameover_continue.update()
    gameover_quit.update()
    gameover_bumerangue.update()

    pygame.display.flip()
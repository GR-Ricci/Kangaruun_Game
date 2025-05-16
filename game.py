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

            if event.key == K_1:
                bumerangue.ataca= True

        if not canguru.pulando and 485 <= canguru.rect.centery <= 530:
            canguru.agachado = pygame.key.get_pressed()[K_DOWN]

    #pontos.update()
    game.update()
    game.draw(tela)
    pygame.display.flip()

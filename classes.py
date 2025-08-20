from random import randint
from random import choice
import pygame.transform
import math
from recursos import*
from pygame.locals import *
import pygame.freetype

#---------Sistema----------#
#Menu Principal
class Menu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.menu_on = True
        self.image = carroca_menu_image
        self.image = pygame.transform.scale (self.image, (640,480))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0,0)
    def update(self):
        if self.menu_on:
            tela.blit(self.image, self.rect)
class Kangaruun(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = carroca_kangarunn
        self.image = pygame.transform.scale (self.image, (1024/3,1024/3))
        self.rect = self.image.get_rect()
        self.rect.center = (425,40)
    def update(self):
        tela.blit(self.image, self.rect)
class Play(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.menu_play_on = False
        self.image = carroca_menu_play
        self.image = pygame.transform.scale (self.image, (1024/3.5 ,1024/3.5))
        self.rect = self.image.get_rect()
        self.rect.center = (428,90)
    def update(self):
        tela.blit(self.image, self.rect)
class Shop(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.menu_shop_on = False
        self.image = carroca_menu_shop
        self.image = pygame.transform.scale (self.image, (612/4 ,408/4))
        self.image.fill((128, 128, 128), special_flags=pygame.BLEND_RGB_MULT)  # ainda nao programado
        self.rect = self.image.get_rect()
        self.rect.center = (428,180)
    def update(self):
        tela.blit(self.image, self.rect)
class Settings(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = carroca_menu_settings
        self.image = pygame.transform.scale (self.image, (1024/3.5, 1024/3.5))
        self.image.fill((128, 128, 128), special_flags=pygame.BLEND_RGB_MULT) #ainda nao programado
        self.rect = self.image.get_rect()
        self.rect.center = (427,225)
    def update(self):
        tela.blit(self.image, self.rect)
class Exit(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = carroca_menu_exit
        self.image = pygame.transform.scale (self.image, (1024/4,1024/4))
        self.rect = self.image.get_rect()
        self.rect.center = (428,230)
    def update(self):
        tela.blit(self.image, self.rect)

#menu Play
class New_game(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = carroca_menu_new_game
        self.image = pygame.transform.scale (self.image, (612/4.3 ,408/4.3))
        #self.image.fill((128, 128, 128), special_flags=pygame.BLEND_RGB_MULT) #ainda nao programado
        self.rect = self.image.get_rect()
        self.rect.center = (427,120)
    def update(self):
        tela.blit(self.image, self.rect)
class Continue_menu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = carroca_menu_continue
        self.image = pygame.transform.scale (self.image, (612/4,408/4))
        self.image.fill((128, 128, 128), special_flags=pygame.BLEND_RGB_MULT) #ainda nao programado
        self.rect = self.image.get_rect()
        self.rect.center = (425,195)
    def update(self):
        tela.blit(self.image, self.rect)
class Lvl(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = carroca_menu_lvl
        self.image = pygame.transform.scale (self.image, (612/6 ,408/6.5))
        self.image.fill((128, 128, 128), special_flags=pygame.BLEND_RGB_MULT) #ainda nao programado
        self.rect = self.image.get_rect()
        self.rect.center = (427,250)
    def update(self):
        tela.blit(self.image, self.rect)
class Back_play(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = carroca_back
        self.image = pygame.transform.scale (self.image, (1280/15, 853/10))
        self.rect = self.image.get_rect()
        self.rect.center = (427,345)
    def update(self):
        tela.blit(self.image, self.rect)
class Tutorial(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = carroca_menu_tutorial
        self.image = pygame.transform.scale(self.image, (612 / 4.3, 408 / 5.5))
        self.rect = self.image.get_rect()
        self.rect.center = (428, 300)

    def update(self):
        tela.blit(self.image, self.rect)

#menu tutorial
class Tutorial_Menu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.on=False
        self.max_paginas = 3
        self.pagina = 0
        self.x =0
        self.y =0
        self.Sprites()

    def Sprites(self):
        self.images = []
        for i in range (4):
            tutorial_paginas = carroca_tutorial_paginas.subsurface((i * 640, 0), (640, 480))
            self.images.append(tutorial_paginas)

        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def Update(self):
        if self.on:
            self.image = self.images[self.pagina]
            self.rect = self.image.get_rect()
            self.rect.topleft = (self.x, self.y)
            tela.blit(self.image, self.rect)
class Paginas_Tutorial(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.fonte_score = pygame.freetype.Font(carroca_fonte_pixel, 16)


    def Update(self):
        if tutorial_menu.on:
            texto, _ = self.fonte_score.render(f'{tutorial_menu.pagina +1} / {tutorial_menu.max_paginas +1}', (255, 0, 0))
            tela.blit(texto, (570, 10))


#efeitos menu
class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cima = True
        self.meio = False
        self.baixo = False
        self.baixo2 = False
        self.baixo_final = False
        self.direita = False
        self.esquerda = False

        self.image = carroca_cursor_play
        self.image = pygame.transform.scale (self.image, (653/3.2,433/3.2))
        self.rect = self.image.get_rect()
        self.rect.center = (-100,-100)

    def update(self):
        tela.blit(self.image, self.rect)
        if menu.menu_on and not play.menu_play_on:
            if self.cima:
                self.image = carroca_cursor_play
                self.image = pygame.transform.scale (self.image, (653/4.5,433/4.5))
                self.rect = self.image.get_rect()
                self.rect.center = (570,120)
            if self.meio:
                self.image = carroca_cursor_shop
                self.image = pygame.transform.scale (self.image, (500/5,500/5))
                self.rect = self.image.get_rect()
                self.rect.center = (555,185)
            if self.baixo:
                self.image = carroca_cursor_settings
                self.image = pygame.transform.scale(self.image, (653 / 4.6, 433 / 4.6))
                self.rect = self.image.get_rect()
                self.rect.center = (550, 245)
            if self.baixo_final:
                self.image = carroca_cursor_exit
                self.image = pygame.transform.scale(self.image, (653 / 4.5, 433 / 4.5))
                self.rect = self.image.get_rect()
                self.rect.center = (520, 296)

        if play.menu_play_on:
            if self.cima:
                self.image = carroca_cursor_new_game
                self.image = pygame.transform.scale (self.image, (1024/10,1024/10))
                self.rect = self.image.get_rect()
                self.rect.center = (550,115)
            if self.meio:
                self.image = carroca_cursor_continue
                self.image = pygame.transform.scale (self.image, (500/5,500/5))
                self.rect = self.image.get_rect()
                self.rect.center = (555,185)
            if self.baixo:
                self.image = carroca_cursor_lvl
                self.image = pygame.transform.scale(self.image, (1024 / 12, 1024 / 12))
                self.rect = self.image.get_rect()
                self.rect.center = (525, 245)
            if self.baixo2:
                self.image = carroca_cursor_tutorial
                self.image = pygame.transform.scale(self.image, (500 /5, 500 /5))
                self.rect = self.image.get_rect()
                self.rect.center = (553, 298)

            if self.baixo_final:
                self.image = carroca_cursor_back
                self.image = pygame.transform.scale(self.image, (655 /4, 433 /4))
                self.rect = self.image.get_rect()
                self.rect.center = (520, 330)
class Efeito_menu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.contador_efeitos =0
        self.efeitos = []

        for i in range(4):

            imagens_efeitos = carroca_menu_efeitos.subsurface((i*1535,0), (1536,1024))
            self.efeitos.append(imagens_efeitos)
            self.image = self.efeitos[0]
            self.rect = self.image.get_rect()
            self.rect.center = (-100,-100)

    def update(self):
        tela.blit(self.image, self.rect)
        self.image = self.efeitos[int(self.contador_efeitos)]
        self.contador_efeitos += 0.15
        if self.contador_efeitos >= len(self.efeitos):
            self.contador_efeitos = 0
        if menu.menu_on and not play.menu_play_on:
            if cursor.cima:
                self.image = pygame.transform.scale (self.image, (1536/2.4,1024/3.4))
                self.rect = self.image.get_rect()
                self.rect.center = (435,155)

            if cursor.meio:
                self.image = pygame.transform.scale (self.image, (1536/3,1024/2.6))
                self.rect = self.image.get_rect()
                self.rect.center = (433,233)

            if cursor.baixo:
                self.image = pygame.transform.scale(self.image, (1536 / 2.7, 1024 / 3.6))
                self.rect = self.image.get_rect()
                self.rect.center = (434, 284)

            if cursor.baixo_final:
                self.image = pygame.transform.scale(self.image, (1536 / 3.8, 1024 / 4.2))
                self.rect = self.image.get_rect()
                self.rect.center = (433, 328)

        if play.menu_play_on:
            if cursor.cima:
                self.image = pygame.transform.scale(self.image, (1536 / 3.2, 1024 / 2.7))
                self.rect = self.image.get_rect()
                self.rect.center = (430, 173)

            if cursor.meio:
                self.image = pygame.transform.scale(self.image, (1536 / 3, 1024 / 3))
                self.rect = self.image.get_rect()
                self.rect.center = (430, 240)

            if cursor.baixo:
                self.image = pygame.transform.scale(self.image, (1536 / 4.7, 1024 / 4.2))
                self.rect = self.image.get_rect()
                self.rect.center = (428, 283)

            if cursor.baixo2:
                self.image = pygame.transform.scale(self.image, (1536 / 3.5, 1024 / 4.2))
                self.rect = self.image.get_rect()
                self.rect.center = (433, 332)

            if cursor.baixo_final:
                self.image = pygame.transform.scale(self.image, (1536 / 5.5, 1024 / 4.3))
                self.rect = self.image.get_rect()
                self.rect.center = (428, 380)

#menus in game
class Pause(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.pause = False
        self.x = 320
        self.y = 250

        self.image = carroca_pause
        self.image = pygame.transform.scale(self.image, (1024/3.5,1024/3.5))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)


    def update (self):
        if self.pause:
            tela.blit(self.image,self.rect)
class Stage_clear(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 320
        self.y = 170

        self.image = carroca_stage_clear
        self.image = pygame.transform.scale(self.image, (1024/4,1024/4))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)


    def update (self):
        if leveis.fim:
            tela.blit(self.image,self.rect)
class Score(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.x = 325
        self.y = 305

        self.image = carroca_score
        self.image = pygame.transform.scale(self.image, (1024 / 10, 1024 / 10))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
    def update(self):
        if leveis.reset_fim >= 100:
            tela.blit(self.image,self.rect)

#Menu GameOver
class Gameover(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 320
        self.y = 190
        self.image = carroca_gameover
        self.image = pygame.transform.scale(self.image, (1024 /4, 1024/4))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)

    def update(self):
        if canguru.gameover:
            tela.blit(self.image,self.rect)
class Gameover_continue (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.continue_selecionado = False
        self.iniciar_continue = False

        self.x = 320
        self.y = 200
        self.image = pygame.transform.scale(carroca_gameover_continue, (1024 // 4, 1024 // 4))
        self.rect = self.image.get_rect(center=(self.x, self.y))

        # Física do impacto
        self.velocidade = 0
        self.offset_x = 0
        self.oscilando = False

        # Parâmetros físicos
        self.amortecimento = 0.90
        self.elasticidade = 0.5

    def update(self):
        if not canguru.gameover2:
            return

        if self.continue_selecionado and not self.oscilando:
            self.image = pygame.transform.scale(carroca_gameover_continue_quebrado, (1024 // 3.7, 1024 // 3.7))
            self.y = 198
            self.rect = self.image.get_rect(center=(self.x, self.y))
            self.velocidade = 25
            self.oscilando = True

        if self.oscilando:
            forca_retorno = -self.offset_x * self.elasticidade
            self.velocidade += forca_retorno
            self.velocidade *= self.amortecimento
            self.offset_x += self.velocidade

            if abs(self.velocidade) < 0.1 and abs(self.offset_x) < 0.1:
                self.offset_x = 0
                self.velocidade = 0
                self.oscilando = False
                self.continue_selecionado = False
                self.iniciar_continue = True

        self.rect.centerx = self.x + self.offset_x
        self.rect.centery = self.y

        tela.blit(self.image, self.rect)
class Gameover_quit (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # Flag que será definida externamente quando o bumerangue selecionar
        self.quit_selecionado = False
        self.iniciar_quit = False

        self.x = 320
        self.y = 195
        self.image = pygame.transform.scale(carroca_gameover_quit, (1024 // 4, 1024 // 4))
        self.rect = self.image.get_rect(center=(self.x, self.y))

        # Física do impacto
        self.velocidade = 0  # Velocidade de oscilação
        self.offset_x = 0  # Deslocamento atual
        self.oscilando = False  # Está balançando?

        # Parâmetros físicos
        self.amortecimento = 0.90  # Perda de energia (0.9 = forte atrito)
        self.elasticidade = 0.5  # Força que puxa de volta ao centro

    def update(self):
        if not canguru.gameover2:
            return

        if self.quit_selecionado and not self.oscilando:
            self.image = pygame.transform.scale(carroca_gameover_quit_quebrado, (1024 // 3.7, 1024 // 3.7))
            self.y = 190
            self.rect = self.image.get_rect(center=(self.x, self.y))
            # Quando recebe o impacto
            self.velocidade = 25  # força do impacto
            self.oscilando = True

        if self.oscilando:
            # Força restauradora (puxa de volta pro centro)
            forca_retorno = -self.offset_x * self.elasticidade
            self.velocidade += forca_retorno
            self.velocidade *= self.amortecimento
            self.offset_x += self.velocidade

            # Se a oscilação já morreu (quase parado), reseta
            if abs(self.velocidade) < 0.1 and abs(self.offset_x) < 0.1:
                self.offset_x = 0
                self.velocidade = 0
                self.oscilando = False
                self.quit_selecionado = False
                self.iniciar_quit = True


        self.rect.centerx = self.x + self.offset_x
        self.rect.centery = self.y

        tela.blit(self.image, self.rect)
class Gameover_bumerangue (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.contador_bumerangue =0
        self.contador_bumerangue_gameover = 0
        self.bumerangue_selecionado = False
        self.bumerangue_indo = False
        self.bumerangue_voltando = False
        self.bumerangue_desce = False
        self.bumerangue_sobe = False
        self.iniciou_descida = False
        self.bumerangue_cima = True
        self.bumerangue_baixo = False


        self.x = 160
        self.y = 227
        self.bumerangue =[]

        for i in range(7):
            imagem_bumerangue = carroca_bumerangue.subsurface((i * 127, 0), (127, 111))
            imagem_bumerangue = pygame.transform.scale(imagem_bumerangue, (127 / 2.8, 111 / 2.8))
            self.bumerangue.append(imagem_bumerangue)
            self.image = self.bumerangue[int(self.contador_bumerangue)]
            self.rect = self.image.get_rect()
            self.rect.center = (self.x, self.y)

    def update(self):
        if canguru.gameover2:
            self.contador_bumerangue_gameover +=1
            if self.contador_bumerangue_gameover >= 60:

                if self.bumerangue_desce:
                    self.y = 277
                    if not self.iniciou_descida:
                        self.contador_bumerangue = len(self.bumerangue) - 1  # começa no frame 6
                        self.iniciou_descida = True  # evita resetar
                    self.contador_bumerangue -= 0.3

                    if self.contador_bumerangue <= 0:
                        self.contador_bumerangue = 0
                        self.bumerangue_desce = False
                        self.iniciou_descida = False  # reseta flag para futuro uso


                if self.bumerangue_sobe:
                    self.y = 227
                    self.contador_bumerangue += 0.3

                    if self.contador_bumerangue >= len(self.bumerangue):
                        self.contador_bumerangue = 0
                        self.bumerangue_sobe = False
                        self.iniciou_descida = False


                if self.bumerangue_selecionado and self.bumerangue_cima:
                    self.contador_bumerangue += 0.7
                    if self.contador_bumerangue >= len(self.bumerangue):
                        self.contador_bumerangue = 0

                    if not self.bumerangue_voltando:
                        self.x += 5
                        # Ponto de “batida” no CONTINUE — ajuste conforme a posição certa
                        if self.x >= 210:
                            self.bumerangue_voltando = True
                            gameover_continue.continue_selecionado = True
                            self.movimento_x = self.x
                            self.y_fixo = self.y

                    else:
                        self.movimento_x -= 10
                        arco = ((self.movimento_x - 100) ** 2) / 1000 - 20
                        self.x = self.movimento_x
                        self.y = self.y_fixo + arco

                        # Sai da tela à esquerda — você pode só parar de desenhar ou deixar assim
                        if self.x < -100:
                            pass  # não reseta, deixa o gameover sair do código

                if self.bumerangue_selecionado and self.bumerangue_baixo:
                    self.contador_bumerangue -= 0.5
                    if self.contador_bumerangue < 0:
                        self.contador_bumerangue = len(self.bumerangue) - 1

                    if not self.bumerangue_voltando:
                        self.x += 5
                        if self.x >= 250:
                            self.bumerangue_voltando = True
                            gameover_quit.quit_selecionado = True

                            self.movimento_x = self.x
                            self.y_fixo = self.y
                    else:
                        self.movimento_x -= 10
                        arco = ((self.movimento_x - 100) ** 2) / 1000 - 30
                        self.x = self.movimento_x
                        self.y = self.y_fixo + arco
                        if self.x < -100:
                            pass  # sai da tela, não reseta



                self.image = self.bumerangue[int(self.contador_bumerangue)]
                self.rect = self.image.get_rect()
                self.rect.center = (self.x, self.y)
                tela.blit(self.image, self.rect)

#Progressão
class Leveis():
    def __init__(self):
        self.fim = False
        self.fim_velocidade = False
        self.reset_fim = 0
        self.fim_velocidade_contador =0

        self.inimigos_off = False
        self.pontos = 0
        self.contador = 0
        self.fonte = pygame.font.SysFont('calibri', 20, False, False)
        self.fonte_score =  pygame.freetype.Font(carroca_fonte_pixel, 16)
        self.fonte_score.pad = True
        self.boss = False
        self.boss_a = False
        self.boss_b = False
        self.boss_c = False
        self.boss_perto = False
        self.boss_derrotado = False
        self.lvl_0 = False
        self.lvl_1 = False
        self.lvl_2 = False
        self.lvl_3 = False
        self.lvl_4 = False
        self.lvl_5 = False

    def pontuacao(self):
        texto = self.fonte.render(f'PONTOS: {self.pontos}', True, (255, 0, 0))
        if not self.boss:
            self.contador +=0.10
            self.pontos = int(self.contador)
        #tela.blit(texto, (10, 450))

    def lvl(self):
        #distancia boss perto == 20
        if self.pontos >= 1220:
            self.fim = True
            self.fim_velocidade_contador += 1
            if self.fim_velocidade_contador >=100 :
                self.fim_velocidade = True
        elif self.pontos >= 1201:
            self.inimigos_off = True
            self.boss = False
            self.boss_perto = False
        elif 1201> self.pontos >= 1200:
            self.boss_c = True
            self.boss = True
        elif self.pontos >= 1180:
            self.boss_perto = True
        elif self.pontos >= 1000:
            self.lvl_5 = True
            self.lvl_4 = False
        elif self.pontos >= 805:
            self.lvl_4 = True
            self.lvl_3 = False
            self.boss_b = False
            self.boss = False
        elif 805 > self.pontos >= 800:
            self.boss_b = True
            self.boss = True
        elif self.pontos >= 780:
            self.boss_perto = True
        elif self.pontos >= 600:
            self.lvl_3 = True
            self.lvl_2 = False
            self.boss_perto = False
            self.boss = False
        elif self.pontos >= 405:
            self.lvl_2 = True
            self.lvl_1 = False
            self.boss_perto = False
            self.boss = False
        elif 405 > self.pontos >= 400:
            self.boss_a = True
            self.boss = True
        elif self.pontos >= 380:
            self.boss_perto = True
        elif self.pontos >= 10:
            self.lvl_1 = True
            self.lvl_0 = False
        else:
            self.lvl_0 = True

    def update(self):
        if not canguru.morreu and not self.fim:
            self.pontuacao()
            self.lvl()

            progresso.atualizar_valor(self.pontos)

        if self.fim:
            self.reset_fim +=1

        if leveis.reset_fim >= 150:
            contorno_cor = (0, 0, 0)
            texto_cor = (255, 150, 36)
            posicao = (301, 311)
            offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

            for x, y in offsets:
                self.fonte_score.render_to(tela, (posicao[0] + x, posicao[1] + y),
                                           f'{self.pontos}', contorno_cor)

            self.fonte_score.render_to(tela, posicao, f'{self.pontos}', texto_cor)
class Progress(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 68
        self.y = 75
        self.valor = 0
        self.valor_max = 1220  # agora a barra vai até o valor real de pontos

        # imagens base
        self.progresso_vazio = pygame.transform.scale(carroca_progresso, (int(796 / 8), int(240 / 8)))
        self.progresso_full = pygame.transform.scale(carroca_progresso_full, (int(796 / 8), int(240 / 8)))

        self.image = self.progresso_vazio.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def atualizar_valor(self, novo_valor):
        # mantém nos limites
        self.valor = max(0, min(self.valor_max, novo_valor))

    def update(self):
        # copia a barra vazia
        self.image = self.progresso_vazio.copy()

        # calcula a largura proporcional
        largura_total = self.progresso_full.get_width()
        largura_preenchida = int((self.valor / self.valor_max) * largura_total)

        if largura_preenchida > 0:
            rect_preenchido = pygame.Rect(0, 0, largura_preenchida, self.progresso_full.get_height())
            self.image.blit(self.progresso_full.subsurface(rect_preenchido), (0, 0))

        # mantém posição e desenha
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        tela.blit(self.image, self.rect)
class Progress_brand(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 551
        self.y = 573
        self.image = carroca_progresso_marca
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)

    def update(self):
        self.image = carroca_progresso_marca
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image,(1024/50,1024/50))
        self.rect.center = (self.x, self.y)
class Progress_brand2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 583
        self.y = 573
        self.image = carroca_progresso_marca
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)

    def update(self):
        self.image = carroca_progresso_marca
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image,(1024/50,1024/50))
        self.rect.center = (self.x, self.y)

class Fases(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.fases=[]
        self.fases.append(carroca_deserto)
        self.fases_index = 0

        for i in range (len(self.fases)):
            self.image = self.fases[i]
            self.rect = self.image.get_rect()
            self.rect.center = 0,0

    def mostrar(self):
        if leveis.lvl_0:
            self.fase_index = 0
        #elif self.leveis.lvl_1:
            #fase_index = 1
        #elif self.leveis.lvl_2:
            #fase_index = 2
        # e assim por diante

        self.image = pygame.transform.scale(self.fases[self.fase_index], (1536 / 2.1, 1024 / 2.1))
        tela.blit(self.image, (0, 0))

    def update(self):
        self.mostrar()
#Sorteador
class Gerenciador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.tempo = 0
        self.ligar_gerenciador = True

        self.sorteio = randint (1,13)
        self.grupos = {
            1: [lagarto, dingo, rato],
            2: [lagarto, lagarto3, dingo2, rato3],
            3: [rato2, rato3, dingo5, dingo6, dingo3],
            4: [lagarto, lagarto3,dingo, dingo2,  rato5, rato2],
            5: [lagarto2, lagarto3, dingo5, dingo3, dingo],
            6: [lagarto4, lagarto2,dingo,rato],
            7: [dingo, rato, rato5, rato],
            8: [lagarto, lagarto2,dingo, rato, rato4],

            # waves
            9: [dingo, dingo2, dingo4, dingo5, rato2],
            10: [dingo, dingo2, dingo3, dingo4, dingo5, dingo6],
            11: [lagarto, lagarto2, lagarto4, lagarto5,rato3,rato6,dingo4,dingo],
            12: [rato, rato2, rato3, rato4, rato5,rato6],
            13: [rato, rato2, rato3,rato6,dingo3,dingo5,lagarto5]} #colocar lagarto 6
    def sorteador(self):
        grupo_atual = self.grupos[self.sorteio]
        if all(v.spawn_on for v in grupo_atual):
            for i, v in enumerate(grupo_atual):
                v.spawn = True
                v.spawn_on = False
                self.ligar_gerenciador = False
        else:
            self.ligar_gerenciador = True

    def update(self):
        if not leveis.lvl_0:
            if self.ligar_gerenciador:
                self.sorteador()
            else:
                self.tempo +=1
                if self.sorteio not in [9,10,11,13]:
                    if self.tempo == 200:
                        self.tempo = 0
                        self.sorteio = randint (1,13)
                        self.ligar_gerenciador = True
                else:
                    if self.tempo == 300:
                        self.tempo = 0
                        self.sorteio = randint (1,13)
                        self.ligar_gerenciador = True

#------------Personagem-----------#
#Canguru
class Canguru(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.bumerangue = None

        self.canguru = []
        self.canguru_ataca = []
        self.canguru_agachado = []
        self.canguru_atacar = []

        self.contador_colisao = 0
        self.contador_frames_reducao = 0
        self.atual_parado = 0
        self.atual = 0
        self.atual_ataca = 0
        self.atual_morto = 0
        self.atual_correndo = 0
        self.gravidade = 0
        self.bug_bumerangue = 0
        self.loading_battle = False
        self.pulo_volta = False
        self.pulo_avanco = False
        self.bateu_parede = False
        self.parou = False
        self.ferido = False
        self.morreu = False
        self.gameover = False
        self.gameover2 = False
        self.baixo = False
        self.cima = True
        self.bloquear_agachamento = False
        self.pulo = False
        self.pulo_duplo = False
        self.queda = False
        self.queda_ar = False
        self.pulando = False
        self.agachado = False
        self.andando = False
        self.animar = True
        self.atacando = False
        self.avanco = False
        self.avancando = False
        self.voltando = False
        self.volta_rapido = False
        self.Sprites()

    def get_layer(self):
        # Define a camada de desenho com base no Y
        return 6.4 if self.baixo else 5.9

    def Sprites(self):

        self.canguru = []
        self.canguru.append(carroca_canguru.subsurface((0 * 287, 0), (287, 316))),
        self.canguru.append(carroca_canguru.subsurface((3 * 287, 0), (287, 316)))

        self.canguru_parado = []
        self.canguru_parado.append(carroca_canguru_parado.subsurface((0 * 315, 0), (315, 379))),
        self.canguru_parado.append(carroca_canguru_parado.subsurface((1 * 315, 0), (315, 379)))

        self.canguru_morto = []
        self.canguru_morto.append(carroca_canguru_morto.subsurface((0 * 1024, 0), (1024, 1024))),
        self.canguru_morto.append(carroca_canguru_morto.subsurface((1 * 1024, 0), (1024, 1024)))

        self.canguru_morto_sem_bumerangue = []
        self.canguru_morto_sem_bumerangue.append(carroca_canguru_morto_sem_bumerangue.subsurface((0 * 1024, 0), (1024, 1024))),
        self.canguru_morto_sem_bumerangue.append(carroca_canguru_morto_sem_bumerangue.subsurface((1 * 1024, 0), (1024, 1024)))

        self.canguru_ataca = []
        self.canguru_ataca.append(carroca_canguru.subsurface((4 * 287, 0), (287, 316)))
        self.canguru_ataca.append(carroca_canguru.subsurface((1 * 287, 0), (287, 316)))

        self.canguru_agachado = [
            pygame.transform.scale(
                carroca_canguru_deitado1,
                (438 / 4, 315 / 4)  # Tamanho corrigido
            ),
            pygame.transform.scale(
                carroca_canguru_deitado2,
                (438 / 4, 315 / 4))
        ]
        self.queda_imagem = carroca_canguru_deitado1
        self.queda_imagem = pygame.transform.scale(self.queda_imagem, (438 / 4, 315 / 4))

        self.pulo_imagem = carroca_canguru_pulo
        self.pulo_imagem = pygame.transform.scale(self.pulo_imagem, (315 / 4, 379 / 4))

        self.pulo_duplo_imagem = carroca_canguru_pulo_duplo
        self.pulo_duplo_imagem = pygame.transform.scale(self.pulo_duplo_imagem, (315 / 4, 379 / 4))

        self.image = self.canguru[int(self.atual)]
        self.rect = self.image.get_rect()
        self.rect.center = (190, 490)

    def avancar(self):
        self.origem = 190
        self.velocidade = 10
        self.volta = 5
        self.volta_mais = 10

        if leveis.boss:
            self.destino = 680
        else:
            self.destino = 450


        if self.avanco and not self.avancando and not self.voltando:
            self.avancando = True
            self.voltando = False
            self.volta_rapido = False

        if self.volta_rapido:
            self.avanco = False
            self.voltando = False
            self.avancando = False

        if self.avancando:
            if self.rect.centerx < self.destino:
                self.rect.centerx += self.velocidade
            else:
                self.rect.centerx = self.destino
                self.avancando = False
                self.voltando = True

        if self.avancando and self.volta_rapido:
            self.avancando = False
            self.voltando = True
            self.volta_rapido = True

        if self.voltando:

            if self.rect.centerx > self.origem:
                self.rect.centerx -= self.volta
            else:
                self.rect.centerx = self.origem
                self.voltando = False
                self.avanco = False  # Finaliza tudo
                self.volta_rapido = False

        if self.pulando and self.rect.centerx >= self.destino:
            self.bateu_parede = True
        if not self.pulando:
            self.bateu_parede = False


        if self.voltando and self.avanco:
            self.avanco = False
            self.voltando = False
            self.avancando = True
            self.volta_rapido = False

        if self.volta_rapido:
            self.voltando = False
            if self.rect.centerx > self.origem:
                self.rect.centerx -= self.volta_mais
            else:
                if not self.pulando:
                    self.rect.centerx = self.origem
                    self.avanco = False
                    self.volta_rapido = False

    def atacar(self):
        if self.bumerangue.ataca:
            self.bug_bumerangue +=1
            self.atacando = True
            self.animar = False
        else:
            self.bug_bumerangue =0
            self.atacando = False

        if self.bug_bumerangue >= 100:
            self.bumerangue.ataca = False
            self.atacando = False
            self.animar = True
            bumerangue.ataca = False
            bumerangue.reload = True
            bumerangue.movimento_x = 0
            bumerangue.movimento_y = 0
            bumerangue.y_fixo = 0
            bumerangue.indo = True
            bumerangue.voltando = False
            bumerangue.contador_bumerangue = 0

            bumerangue.rect.center = (-100, -100)

    def pular(self):
        if not self.loading_battle:
            if self.pulo and not self.pulando:
                self.agachado = False
                self.animar = False
                self.atacando = False
                self.pulando = True
                self.pulo = False
                self.pulo_duplo = True
                self.gravidade = -27
                self.image = self.pulo_imagem
                self.image = pygame.transform.scale(self.image, (315 / 4, 379 / 4))

            if pygame.key.get_pressed()[K_DOWN]and pygame.key.get_pressed()[K_UP] and not self.pulando:
                self.pulo = True
                self.agachado = False
                self.animar = False
                self.atacando = False
                self.pulando = True
                self.pulo = False
                self.pulo_duplo = True
                self.gravidade = -27
                self.image = self.pulo_imagem

            if self.pulo_duplo and self.pulo and self.pulando and self.queda:
                self.pulo = False
                self.pulo_duplo = False
                self.queda = False
                self.gravidade = -25
                self.image = self.pulo_duplo_imagem
                self.image = pygame.transform.scale(self.image, (315 / 4, 379 / 4))

            if self.pulo_duplo and self.pulo and self.pulando :
                self.pulo = False
                self.pulo_duplo = False
                self.gravidade = -25
                self.image = self.pulo_duplo_imagem
                self.image = pygame.transform.scale(self.image, (315 / 4, 379 / 4))

            if self.pulando and self.queda:
                self.gravidade += 2
                self.image = self.queda_imagem
                self.image = pygame.transform.scale(self.image, (438 / 4, 315 / 4))

            if not self.pulando and self.queda:
                self.pulando = False
                if not self.atacando:
                    self.animar = True
                if not self.animar:
                    self.atacando = True

            if not self.pulando and self.agachado:
                self.animar = False
                self.atacando = False
                self.image = self.queda_imagem

            if self.pulando:
                self.rect.centery += self.gravidade
                self.gravidade += 2


                if self.rect.centery >= 485:  # chão
                    self.rect.centery = 485
                    self.gravidade = 0
                    self.pulando = False
                    self.pulo_avanco = False
                    self.pulo_volta = False
                    self.queda_ar = False
                    self.queda = False
                    if not self.atacando:
                        self.animar = True
                    if not self.animar:
                        self.atacando = True

                    teclas = pygame.key.get_pressed()
                    if teclas[pygame.K_DOWN] and not teclas[pygame.K_UP]:
                        canguru.agachado = True

                if self.rect.centery >= 560:
                    self.pulando = False
                    self.pulo_avanco = False
                    self.pulo_volta = False
                    self.queda = False
                    self.queda_ar = False
                    teclas = pygame.key.get_pressed()
                    if teclas[pygame.K_DOWN] and not teclas[pygame.K_UP]:
                        self.agachado = True

                    if not self.atacando:
                        self.animar = True
                    if not self.animar:
                        self.atacando = True

            if pygame.key.get_pressed()[K_UP] and self.agachado:
                self.agachado = False
                self.animar = False
                self.atacando = False
                self.atacando = False
                self.pulo = True
                self.pulando = True
                self.gravidade = -25
                self.image = self.pulo_imagem
                self.rect = self.image.get_rect(center=self.rect.center)

            if pygame.key.get_pressed()[K_UP] and self.animar:
                self.agachado = False
                self.animar = False
                self.atacando = False
                self.pulando = True
                self.pulo = False
                self.pulo_duplo = True
                self.gravidade = -27
                self.image = self.pulo_imagem
                self.image = pygame.transform.scale(self.image, (315 / 4, 379 / 4))
            # impede o bug de baixo e cima rapido

            if not self.agachado and not self.pulando:
                self.pulo = False
                self.pulando = False
                self.agachado = False
                if not self.atacando:
                    self.animar = True
                if not self.animar:
                    self.atacando = True

    def Colisao(self):
        if not self.agachado and not self.queda and not self.queda_ar:
            canguru_hitbox_cabeca = pygame.Rect(canguru.rect.x + 25, canguru.rect.y + 10, 50, 35)
            canguru_hitbox_corpo = pygame.Rect(canguru.rect.x + 25, canguru.rect.y + 55, 40, 40)
            #pygame.draw.rect(tela, (0, 250, 250), canguru_hitbox_cabeca, 2)
            #pygame.draw.rect(tela, (0, 250, 250), canguru_hitbox_corpo, 2)
            return [canguru_hitbox_cabeca,canguru_hitbox_corpo]

        elif self.agachado or self.queda or self.queda_ar:
            canguru_hitbox_cabeca_deitado = pygame.Rect(canguru.rect.x + 40, canguru.rect.y + 10, 50, 70)
            #pygame.draw.rect(tela, (100,0 , 250), canguru_hitbox_cabeca_deitado, 2)
            canguru_hitbox_perna_deitado = pygame.Rect(canguru.rect.x + 10, canguru.rect.y + 30, 50, 40)
            #pygame.draw.rect(tela, (100, 0, 250), canguru_hitbox_perna_deitado, 2)
            return [canguru_hitbox_cabeca_deitado,canguru_hitbox_perna_deitado]

    def update(self):

        if leveis.fim:
            self.rect.x += 5

        if not self.pulando and pygame.key.get_pressed()[K_DOWN] and not pygame.key.get_pressed()[K_UP]:
            self.agachado = True
            self.parou = False  # Força sair do estado parado
            self.rect.centery = 530

        if self.pulando and self.voltando and self.avanco:
            self.pulo_avanco = True
        if self.pulando and self.avanco and self.volta_rapido:
            self.pulo_volta = True

        if self.morreu and not self.pulando:
            if self.morreu and not self.atacando:
                self.atual_morto +=0.02
                if self.atual_morto >= len(self.canguru_morto):
                    self.atual_morto = 1
                self.image = self.canguru_morto [int(self.atual_morto)]
                self.image = pygame.transform.scale(self.image, (1024/10, 1024/10))
                self.rect.centery = 485

            elif self.morreu and self.atacando:
                self.atual_morto += 0.02
                if self.atual_morto >= len(self.canguru_morto):
                    self.atual_morto = 1
                self.image = self.canguru_morto_sem_bumerangue[int(self.atual_morto)]
                self.image = pygame.transform.scale(self.image, (1024 / 10, 1024 / 10))
                self.rect.centery = 485

        else:
            self.avancar()
            self.atacar()
            if leveis.inimigos_off and self.pulando:
                self.pular()
            if not leveis.inimigos_off:
                self.pular()
            if leveis.inimigos_off and not self.pulando:
                self.andando = True
                self.agachado = False

            self.cima = True
            self.baixo = False

            if self.pulando and pygame.key.get_pressed()[K_DOWN]:
                self.baixo = True
                self.cima = False

            if self.pulando and self.avanco:
                self.image = self.queda_imagem
            if self.avancando and self.pulando:
                self.image = self.queda_imagem

            elif self.pulando and not self.queda:
                if self.pulo_avanco:
                    self.image = self.queda_imagem
                    self.image = pygame.transform.scale(self.image, (438 / 4, 315 / 4))
                if self.bateu_parede:
                    self.image = self.queda_imagem
                    self.image = pygame.transform.scale(self.image, (438 / 4, 315 / 4))
                if self.pulo_volta:
                    self.image = self.queda_imagem
                    self.image = pygame.transform.scale(self.image, (438 / 4, 315 / 4))

                if not self.pulo_avanco and not self.pulo_volta and not self.bateu_parede and self.image != self.queda_imagem :
                    self.image = pygame.transform.scale(self.image, (315 / 4, 379 / 4))

                else:
                    self.image = pygame.transform.scale(self.image, (438 / 4, 315 / 4))

            elif self.pulando and self.queda:
                if self.queda:
                    self.image = pygame.transform.scale(self.image, (438 / 4, 315 / 4))

            elif self.avanco and self.pulo:
                self.image = pygame.transform.scale(self.image, (438 / 4, 315 / 4))

            elif self.agachado and not self.loading_battle:
                self.atual_correndo += 0.15
                if self.atual_correndo >= len(self.canguru_agachado):
                    self.atual_correndo = 0
                self.image = self.canguru_agachado[int(self.atual_correndo)]
                self.image = pygame.transform.scale(self.image, (438 / 4, 315 / 4))
                self.rect.centery = 530
                self.baixo = True
                self.cima = False
                if leveis.boss:
                    self.parou = True
                    if not self.avanco and not self.voltando:
                        self.atual_correndo =1
                    else:
                        self.atual_correndo += 0.15
                else:
                    self.parou = False

            elif self.atacando:
                self.atual_ataca += 0.10
                if self.atual_ataca >= len(self.canguru_ataca):
                    self.atual_ataca = 0
                self.image = self.canguru_ataca[int(self.atual_ataca)]
                self.image = pygame.transform.scale(self.image, (315 / 4, 379 / 4))
                self.rect.centery = 485

            elif leveis.boss and not self.parou:
                self.loading_battle = True
                self.incremento = max(0.01, 0.10 * (0.97 ** self.contador_frames_reducao))
                self.atual += self.incremento

                self.contador_frames_reducao += 1

                if self.incremento <= 0.01:
                    self.parou = True
                    self.loading_battle = False

                if self.atual >= len(self.canguru):
                    self.atual = 0

                self.image = self.canguru[int(self.atual)]
                self.image = pygame.transform.scale(self.image, (315 // 4, 379 // 4))
                self.rect.centery = 485

            elif self.parou and not self.avanco and not self.voltando and not self.volta_rapido:

                self.atual_parado +=0.10
                if self.atual_parado >= len(self.canguru_parado):
                    self.atual_parado = 0
                self.image = self.canguru_parado[int(self.atual_parado)]
                self.image = pygame.transform.scale(self.image, (315 / 3.6, 379 / 3.4))
                self.rect.centery = 477

            else:
                self.parou = False
                self.atual += 0.10
                if self.atual >= len(self.canguru):
                    self.atual = 0
                self.image = self.canguru[int(self.atual)]
                self.image = pygame.transform.scale(self.image, (315 / 4, 379 / 4))
                self.rect.centery = 485


            if self.contador_colisao >= 1:
                self.contador_colisao += 1
                #efeito dano
                if self.contador_colisao % 10 < 5:
                    self.image.set_alpha(100)
                else:
                    self.image.set_alpha(180)
                #Tempo de dano
                if self.contador_colisao >= 150:
                    self.image.set_alpha(255)
                    self.contador_colisao = 0

        if self.contador_colisao == 0:
            self.image.set_alpha(255)

        grupos = self.groups()
        if grupos:
            grupo = grupos[0]
            grupo.change_layer(self, self.get_layer())

            self.Colisao()

class Vidas_numeros(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.dano = False
        self.contador_gameover = 0
        self.contador_gameover2 =0
        self.morreu = False
        self.contador_dano = 0
        self.coracao = 0
        self.vidas = 3
        self.x = 105
        self.y = 37
        self.Sprites()

    def Sprites(self):
        self.numeros = []
        for i in range(4):
            numero = carroca_numero_vida.subsurface((i * 200, 0), (200, 200))
            numero = pygame.transform.scale(numero, (200 / 3, 200 / 3))
            self.numeros.append(numero)
        self.image = self.numeros[self.vidas]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self):
        if self.dano and self.vidas > 0:
            self.vidas -= 1
            self.dano = False

        if item_vida.ganha_vida and self.vidas < 3 and self.vidas > 0:
            self.vidas +=1
            item_vida.ganha_vida = False


        elif self.vidas == 0:
            canguru.morreu = True
            self.contador_gameover += 1
            if self.contador_gameover >= 120:
                canguru.gameover = True
                self.contador_gameover2 += 1
                if self.contador_gameover2 >= 60:
                    canguru.gameover2 = True

        if self.coracao:
            self.vidas += 1
        if self.vidas < 3:
            canguru.ferido = True
        else:
            canguru.ferido = False

        self.image = self.numeros[self.vidas]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
class Vidas_rosto(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.dano = False
        self.coracao = 0
        self.contador_dano = 0
        self.vidas = 0
        self.x = 50
        self.y = 36
        self.Sprites()

    def Sprites(self):
        self.rostos = []
        for i in range (4):
            rosto = carroca_rosto_vida.subsurface((i*500,0), (500,500))
            rosto = pygame.transform.scale(rosto,(500/7,500/7))
            self.rostos.append(rosto)
        self.image = self.rostos[self.vidas]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)

    def update(self):
        if self.dano and self.vidas < 3:
            self.vidas += 1
            self.dano = False

        if item_vida.ganha_vida and self.vidas < 3 and self.vidas > 0:
            self.vidas -=1

        self.image = self.rostos[self.vidas]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
class Dano_canguru_Sprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = None
        self.rect = None
        self.contador_dano = 0
        self.danos = []

    def Sprites(self):
        self.danos = []
        for i in range(6):
            dano = carroca_dano_canguru.subsurface((i * 400, 0), (400, 400))
            dano = pygame.transform.scale(dano,(400/2,400/2))
            self.danos.append(dano)
        self.image = self.danos[0]
        self.rect = self.image.get_rect()
        self.rect.center = (canguru.rect.x + 50, canguru.rect.y)

    def animacao(self):
        if self.image:
            self.image = self.danos[int(self.contador_dano)]
            self.contador_dano += 0.15
            if self.contador_dano >= len(self.danos):
                self.contador_dano = 0

    def update(self):
        if canguru.contador_colisao > 0 and self.image is None:
            self.Sprites()

        # Sempre acompanha a posição do canguru
        if self.rect:
            self.rect.center = (canguru.rect.x + 50, canguru.rect.y+50)

        if self.image and not canguru.morreu:
            self.animacao()

            if canguru.contador_colisao >= 1:
                canguru.contador_colisao += 1

                # efeito piscando
                if canguru.contador_colisao % 10 < 5:
                    self.image.set_alpha(100)
                else:
                    self.image.set_alpha(250)

                tela.blit(self.image, self.rect)

                if canguru.contador_colisao == 0:
                    self.image.set_alpha(255)
                    self.image = None
                    self.rect = None

#--itens
class Mochila(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 630
        self.y = 725
        self.image = carroca_mochila
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)

    def update(self):
        self.image = carroca_mochila
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image,(1024/6,1536/6))
        self.rect.center = (self.x, self.y)
class Item_vida(pygame.sprite.Sprite):
    #bloquear para criar um item depois no boss e para drop rapido
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sorteio = choice([1,2])
        self.y = -100
        self.x = -100
        self.ganha_vida = False
        self.ganha = 0
        self.spawn = True
        self.reset = False
        self.contador_vida = 0
        self.liberar = 0
        self.sorteio = 0
        self.movimento = []
        self.velocidade = 3
        self.movimento.append([self.x, self.y])

    def Sprites(self):
        self.vida = []
        for i in range (3):
            vida = carroca_vida.subsurface((i*586,0),(586,426))
            vida = pygame.transform.scale(vida,(588/8,426/8))
            self.vida.append(vida)

        self.image = self.vida[0]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)

    def Animacao(self):

        self.image = self.vida[int(self.contador_vida)]

        if self.spawn == False:
           self.contador_vida = 2
           self.velocidade = 0
        else:
            self.contador_vida += 0.05
            self.velocidade = 1
            if self.contador_vida >= len(self.vida)-1:
                self.contador_vida = 0

        for i in self.movimento:

            i[0] -= self.velocidade
            if i[0] <= -10 and not canguru.morreu:
                self.spawn = False
                self.liberar = 0
                # REMOVE A POSIÇÃO ANTIGA E CRIA UMA NOVA
            if self.spawn == False:
                self.movimento.remove(i)
            if canguru.morreu:
                self.movimento.remove(i)


    def Colisao(self):
        self.vida_hitbox = pygame.Rect(self.rect.x + 10, self.rect.y + 3, 55, 50)
        pygame.draw.rect(tela, (0, 0, 250), self.vida_hitbox, 2)
        canguru_hitbox = canguru.Colisao()

        if canguru.ferido:

            if self.sorteio == 1:
                for hitbox in canguru_hitbox:
                    if self.vida_hitbox.colliderect(hitbox) and not canguru.baixo:
                        self.ganha_vida = True

                        self.liberar = 0
                        self.spawn = False
                        self.reset = True

            if self.sorteio == 2:
                for hitbox in canguru_hitbox:
                    if self.vida_hitbox.colliderect(hitbox) and canguru.baixo:
                        self.ganha_vida = True

                        self.liberar = 0
                        self.spawn = False
                        self.reset = True
                        #print('vida')

        if self.spawn == False:
            self.liberar +=1
            if self.liberar >= 500:
                self.sorteio = choice([1, 2])
                if self.sorteio == 1:
                    self.y = randint(0, 370)  # 410
                elif self.sorteio == 2:
                    self.y = randint(390, 410)  # 410
                self.x = 900
                self.movimento.append([self.x, self.y])
                self.spawn = True

    def update(self):
        self.Sprites()
        if not canguru.morreu and not leveis.boss:
            self.Animacao()
            for i in self.movimento:
                self.image = pygame.transform.scale(self.image, (586/8,426/8))
                self.rect = self.image.get_rect()
                self.rect.topright = i[0], i[1]
                tela.blit(self.image, self.rect)

            self.Colisao()

#--ataques
class Bumerangue(pygame.sprite.Sprite):
    def __init__(self,canguru):
        pygame.sprite.Sprite.__init__(self)
        self.canguru = canguru
        self.contador_bumerangue = 0
        self.bumerangue = []
        self.ataca = False
        self.movimento_x = 0
        self.movimento_y = 0
        self.y_fixo = 0
        self.acertou = False
        self.baixo = False
        self.cima = True
        self.indo = True
        self.voltando = False
        self.reload = False

        for i in range(7):
            imagem_bumerange = carroca_bumerangue.subsurface((i * 127, 0), (127, 111))
            self.bumerangue.append(imagem_bumerange)
            self.image = self.bumerangue[int(self.contador_bumerangue)]
            self.rect = self.image.get_rect()
            self.rect.center = (-100, -100)

    def reset_bumerangue(self):
        self.movimento_x = 0
        self.movimento_y = 0
        self.y_fixo = 0
        self.indo = True
        self.voltando = False
        self.contador_bumerangue = 0
        self.ataca = False
        self.rect.center = (-100, -100)

    def bumerangue_on(self):
        if self.contador_bumerangue > 6:
            self.contador_bumerangue = 0
        self.contador_bumerangue += 0.20

        self.image = self.bumerangue[int(self.contador_bumerangue)]
        self.image = pygame.transform.scale(self.image, (127 / 2.8, 111 / 2.8))

        # Na ida, usa apenas a posição X inicial (não acompanha o canguru)
        if self.indo:
            if self.movimento_x == 0:  # Primeiro frame do lançamento
                self.x_inicial = self.canguru.rect.x + 120  # Guarda a posição X inicial
                self.y_fixo = self.canguru.rect.y + 100  # Guarda a posição Y inicial

            self.movimento_x += 15
            arco = ((self.movimento_x - 100) ** 2) / 1000 - 60
            self.rect.center = (self.x_inicial + self.movimento_x, self.y_fixo + arco)

            if self.rect.x >= 500:  # Distância fixa da tela
                self.indo = False
                self.voltando = True

        # Na volta, ajusta gradualmente para a posição atual do canguru
        elif self.voltando:
            self.movimento_x -= 25

            # Calcula posição alvo baseada na posição ATUAL do canguru
            alvo_x = self.canguru.rect.x + 70
            alvo_y = self.canguru.rect.y + 100
            # Calcula distância atual até o canguru
            distancia_x = abs(self.rect.centerx - (self.canguru.rect.x + 70))
            distancia_total = 500 - (self.canguru.rect.x + 70)
            percentual = distancia_x / distancia_total if distancia_total > 0 else 0

            # Ajuste normal durante a maior parte do trajeto
            alvo_y = self.canguru.rect.y + 100
            ajuste = 5  # velocidade base de ajuste

            # Se estiver muito próximo (últimos 30% do trajeto)
            if not canguru.morreu:
                if percentual < 0.3 :
                    # Ajuste mais agressivo
                    ajuste = 50
                    # Força o y_fixo a ir diretamente para o alvo
                    if self.y_fixo < alvo_y:
                        self.y_fixo = min(alvo_y, self.y_fixo + ajuste)
                    elif self.y_fixo > alvo_y:
                        self.y_fixo = max(alvo_y, self.y_fixo - ajuste)
                if percentual < 0.2:
                    ajuste = 100
                    # Força o y_fixo a ir diretamente para o alvo
                    if self.y_fixo < alvo_y:
                        self.y_fixo = min(alvo_y, self.y_fixo + ajuste)
                    elif self.y_fixo > alvo_y:
                        self.y_fixo = max(alvo_y, self.y_fixo - ajuste)
                if percentual < 0.1:
                    ajuste = 200
                    # Força o y_fixo a ir diretamente para o alvo
                    if self.y_fixo < alvo_y:
                        self.y_fixo = min(alvo_y, self.y_fixo + ajuste)
                    elif self.y_fixo > alvo_y:
                        self.y_fixo = max(alvo_y, self.y_fixo - ajuste)
            else:
                # Ajuste suave normal
                if self.y_fixo < alvo_y:
                    self.y_fixo += min(ajuste, alvo_y - self.y_fixo)
                elif self.y_fixo > alvo_y:
                    self.y_fixo -= min(ajuste, self.y_fixo - alvo_y)
            # Suaviza o movimento Y


            # Mantém a trajetória de arco mesmo na volta
            arco = ((self.movimento_x - 100) ** 2) / 1000 - 60
            self.rect.center = (self.x_inicial + self.movimento_x, self.y_fixo + arco)

            # Verifica colisão com o canguru
            if abs(self.rect.centerx - alvo_x) < 30 and abs(self.rect.centery - alvo_y) < 30:
                self.reset_bumerangue()

    def Colisao(self):
        if self.ataca:
            bumerangue_hitbox = pygame.Rect(self.rect.x + 10, self.rect.y + 5, 30, 40) # Ajuste da hitbox do bumerangue
            canguru_hitbox = pygame.Rect(self.canguru.rect.x + 0, self.canguru.rect.y - 20, 100, 150)

            #pygame.draw.rect(tela, (0, 0, 0), bumerangue_hitbox, 2)
            #pygame.draw.rect(tela, (250, 250, 250), canguru_hitbox, 2)

            if self.voltando and not canguru.morreu:
                if bumerangue_hitbox.colliderect(canguru_hitbox):
                    #print('pegou bumerangue')
                    self.ataca = False
                    self.acertou = False
            return [bumerangue_hitbox]
        return []

    def update(self):

        self.Colisao()
        if self.ataca:
            self.bumerangue_on()

        else:
            self.reset_bumerangue()
class Colisao(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.contador_impacto = 0
        self.contador_impacto_escudo = 0
        self.image = None
        self.rect = None
        self.escudo = False

    def Sprites(self):
        self.impacto = []
        self.impacto_boss = []
        self.impacto_escudo_boss = []
        self.x = bumerangue.rect.x
        self.y = bumerangue.rect.y

        for i in [0, 1]:
            colisao = carroca_impacto.subsurface((i * 400, 0), (400, 400))
            colisao = pygame.transform.scale(colisao, (400/4, 400/4))
            self.impacto.append(colisao)

        for i in range (4):
            colisao_boss = carroca_animacao_dano_boss.subsurface((i* 400,0),(400,400))
            colisao_boss = pygame.transform.scale(colisao_boss,(400/3.5,400/3.5))
            self.impacto_boss.append(colisao_boss)

        for i in range(3):
            escudo_boss = carroca_animacao_escudo_boss.subsurface((i*400,0),(400,400))
            escudo_boss = pygame.transform.scale(escudo_boss,(400/4,400/4))
            self.impacto_escudo_boss.append(escudo_boss)


        if not leveis.boss:
            self.x = bumerangue.rect.x
            self.y = bumerangue.rect.y
            self.image = self.impacto[0]
            self.rect = self.image.get_rect()
            self.rect.center = (self.x, self.y)

        if leveis.boss and tasmania.vulneravel:
            self.x = 530
            self.y = 370
            self.image = self.impacto_boss[0]
            self.rect = self.image.get_rect()
            self.rect.center = (self.x, self.y)

        if leveis.boss and not tasmania.vulneravel:

            self.image = self.impacto_escudo_boss[0]
            self.rect = self.image.get_rect()
            self.rect.center = (tasmania.rect.x, tasmania.rect.y)

        bumerangue.acertou = False

    def animacao(self):
        if not leveis.boss:
            if self.image:
                self.image = self.impacto[int(self.contador_impacto)]
                self.contador_impacto += 0.15
                if self.contador_impacto >= len(self.impacto):
                    self.contador_impacto = 0
                    bumerangue.acertou = False
                    self.image = None
                    self.rect = None

        if leveis.boss and tasmania.vulneravel:
            if self.image:
                self.image = self.impacto_boss[int(self.contador_impacto)]
                self.contador_impacto += 0.25
                if self.contador_impacto >= len(self.impacto_boss):
                    self.contador_impacto = 0
                    bumerangue.acertou = False
                    self.image = None
                    self.rect = None

        if leveis.boss and not tasmania.vulneravel:
            if self.image:
                self.escudo = True
                self.image = self.impacto_escudo_boss[int(self.contador_impacto_escudo)]
                self.contador_impacto_escudo += 0.20
                if self.contador_impacto_escudo >= len(self.impacto_escudo_boss):
                    self.contador_impacto_escudo = 0
                    bumerangue.acertou = False
                    self.image = None
                    self.rect = None

    def update(self):
        if bumerangue.acertou:
            self.Sprites()
        self.animacao()
        if self.escudo and self.image != None:
            self.rect = self.image.get_rect()
            self.rect.center = (tasmania.rect.x +210, tasmania.rect.y+50)
            if tasmania.base2:
                self.rect.center = (tasmania.rect.x + 290, tasmania.rect.y + 50)
        if self.image:
            tela.blit(self.image, self.rect)

# -------------Boss-------------#
class Miniboss(pygame.sprite.Sprite): #rect do bumerangue

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.reset_on = False
        self.contador_colisao = 0
        self.contador = 10
        self.sorteio_ataque = choice([1,2,3])
        self.tempo_ataque = choice([120,240])
        self.boss_saiu = False
        self.boss_venceu = False
        self.controle_dano = 0
        self.tomou_dano = False

        self.vida = 9

        self.dano = False

        self.indo = True
        self.voltando = False

        self.x = 700
        self.y = 375
        self.contador_teste =0
        self.contador = 0
        self.contador_batalha = 0
        self.descanso = 0

    #controles de ataque
        self.total = 0
        self.flag_total = False
        self.contador_vulneravel = 0
        self.vulneravel_pronto = False

        self.repeticao1 = 0
        self.repeticao2 = 0
        self.repeticao3 = 0
        self.repeticao4 = 0
        self.repeticao5 = 0

        self.flag_repeticao1 = False
        self.flag_repeticao2 = False
        self.flag_repeticao3 = False
        self.flag_repeticao4 = False
        self.flag_repeticao5 = False

        self.ladoa = True
        self.ladob = False

        self.base = True
        self.base2 = False
        self.ataque = False
        self.ataqueb = False

    #controles do avanco
        self.avanco = False
        self.limite = 50
        self.limite_reset = 535
        self.avancob = False
        self.limiteb = 570
        self.limite_resetb = 100
        self.posicao = False
        self.sorteio_lado = None
        self.vulneravel_depois = False

        self.pulo = False
        self.pulando = False
        self.descendo = False
        self.chao = False
        self.imagem_pulo = 0
        self.contador_pulo = 0
        self.vulneravel = False
        self.derrotado = False
        self.ataque_baixo = False
        self.ataque_cima = False
        self.estado_anterior = "parado"
        self.contador_animacao = 0
        self.contador_animacao2 = 0
        self.contador_animacao3 = 0
        self.contador_animacao4 = 0
        #mudar nomes pra contador animacao ataque e ataqueb
        self.machado1 = False
        self.machado2 = False
        self.machado2_indo = False
        self.machado3 = False
        self.machado4 = False
        self.battle = False
        self.Sprites()

    def Sprites(self):

        self.tasmania = []
        for i in range(2):
            tasmania_base = carroca_boss_base.subsurface((i*1280,0), (1280,320))
            tasmania_base = pygame.transform.scale(tasmania_base,(1280/3,320/2.8))
            self.tasmania.append(tasmania_base)

        self.tasmania_base_inversa = []
        for i in range(2):
            tasmania_base2 = carroca_boss_base_inversa.subsurface((i * 1280, 0), (1280, 320))
            tasmania_base2 = pygame.transform.scale(tasmania_base2, (1280 / 3, 320 / 2.8))
            self.tasmania_base_inversa.append(tasmania_base2)

        self.tasmania_ataque1 = []
        for i in (0,1,2,3):
            tasmania_ataque = carroca_boss_ataque.subsurface((i*1280,0),(1280,320))
            tasmania_ataque = pygame.transform.scale(tasmania_ataque,(1280/3,320/2.8))
            self.tasmania_ataque1.append(tasmania_ataque)

        self.tasmania_ataque2 = []
        for i in (4,5,6):
            tasmania_ataque2 = carroca_boss_ataque.subsurface((i * 1280, 0), (1280, 320))
            tasmania_ataque2 = pygame.transform.scale(tasmania_ataque2, (1280 / 3, 320 / 2.8))
            self.tasmania_ataque2.append(tasmania_ataque2)

        self.tasmania_ataque3 = []
        for i in (0,1,2,3):
            tasmania_ataqueb = carroca_boss_ataqueb.subsurface((i*1280,0),(1280,320))
            tasmania_ataqueb = pygame.transform.scale(tasmania_ataqueb,(1280/3,320/2.8))
            self.tasmania_ataque3.append(tasmania_ataqueb)

        self.tasmania_ataque4 = []
        for i in (4, 5, 6):
            tasmania_ataqueb2 = carroca_boss_ataqueb.subsurface((i * 1280, 0), (1280, 320))
            tasmania_ataqueb2 = pygame.transform.scale(tasmania_ataqueb2, (1280 / 3, 320 / 2.8))
            self.tasmania_ataque4.append(tasmania_ataqueb2)

        self.tasmania_avanco = []
        for i in range(4):
            tasmania_avanco = carroca_boss_avanco.subsurface((i*1280,0),(1280,320))
            tasmania_avanco = pygame.transform.scale(tasmania_avanco,(1280/3,320/2.8))
            self.tasmania_avanco.append(tasmania_avanco)

        self.tasmania_avancob = []
        for i in range(4):
            tasmania_avanco2 = carroca_boss_avanco2.subsurface((i*1280,0),(1280,320))
            tasmania_avanco2 = pygame.transform.scale(tasmania_avanco2,(1280/3,320/2.8))
            self.tasmania_avancob.append(tasmania_avanco2)

        self.tasmania_vulneravel = []
        for i in range(2):
            tasmania_vulneravel= carroca_boss_vulneravel.subsurface((i*1280,0),(1280,320))
            tasmania_vulneravel = pygame.transform.scale(tasmania_vulneravel,(1280/3,320/2.8))
            self.tasmania_vulneravel.append(tasmania_vulneravel)

        self.tasmania_pulo = []
        for i in range(4):
            tasmania_pulo = carroca_boss_pulo.subsurface((i*1280,0), (1280,320))
            tasmania_pulo = pygame.transform.scale(tasmania_pulo,(1280/3,320/2.8))
            self.tasmania_pulo.append(tasmania_pulo)


        self.tasmania_derrotado = []
        for i in range(1):
            tasmania_derrotado= carroca_boss_derrotado.subsurface((i*1280,0),(1280,320))
            tasmania_derrotado = pygame.transform.scale(tasmania_derrotado,(1280/3,320/2.8))
            self.tasmania_derrotado.append(tasmania_derrotado)

        self.image = self.tasmania[0]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def Reset(self):
        if self.reset_on and leveis.boss_b:
            #Reset do canguru
            canguru.loading_battle = True
            canguru.atual = 0
            canguru.parou = False  # Resetar isso também
            canguru.contador_frames_reducao = 0

            self.contador_reset_b = 0
            self.contador_reset_c = 0
            self.contador_colisao = 0
            self.contador = 0
            self.sorteio_ataque = choice([1,2,3])
            self.tempo_ataque = choice([40,120,160,240,280])
            self.boss_saiu = False
            self.boss_venceu = False
            self.controle_dano = 0
            self.tomou_dano = False

            self.vida = 9

            self.dano = False
            self.indo = True
            self.voltando = False

            self.x = 700
            self.y = 375
            self.contador_teste = 0
            self.contador = 0
            self.contador_batalha = 0

            self.descanso = 0

            # controles de ataque
            self.total = 0
            self.flag_total = False
            self.contador_vulneravel = 0
            self.vulneravel_pronto = False

            self.repeticao1 = 0
            self.repeticao2 = 0
            self.repeticao3 = 0
            self.repeticao4 = 0
            self.repeticao5 = 0

            self.flag_repeticao1 = False
            self.flag_repeticao2 = False
            self.flag_repeticao3 = False
            self.flag_repeticao4 = False
            self.flag_repeticao5 = False

            self.ladoa = True
            self.ladob = False

            self.base = True
            self.base2 = False
            self.ataque = False
            self.ataqueb = False

            # controles do avanco
            self.avanco = False
            self.limite = 50
            self.limite_reset = 535
            self.avancob = False
            self.limiteb = 570
            self.limite_resetb = 100
            self.posicao = False
            self.sorteio_lado = None
            self.vulneravel_depois = False

            self.pulo = False
            self.pulando = False
            self.descendo = False
            self.chao = False
            self.imagem_pulo = 0
            self.contador_pulo = 0
            self.vulneravel = False
            self.derrotado = False
            self.ataque_baixo = False
            self.ataque_cima = False
            self.estado_anterior = "parado"
            self.contador_animacao = 0
            self.contador_animacao2 = 0
            self.contador_animacao3 = 0
            self.contador_animacao4 = 0

            self.machado1 = False
            self.machado2 = False
            self.machado2_indo = False
            self.machado3 = False
            self.machado4 = False
            self.battle = False
            self.Sprites()
            self.reset_on = False

        elif self.reset_on and leveis.boss_c:
            #Reset do canguru
            canguru.loading_battle = True
            canguru.atual = 0
            canguru.parou = False  # Resetar isso também
            canguru.contador_frames_reducao = 0

            self.contador_reset_b = 0
            self.contador_reset_c = 0
            self.contador_colisao = 0
            self.contador = 0
            self.sorteio_ataque = choice([1, 2, 3])
            self.tempo_ataque = choice([120, 240])
            self.boss_saiu = False
            self.boss_venceu = False
            self.controle_dano = 0
            self.tomou_dano = False


            self.vida = 9

            self.dano = False

            self.indo = True
            self.voltando = False

            self.x = 700
            self.y = 375
            self.contador_teste = 0
            self.contador = 0
            self.contador_batalha = 0

            self.descanso = 0

            # controles de ataque
            self.total = 0
            self.flag_total = False
            self.contador_vulneravel = 0
            self.vulneravel_pronto = False

            self.repeticao1 = 0
            self.repeticao2 = 0
            self.repeticao3 = 0
            self.repeticao4 = 0
            self.repeticao5 = 0

            self.flag_repeticao1 = False
            self.flag_repeticao2 = False
            self.flag_repeticao3 = False
            self.flag_repeticao4 = False
            self.flag_repeticao5 = False

            self.ladoa = True
            self.ladob = False

            self.base = True
            self.base2 = False
            self.ataque = False
            self.ataqueb = False

            # controles do avanco
            self.avanco = False
            self.limite = 50
            self.limite_reset = 535
            self.avancob = False
            self.limiteb = 570
            self.limite_resetb = 100
            self.posicao = False
            self.sorteio_lado = None
            self.vulneravel_depois = False

            self.pulo = False
            self.pulando = False
            self.descendo = False
            self.chao = False
            self.imagem_pulo = 0
            self.contador_pulo = 0
            self.vulneravel = False
            self.derrotado = False
            self.ataque_baixo = False
            self.ataque_cima = False
            self.estado_anterior = "parado"
            self.contador_animacao = 0
            self.contador_animacao2 = 0
            self.contador_animacao3 = 0
            self.contador_animacao4 = 0
            # mudar nomes pra contador animacao ataque e ataqueb
            self.machado1 = False
            self.machado2 = False
            self.machado2_indo = False
            self.machado3 = False
            self.machado4 = False
            self.battle = False
            self.Sprites()
            self.reset_on = False

    def Ataques(self):

        if self.base:
            self.y= 375

            self.chao = False
            self.x = 535
            self.base2 = False
            self.ataque = False
            self.ataqueb = False
            self.avanco = False
            self.avancob = False
            self.derrotado = False
            self.pulo = False
            self.pulando = False
            self.descendo = False
            self.posicao = False
            self.ladob = True
            self.ladoa = False
            self.flag_repeticao1 = False
            self.flag_repeticao2 = False
            self.flag_repeticao3 = False
            self.flag_repeticao4 = False
            self.flag_repeticao5 = False
            self.descanso += 1

            if not leveis.boss_b:
                if self.descanso >= 40:
                    if canguru.morreu:
                        self.boss_venceu = True
                        self.base = True
                        self.tempo_ataque = None
                        self.sorteio_ataque = None
                        self.battle = False

                    elif not canguru.morreu:

                        if self.vulneravel_pronto:
                            self.sorteio_ataque =2
                            self.vulneravel_depois = True
                            self.flag_repeticao2 = True
                            self.tempo_ataque = choice([120, 240])
                            self.descanso = 0

                        else:
                            if self.repeticao1 >= 2:
                                self.sorteio_ataque = choice([2, 3])
                                self.tempo_ataque = choice([120, 240])
                                self.descanso = 0
                                self.repeticao1 = 0

                            elif self.repeticao2 >= 2:
                                self.sorteio_ataque = choice([1, 3])
                                self.tempo_ataque = choice([120, 240])
                                self.descanso = 0
                                self.repeticao2 = 0

                            else:
                                self.sorteio_ataque = choice([1, 2, 3])

                                if self.sorteio_ataque == 2 and not self.vulneravel_pronto:
                                    self.flag_repeticao2 = False
                                    self.vulneravel_depois = False
                                    self.tempo_ataque = choice([120, 240])
                                    self.descanso = 0

                                if self.sorteio_ataque == 3:
                                    self.tempo_ataque = None
                                    self.descanso = 0
                                else:
                                    self.tempo_ataque = choice([120, 240])
                                    self.descanso = 0

            else:
                if self.descanso >= 20:
                    if canguru.morreu:
                        self.boss_venceu = True
                        self.base = True
                        self.tempo_ataque = None
                        self.sorteio_ataque = None
                        self.battle = False

                    elif not canguru.morreu:

                        if self.vulneravel_pronto:
                            self.sorteio_ataque = 2
                            self.vulneravel_depois = True
                            self.flag_repeticao2 = True
                            self.tempo_ataque = choice([80, 160])
                            self.descanso = 0

                        else:
                            if self.repeticao1 >= 2:
                                self.sorteio_ataque = choice([2, 3])
                                self.tempo_ataque = choice([80, 160])
                                self.descanso = 0
                                self.repeticao1 = 0

                            elif self.repeticao2 >= 2:
                                self.sorteio_ataque = choice([1, 3])
                                self.tempo_ataque = choice([120, 240])
                                self.descanso = 0
                                self.repeticao2 = 0

                            else:
                                self.sorteio_ataque = choice([1,2,3])

                                if self.sorteio_ataque == 2 and not self.vulneravel_pronto:
                                    self.flag_repeticao2 = False
                                    self.vulneravel_depois = False
                                    self.tempo_ataque = choice([160, 320])
                                    self.descanso = 0

                                if self.sorteio_ataque == 3:
                                    self.tempo_ataque = None
                                    self.descanso = 0
                                else:
                                    self.tempo_ataque = choice([160, 320])
                                    self.descanso = 0

        if self.base2:


            if not self.ataqueb:
                self.x = 0
            self.base = False
            self.ataque = False
            self.ataqueb = False
            self.avanco = False
            self.avancob = False
            self.derrotado = False
            self.pulo = False
            self.pulando = False
            self.descendo = False
            self.posicao = False
            self.ladob = True
            self.ladoa = False
            self.flag_repeticao1 = False
            self.flag_repeticao2 = False
            self.flag_repeticao3 = False
            self.flag_repeticao4 = False
            self.flag_repeticao5 = False

            self.descanso += 1
            if not leveis.boss_b:
             if self.descanso >= 30:
                self.chao = False

                if canguru.morreu:
                    self.boss_venceu = True
                    self.base2 = True
                    self.tempo_ataque = None
                    self.sorteio_ataque = None
                    self.battle = False
                elif not canguru.morreu:

                    if self.vulneravel_pronto:
                        self.sorteio_ataque = choice([5])
                        self.tempo_ataque = choice([60, 180, 300])
                        self.vulneravel_depois = True
                        self.flag_repeticao5 = True
                        self.descanso = 0

                    else:
                        if self.repeticao4 >= 2:
                            self.sorteio_ataque = choice([5])

                            self.descanso = 0
                            self.repeticao4 = 0

                        elif self.repeticao5 >= 2:
                            self.sorteio_ataque = choice([4])
                            self.tempo_ataque = choice([180, 240])
                            self.descanso = 0
                            self.repeticao5 = 0

                        else:
                            self.sorteio_ataque = choice([4,5])
                            if self.sorteio_ataque == 5 and not self.vulneravel_pronto:
                                self.flag_repeticao5 = False

                                self.vulneravel_depois = False
                                self.descanso = 0
                            else:
                                self.tempo_ataque = choice([120,240])
                                self.descanso = 0

            else:
                if self.descanso >= 20:
                    self.chao = False

                    if canguru.morreu:
                        self.boss_venceu = True
                        self.base2 = True
                        self.tempo_ataque = None
                        self.sorteio_ataque = None
                        self.battle = False
                    elif not canguru.morreu:

                        if self.vulneravel_pronto:
                            self.sorteio_ataque = choice([5])
                            self.tempo_ataque = choice([40, 120, 200,280])
                            self.vulneravel_depois = True
                            self.flag_repeticao5 = True

                            self.descanso = 0

                        else:
                            if self.repeticao4 >= 2:
                                self.sorteio_ataque = choice([5])
                                self.tempo_ataque = choice([80, 160,320])
                                self.descanso = 0
                                self.repeticao4 = 0

                            elif self.repeticao5 >= 2:
                                self.sorteio_ataque = choice([4])
                                self.tempo_ataque = choice([180, 240])
                                self.descanso = 0
                                self.repeticao5 = 0

                            else:
                                self.sorteio_ataque = choice([4, 5])
                                if self.sorteio_ataque == 5 and not self.vulneravel_pronto:
                                    self.flag_repeticao5 = False
                                    self.vulneravel_depois = False
                                    self.descanso = 0
                                else:
                                    self.tempo_ataque = choice([80, 160,320])
                                    self.descanso = 0

        if self.sorteio_ataque == 1:
            self.y= 375

            if not self.flag_repeticao1:
                self.total += 1
                self.repeticao1 += 1
                self.repeticao2 = 0
                self.repeticao3 = 0
                self.repeticao4 = 0
                self.repeticao5 = 0
                self.flag_repeticao1 = True
            self.base = False
            self.ataque = True
            self.contador += 1

            if self.contador >= self.tempo_ataque:
                self.base = True
                self.ataque = False
                self.sorteio_ataque  = None
                self.contador = 0

        if self.sorteio_ataque == 2:
            if not self.flag_repeticao2:
                self.repeticao1 = 0
                self.repeticao2 += 1
                self.repeticao3 = 0
                self.repeticao4 =0
                self.repeticao5 = 0
                self.total += 1

                self.flag_repeticao2 = True

            self.base = False
            self.avanco = True
            self.contador += 1

            if self.vulneravel_depois:
                if self.contador >= self.tempo_ataque and self.rect.x >= 320:
                    self.avanco = False
                    self.vulneravel = True
            else:
                if self.contador >= self.tempo_ataque and self.rect.x >= 320:
                    self.base = True
                    self.avanco = False
                    self.sorteio_ataque = None
                    self.contador = 0

        if self.sorteio_ataque == 3:
            if not self.flag_repeticao3:
                self.total +=1
                self.repeticao1 = 0
                self.repeticao2 = 0
                self.repeticao3 = 0
                self.repeticao4 = 0
                self.repeticao5 = 0
                self.flag_repeticao3 = True
            self.contador = 0
            self.pulo = True
            self.base = False

            if self.chao:

                self.descendo = False
                self.pulo = False
                self.ataque = False
                self.avanco = False
                self.base2 = True
                self.sorteio_ataque = None
                self.pulando = False

        if self.sorteio_ataque == 4:

            if not self.flag_repeticao4:
                self.x = 100
                self.contador = 0
                self.total+=1
                self.repeticao4 +=1
                self.repeticao1 =0
                self.repeticao2 =0
                self.repeticao3 =0
                self.repeticao5 = 0
                self.flag_repeticao4 = True
            self.ataqueb = True
            self.base2 = False
            self.contador += 1

            if self.contador >= self.tempo_ataque:
                self.base2 = True
                self.ataqueb = False
                self.sorteio_ataque = None
                self.contador = 0

        if self.sorteio_ataque == 5:

            if not self.flag_repeticao5:
                self.sorteio_lado = choice([1, 2])
                if not leveis.boss_b and not self.vulneravel_pronto:
                    if self.sorteio_lado == 1: #direito


                        self.tempo_ataque = choice([60, 180, 300])

                    if self.sorteio_lado != 1:

                        self.tempo_ataque = choice([120, 240])
                else:
                    if self.sorteio_lado == 1:
                        self.tempo_ataque = choice([40, 120, 200])
                    if self.sorteio_lado != 1:
                        self.tempo_ataque = choice([80, 160])

                self.total +=1
                self.repeticao5 +=1
                self.repeticao1 = 0
                self.repeticao2 = 0
                self.repeticao3 = 0
                self.repeticao4 = 0
                self.flag_repeticao5 = True
            self.base2 = False
            self.avancob = True
            self.contador += 1

            if self.vulneravel_depois:
                if self.contador >= self.tempo_ataque and self.rect.x >= 320:
                    self.avancob = False
                    self.vulneravel = True
            else:
                if self.sorteio_lado == 1:
                    if self.contador >= self.tempo_ataque and self.rect.x >= 320:

                        self.base = True
                        self.sorteio_ataque = None
                        self.avancob = False
                        self.base2 = False
                        self.contador = 0
                        self.sorteio_lado = 0
                else:
                    if self.contador >= self.tempo_ataque and self.rect.x <= -100:
                        self.base2 = True
                        self.base = False
                        self.avancob = False
                        self.sorteio_ataque = None
                        self.contador = 0
                        self.sorteio_lado = 0

        if self.total >= 7 :
            self.vulneravel_pronto = True

        if self.vulneravel: #ZERAR as repeticoes
            if canguru.morreu:
                self.base = True
                self.vulneravel = False
            else:
                self.base2 = False
                self.base = False
                self.vulneravel_depois = False

                self.ataque = False
                self.ataqueb = False
                self.avanco = False
                self.avancob = False
                self.vulneravel_pronto = False
                self.x = 535
                self.total = 0

                self.contador_vulneravel +=1
                if (self.contador_vulneravel >= 150) or (self.contador_colisao >= 4):
                    self.vulneravel = False
                    self.contador_colisao= 0
                    self.base = True
                    self.base2 = False
                    self.descanso = 0
                    self.sorteio_ataque = None
                    self.contador = 0
                    self.contador_vulneravel = 0

                    self.flag_repeticao1 = False
                    self.flag_repeticao2 = False
                    self.flag_repeticao3 = False
                    self.flag_repeticao4 = False
                    self.flag_repeticao5 = False

                    self.repeticao1 = 0
                    self.repeticao2 = 0
                    self.repeticao3 = 0
                    self.repeticao4 = 0
                    self.repeticao5 = 0

    def Dificuldade(self):
        if leveis.boss_a:
            self.velocidade_animacao_base = 0.10
            self.velocidade_animacao_base2 = 0.10
            self.velocidade_animacao_avanco = 0.25
            self.velocidade_avanco = 8
            self.velocidade_animacao_vulneravel = 0.15
            self.velocidade_animacao_ataque = 0.10
            self.velocidade_animacao_ataque2 = 0.08
            self.velocidade_animacao_ataque3 = 0.10
            self.velocidade_animacao_ataque4 = 0.08
            self.velocidade_pulo = 0.25
            self.velocidade_pulando = 8
        elif leveis.boss_b:
            self.velocidade_animacao_base = 0.15
            self.velocidade_animacao_base2 = 0.15
            self.velocidade_animacao_avanco = 0.35
            self.velocidade_avanco = 12
            self.velocidade_animacao_vulneravel = 0.15
            self.velocidade_animacao_ataque = 0.15
            self.velocidade_animacao_ataque2 = 0.13
            self.velocidade_animacao_ataque3 = 0.15
            self.velocidade_animacao_ataque4 = 0.13
            self.velocidade_pulo = 0.35
            self.velocidade_pulando = 12
        elif leveis.boss_c:
            self.velocidade_animacao_base = 0.13
            self.velocidade_animacao_base2 = 0.13
            self.velocidade_animacao_avanco = 0.28
            self.velocidade_avanco = 12
            self.velocidade_animacao_vulneravel = 0.13
            self.velocidade_animacao_ataque = 0.13
            self.velocidade_animacao_ataque2 = 0.11
            self.velocidade_animacao_ataque3 = 0.13
            self.velocidade_animacao_ataque4 = 0.11
            self.velocidade_pulo = 0.25
            self.velocidade_pulando = 9

    def Animacao(self):

        if self.base:
            estado_atual = "base"
        elif self.base2:
            estado_atual = "base2"
        elif self.ataque:
            estado_atual = "ataque"
        elif self.ataqueb:
            estado_atual = "ataque2"
        elif self.pulo:
            estado_atual = "pulo"
        elif self.pulando:
            estado_atual = "pulando"
        elif self.descendo:
            estado_atual = "descendo"
        elif self.avanco:
            estado_atual = "avanco"
        elif self.avancob:
            estado_atual = "avanco2"
        elif self.vulneravel:
            estado_atual = "vulneravel"
        elif self.derrotado:
            estado_atual = "derrotado"
        else:
            estado_atual = None

        if estado_atual != self.estado_anterior:
            self.contador_animacao = 0
            self.estado_anterior = estado_atual

        if self.base:
            if self.contador_animacao >= len(self.tasmania):
                self.contador_animacao = 0
            self.image = self.tasmania[int(self.contador_animacao)]
            self.contador_animacao += self.velocidade_animacao_base

        elif self.base2:
            if self.contador_animacao >= len(self.tasmania_base_inversa):
                self.contador_animacao = 0
            self.image = self.tasmania_base_inversa[int(self.contador_animacao)]
            self.contador_animacao += self.velocidade_animacao_base2

        elif self.ataque:

            if self.contador_animacao == 0 and self.contador_animacao2 == 0:
                self.sorteio_machado = choice([1, 2])

            if self.sorteio_machado == 1:  # baixo

                if self.contador_animacao >= 2:

                    if not self.machado1:
                        self.machado1 = True

                if self.contador_animacao >= len(self.tasmania_ataque1):

                    self.contador_animacao = 0

                    self.contador_animacao2 = 0

                    self.sorteio_machado = None

                else:

                    self.image = self.tasmania_ataque1[int(self.contador_animacao)]

                    self.contador_animacao += self.velocidade_animacao_ataque

            if self.sorteio_machado == 2:  # cima

                if self.contador_animacao2 >= 1:
                    self.machado2 = True

                if self.contador_animacao2 >= len(self.tasmania_ataque2):

                    self.contador_animacao2 = 0

                    self.contador_animacao = 0

                    self.sorteio_machado = None

                else:

                    self.image = self.tasmania_ataque2[int(self.contador_animacao2)]

                    self.contador_animacao2 += self.velocidade_animacao_ataque2

        elif self.ataqueb:

            if self.contador_animacao3 == 0 and self.contador_animacao4 == 0:
                self.sorteio_machadob = choice([3, 4])

            if self.sorteio_machadob == 3:

                if self.contador_animacao3 >= 2:

                    if not self.machado3:
                        self.machado3 = True

                if self.contador_animacao3 >= len(self.tasmania_ataque3):
                    self.contador_animacao3 = 0
                    self.contador_animacao4 = 0
                    self.sorteio_machadob = None

                else:

                    self.image = self.tasmania_ataque3[int(self.contador_animacao3)]
                    self.contador_animacao3 += self.velocidade_animacao_ataque3

            if self.sorteio_machadob == 4:
                if self.contador_animacao4 >= 1:

                    if not self.machado4:
                        self.machado4 = True

                if self.contador_animacao4 >= len(self.tasmania_ataque4):
                    self.contador_animacao3 = 0
                    self.contador_animacao4 = 0
                    self.sorteio_machadob = None

                else:
                    self.image = self.tasmania_ataque4[int(self.contador_animacao4)]
                    self.contador_animacao4 += self.velocidade_animacao_ataque4

        elif self.avanco:
            if self.indo and not self.voltando:
                self.x -= self.velocidade_avanco
                if self.x <= self.limite:
                    self.voltando = True
                    self.indo = False
            elif self.voltando:
                self.x += self.velocidade_avanco
                if self.x >= self.limite_reset:
                    self.voltando = False
                    self.indo = True

            if self.contador_animacao >= len(self.tasmania_avanco):
                self.contador_animacao = 0
            self.image = self.tasmania_avanco[int(self.contador_animacao)]
            self.contador_animacao += self.velocidade_animacao_avanco

        elif self.avancob:
            if not self.voltando:
                self.indo = True

            if not self.posicao:
                self.x = 100
                self.posicao = True

            if self.indo and not self.voltando:
                self.x += self.velocidade_avanco

                if self.x >= self.limiteb: #650
                    self.voltando = True
                    self.indo = False

            if self.x <= self.limite_resetb:
                self.voltando= False

            elif self.voltando:
                self.x -= self.velocidade_avanco

            if self.contador_animacao >= len(self.tasmania_avancob):
                self.contador_animacao = 0
            self.image = self.tasmania_avancob[int(self.contador_animacao)]
            self.contador_animacao += self.velocidade_animacao_avanco

        elif self.pulo and not self.pulando:
            self.base = False

            if 0 <= self.contador_pulo < 1:
                self.image = self.tasmania_pulo[0]

            elif 1 <= self.contador_pulo < 4:

                self.y -= 5
                self.x -= 5
                self.image = self.tasmania_pulo[1]
                if leveis.boss_c:
                    self.y -= 10

            self.contador_pulo += self.velocidade_pulo

            if self.contador_pulo >= 4:
                self.pulo = False

                self.pulando = True
                self.contador_pulo = 0
                self.x_pulando = self.x
                self.y_inicio_pulo = self.y

        elif self.pulando and not self.chao:

            self.x -= self.velocidade_pulando
            progresso = (self.x_pulando - self.x) / (self.x_pulando - 100)
            progresso = max(0.0, min(1.0, progresso))


            if progresso < 0.5:
                self.image = self.tasmania_pulo[2]
                self.y -= 5  # Continua subindo
                self.y_inicio_pulo = min(self.y_inicio_pulo, self.y)  # Atualiza o ponto mais alto

            # Fase de descida
            else:
                self.descendo = True
                self.image = self.tasmania_pulo[3]
                # Calcula a descida baseada no progresso
                yg = 400
                self.y = self.y_inicio_pulo + (yg - self.y_inicio_pulo) * (progresso - 0.5) * 2
                if self.y >= 400:
                    self.chao = True

        elif self.vulneravel:
            if self.contador_animacao >= len(self.tasmania_vulneravel):
                self.contador_animacao = 0
            self.image = self.tasmania_vulneravel[int(self.contador_animacao)]
            self.contador_animacao += self.velocidade_animacao_vulneravel

        elif self.derrotado:
            self.base = False
            self.image = self.tasmania_derrotado[0]

    def Colisao(self):
        if self.base:
            self.tasmania_hitbox = pygame.Rect(self.rect.x + 160, self.rect.y+5 , 100, 100)
            #pygame.draw.rect(tela, (0, 100, 0), self.tasmania_hitbox, 2)

        if self.base2:
            self.tasmania_hitbox = pygame.Rect(self.rect.x + 243, self.rect.y+5 , 100, 100)
            #pygame.draw.rect(tela, (190, 200, 0), self.tasmania_hitbox, 2)

        if self.ataque:
            self.tasmania_hitbox = pygame.Rect(self.rect.x + 160, self.rect.y+5 , 100, 100)
            #pygame.draw.rect(tela, (30, 100, 100), self.tasmania_hitbox, 2)

        if self.ataqueb:
            self.tasmania_hitbox = pygame.Rect(self.rect.x + 150, self.rect.y+5 , 100, 100)
            #pygame.draw.rect(tela, (190, 50, 100), self.tasmania_hitbox, 2)

        if self.avanco:
            if self.indo:
                self.tasmania_hitbox = pygame.Rect(self.rect.x + 150, self.rect.y + 5, 100, 100)
                #pygame.draw.rect(tela, (190, 0, 150), self.tasmania_hitbox, 2)
            if self.voltando:
                self.tasmania_hitbox = pygame.Rect(self.rect.x + 170, self.rect.y + 5, 100, 100)
                #pygame.draw.rect(tela, (190, 200, 200), self.tasmania_hitbox, 2)

        if self.avancob:
            if self.indo:
                self.tasmania_hitbox = pygame.Rect(self.rect.x + 165, self.rect.y + 5, 100, 100)
                #pygame.draw.rect(tela, (10, 40, 170), self.tasmania_hitbox, 2)
            if self.voltando:
                self.tasmania_hitbox = pygame.Rect(self.rect.x + 150, self.rect.y + 5, 100, 100)
                #pygame.draw.rect(tela, (150, 200, 100), self.tasmania_hitbox, 2)

        if self.pulo:
            self.tasmania_hitbox = pygame.Rect(self.rect.x + 150, self.rect.y + 5, 100, 100)
            #pygame.draw.rect(tela, (0, 200, 100), self.tasmania_hitbox, 2)

        if self.pulando and not self.descendo:
            self.tasmania_hitbox = pygame.Rect(self.rect.x + 150, self.rect.y, 90, 100)
            #pygame.draw.rect(tela, (200, 200, 200), self.tasmania_hitbox, 2)

        if self.descendo:
            self.tasmania_hitbox = pygame.Rect(self.rect.x + 150, self.rect.y, 90, 110)
            #pygame.draw.rect(tela, (200, 200, 0), self.tasmania_hitbox, 2)

        if self.vulneravel:
            self.tasmania_vulneravel_hitbox = pygame.Rect(self.rect.x + 220, self.rect.y + 10, 10, 100)
            #pygame.draw.rect(tela, (80, 120, 250), self.tasmania_vulneravel_hitbox, 2)
            self.tasmania_hitbox = pygame.Rect(self.rect.x + 160, self.rect.y+5 , 100, 100)
            #pygame.draw.rect(tela, (0, 100, 0), self.tasmania_hitbox, 2)

    #canguru e bumerangue
        if not self.vulneravel:
            canguru_hitbox = canguru.Colisao()
            for v in canguru_hitbox:
                if self.tasmania_hitbox.colliderect(v):

                    if canguru.contador_colisao == 0:
                        vidas_rosto.dano = True
                        vidas_numeros.dano = True
                        canguru.contador_colisao = 1

            if bumerangue is not None:  # Se o bumerangue existe
                bumerangue_hitbox = bumerangue.Colisao() or []
                for v in bumerangue_hitbox:
                    if self.tasmania_hitbox.colliderect(v):
                        bumerangue.indo = False
                        bumerangue.voltando = True
                        bumerangue.acertou = True

        if self.vulneravel:
            if bumerangue is not None:  # Se o bumerangue existe
                bumerangue_hitbox = bumerangue.Colisao() or []
                for v in bumerangue_hitbox:
                    if self.tasmania_vulneravel_hitbox.colliderect(v):
                        if self.controle_dano == 0:

                            bumerangue.indo = False
                            bumerangue.voltando = True
                            bumerangue.acertou = True
                            self.dano = True
                            self.controle_dano += 1

            canguru_hitbox = canguru.Colisao()
            for v in canguru_hitbox:
                if self.tasmania_hitbox.colliderect(v):

                    if canguru.contador_colisao == 0:
                        vidas_rosto.dano = True
                        vidas_numeros.dano = True
                        canguru.contador_colisao = 1

    def update(self):

        if not self.boss_saiu and not self.reset_on:
            self.Dificuldade()
            if not self.derrotado:
                self.Colisao()

            if self.vida <= 0 and not self.boss_saiu and not self.reset_on:
                self.base = False
                self.battle = False
                self.derrotado = True
                self.vulneravel = False
                self.image = self.tasmania_derrotado[0]
                self.x -=3
                leveis.boss_perto = False
                leveis.boss = False
                leveis.boss_derrotado = True
                canguru.parou = False
                self.battle = False

            if self.dano:
                self.tomou_dano = True
                self.vida -=1
                self.contador_colisao +=1
                self.dano = False

            if self.tomou_dano:
                self.controle_dano +=1

                #Tempo de dano
                if self.controle_dano == 10:
                   self.controle_dano = 0
                   self.tomou_dano = False

            if canguru.parou:
                self.battle = True

            if not canguru.parou and not self.battle and not canguru.morreu:
                 self.x -= 2.1

            if self.battle:
                self.contador_batalha +=1
                if self.contador_batalha > 15:
                    self.Ataques()
            if self.chao:
                self.x =0
            if self.base2:
                self.x=0

            if self.sorteio_ataque == 4:
                self.ataqueb = True
                self.x =100
            if self.ataqueb:
                self.x = 100
                self.base2 = False

            self.Animacao()
            self.rect.center = (self.x, self.y)
            tela.blit(self.image, self.rect)

            if self.x <= -60:
                self.boss_saiu = True
                self.derrotado = False
                self.base = True
                self.reset_on = True
        if not self.vulneravel:
            colisao.contador_impacto = 0
        if self.vulneravel and not self.derrotado:
            if 0 < colisao.contador_impacto < 3:
                if colisao.contador_impacto % 4 < 2:
                    self.image.set_alpha(100)
                else:
                    self.image.set_alpha(180)
            if colisao.contador_impacto == 0:
                self.image.set_alpha(255)
class Seta(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 100
        self.y = 100
        self.contador = 0

    def sprites(self):
        self.setas = []
        for i in range (3):
            seta = carroca_seta.subsurface((i * 1024, 0), (1024, 1024))
            seta = pygame.transform.scale(seta, (1024 / 4, 1024 /4))
            self.setas.append(seta)
        self.image = self.setas[0]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def animacao(self):
        if self.contador >= len(self.setas):
            self.contador = 0
        self.image = self.setas[int(self.contador)]
        self.contador += 0.235
    def update(self):
        if leveis.boss and canguru.loading_battle:
            self.sprites()
            self.animacao()
            if self.contador <1:
               self.x = 150
            if 1 < self.contador < 2:
               self.x = 300
            if 2 < self.contador < 3:
               self.x = 450
            self.rect.center = (self.x, self.y)
            tela.blit(self.image, self.rect)
class Marcador_boss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 320
        self.y = 120
        self.contador = 0

        self.image = carroca_marcador_boss
        self.image = pygame.transform.scale(self.image, (400 / 5, 400 / 5))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self):
        if leveis.boss_perto and not leveis.boss:
            self.contador += 1

            if self.contador % 36 < 16:
                self.image.set_alpha(100)
            else:
                self.image.set_alpha(255)


            tela.blit(self.image, self.rect)
        else:
            self.image = None
            self.rect = None
#--
class Machado(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.indo = False
        self.contador = 0
        self.x = 480
        self.y = 400
        self.velocidade = 0

    def Dificuldade(self):
        if leveis.boss_a:
            self.velocidade = 15
        else:
            self.velocidade = 18#20

    def Sprites(self):
        self.machado = []
        for i in range (7):
            machado = carroca_machado.subsurface((i * 1024, 0), (1024, 1024))
            machado = pygame.transform.scale(machado, (1024 / 19, 1024 / 19))
            self.machado.append(machado)
        self.image = self.machado[0]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def Animacao(self):
        if self.contador >= len(self.machado):
            self.contador = 0
        self.image = self.machado[int(self.contador)]
        self.contador += 0.25

    def Colisao(self):
        self.machado1_hitbox = pygame.Rect(self.rect.x+5, self.rect.y + 5, 40, 50)
        #pygame.draw.rect(tela, (250, 200, 250), self.machado1_hitbox, 2)

        canguru_hitbox = canguru.Colisao()
        for v in canguru_hitbox:
            if self.machado1_hitbox.colliderect(v):
                if canguru.contador_colisao == 0:
                    vidas_rosto.dano = True
                    vidas_numeros.dano = True
                    canguru.contador_colisao = 1

    def update(self):
        if tasmania.machado1:
            self.Sprites()
            self.Colisao()
            self.Animacao()
            self.Dificuldade()

            tela.blit(self.image, self.rect)
            self.x -= self.velocidade

        if self.x <= 150:
            self.indo = True

        if self.x <= -22:
            tasmania.machado1= False
            self.indo = False
            self.x = 480
class Machado2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.indo = False
        self.contador = 0
        self.x = 550
        self.y = 350
        self.velocidade = 0

    def Dificuldade(self):
        if leveis.boss_a:
            self.velocidade = 17
        else:
            self.velocidade = 20#22

    def Sprites(self):
        self.machado = []
        for i in range(7):
            machado = carroca_machado.subsurface((i * 1024, 0), (1024, 1024))
            machado = pygame.transform.scale(machado, (1024 / 19, 1024 / 19))
            self.machado.append(machado)
        self.image = self.machado[0]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def Animacao(self):
        if self.contador >= len(self.machado):
            self.contador = 0
        self.image = self.machado[int(self.contador)]
        self.contador += 0.25

    def Colisao(self):
        self.machado2_hitbox = pygame.Rect(self.rect.x+5, self.rect.y + 5, 40, 50)
        #pygame.draw.rect(tela, (250, 200, 250), self.machado2_hitbox, 2)

        canguru_hitbox = canguru.Colisao()
        for v in canguru_hitbox:
            if self.machado2_hitbox.colliderect(v):
                if canguru.contador_colisao == 0:
                    vidas_rosto.dano = True
                    vidas_numeros.dano = True
                    canguru.contador_colisao = 1

    def update(self):



        if tasmania.machado2:
            self.Sprites()
            self.Animacao()
            self.Dificuldade()
            self.Colisao()
            tela.blit(self.image, self.rect)

            self.x -= self.velocidade

        if self.x <= 50:
            self.indo = True

        if self.x <= -22:
            tasmania.machado2 = False
            self.indo = False
            self.x = 550
class Machado3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.contador = 0
        self.x = 115 #665
        self.y = 400
        self.velocidade = 0

    def Dificuldade(self):
        if leveis.boss_a:
            self.velocidade = 15
        else:
            self.velocidade = 18#20


    def Sprites(self):
        self.machado = []
        for i in range(7):
            machado = carroca_machadob.subsurface((i * 1024, 0), (1024, 1024))
            machado = pygame.transform.scale(machado, (1024 / 19, 1024 / 19))
            self.machado.append(machado)
        self.image = self.machado[0]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def Animacao(self):
        if self.contador >= len(self.machado):
            self.contador = 0
        self.image = self.machado[int(self.contador)]
        self.contador += 0.25

    def Colisao(self):
        self.machado3_hitbox = pygame.Rect(self.rect.x+5, self.rect.y + 5, 40, 50)
        #pygame.draw.rect(tela, (250, 200, 250), self.machado3_hitbox, 2)

        canguru_hitbox = canguru.Colisao()
        for v in canguru_hitbox:
            if self.machado3_hitbox.colliderect(v):
                if canguru.contador_colisao == 0:
                    vidas_rosto.dano = True
                    vidas_numeros.dano = True
                    canguru.contador_colisao = 1

    def update(self):

        if tasmania.machado3:
            self.Sprites()
            self.Animacao()
            self.Dificuldade()
            self.Colisao()

            tela.blit(self.image, self.rect)

            self.x += self.velocidade

        if self.x >= 665:
            tasmania.machado3 = False
            self.x = 115
class Machado4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.indo = False
        self.contador = 0
        self.x = 100
        self.y = 350
        self.velocidade = 0

    def Dificuldade(self):
        if leveis.boss_a:
            self.velocidade = 17
        else:
            self.velocidade = 20#22




    def Sprites(self):
        self.machado = []
        for i in range(7):
            machado = carroca_machadob.subsurface((i * 1024, 0), (1024, 1024))
            machado = pygame.transform.scale(machado, (1024 / 19, 1024 / 19))
            self.machado.append(machado)
        self.image = self.machado[0]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def Animacao(self):
        if self.contador >= len(self.machado):
            self.contador = 0
        self.image = self.machado[int(self.contador)]
        self.contador += 0.25

    def Colisao(self):
        self.machado4_hitbox = pygame.Rect(self.rect.x + 5, self.rect.y + 5, 40, 50)
        #pygame.draw.rect(tela, (250, 200, 250), self.machado4_hitbox, 2)

        canguru_hitbox = canguru.Colisao()
        for v in canguru_hitbox:
            if self.machado4_hitbox.colliderect(v):
                if canguru.contador_colisao == 0:
                    vidas_rosto.dano = True
                    vidas_numeros.dano = True
                    canguru.contador_colisao = 1

    def update(self):
        if tasmania.machado4:
            self.Sprites()
            self.Animacao()
            self.Dificuldade()
            self.Colisao()

            tela.blit(self.image, self.rect)
            self.x += self.velocidade

        if self.x >= 665:
            tasmania.machado4 = False
            self.x = 100
class Machado5(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.direita = False
        self.esquerda = False
        self.indo5 = False
        self.contador = 0
        self.contador_reset =0
        self.x = tasmania.x
        self.y = tasmania.y
        self.velocidade = 0
        self.alvo_x = 0 # Novo atributo para a posição X do alvo
        self.alvo_y = 0 # Novo atributo para a posição Y do alvo
        self.velocidade_x = 0 # Novo atributo para a velocidade X do machado
        self.velocidade_y = 0 # Novo atributo para a velocidade Y do machado
        self.machado_disparado = False # Flag para controlar o disparo
        self.x, self.y = tasmania.rect.center
        self.machado_disparado = False
        self.Sprites()

    def Dificuldade(self):
        if not leveis.boss_a:
            self.velocidade = 15

    def Sprites(self):
        self.machado = []
        for i in range (7):
            machado = carroca_machado.subsurface((i * 1024, 0), (1024, 1024))
            machado = pygame.transform.scale(machado, (1024 / 19, 1024 / 19))
            self.machado.append(machado)
        self.image = self.machado[0]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        self.machadob = []
        for i in range (7):
            machadob = carroca_machadob.subsurface((i * 1024, 0), (1024, 1024))
            machadob = pygame.transform.scale(machadob, (1024 / 19, 1024 / 19))
            self.machadob.append(machadob)
        self.image = self.machadob[0]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def Animacao(self):
        if self.esquerda:
            if self.contador >= len(self.machado):
                self.contador = 0
            self.image = self.machado[int(self.contador)]
            self.contador += 0.25
        else:
            if self.contador >= len(self.machado):
                self.contador = 0
            self.image = self.machadob[int(self.contador)]
            self.contador += 0.25

    def Colisao(self):
        self.machado5_hitbox = pygame.Rect(self.rect.x+5, self.rect.y + 5, 40, 50)
        #pygame.draw.rect(tela, (250, 200, 250), self.machado5_hitbox, 2)

        canguru_hitbox = canguru.Colisao()
        for v in canguru_hitbox:
            if self.machado5_hitbox.colliderect(v):
                if canguru.contador_colisao == 0:
                    vidas_rosto.dano = True
                    vidas_numeros.dano = True
                    canguru.contador_colisao = 1

    def calcular_direcao(self):
        """Calcula a direção do machado baseado no estado do canguru no momento do disparo"""
        self.alvo_x, self.alvo_y = canguru.rect.center  # Pega a posição atual do canguru

        if not canguru.pulando:  # Se o canguru NÃO está pulando, mira apenas no eixo X
            delta_x = self.alvo_x - self.x
            distancia = max(1, abs(delta_x))  # Usamos abs() pois só importa a magnitude

            if leveis.boss_b:
                velocidade_total = 20
                self.velocidade_x = (delta_x / distancia) * velocidade_total
                self.velocidade_y = 0  # Zera o Y para não ter movimento vertical
            else:
                velocidade_total = 22
                self.velocidade_x = (delta_x / distancia) * velocidade_total
                self.velocidade_y = 0  # Zera o Y para não ter movimento vertical
        else:  # Se o canguru ESTÁ pulando, mira em X e Y
            delta_x = self.alvo_x - self.x
            delta_y = self.alvo_y - self.y
            distancia = max(1, math.hypot(delta_x, delta_y))  # Distância euclidiana

            if leveis.boss_b:
                velocidade_total = 20
                self.velocidade_x = (delta_x / distancia) * velocidade_total
                self.velocidade_y = (delta_y / distancia) * velocidade_total
            else:
                velocidade_total = 22
                self.velocidade_x = (delta_x / distancia) * velocidade_total
                self.velocidade_y = (delta_y / distancia) * velocidade_total

    def reset_machado(self):
        """Reseta o machado para a posição inicial"""
        self.machado_disparado = False
        self.x, self.y = tasmania.rect.center
        self.rect.center = (self.x, self.y)
        self.contador_reset = 0

    def update(self):
        if not leveis.boss_a:
            # Se o machado ainda não foi disparado, e o tasmania está atacando, inicia o disparo
            if (tasmania.avanco or tasmania.avancob) and not self.machado_disparado:
                direita = canguru.rect.centerx > tasmania.rect.centerx

                if direita:
                    self.direita = True
                    self.esquerda = False
                else:
                    self.direita = False
                    self.esquerda = True

                self.machado_disparado = True

                self.x, self.y = tasmania.rect.center
                self.rect.center = (self.x, self.y)

                # Captura a posição atual do canguru no momento do disparo
                self.alvo_x, self.alvo_y = canguru.rect.center

                # Calcula a direção inicial (apenas uma vez no disparo)
                self.calcular_direcao()

            # Se o machado foi disparado, ele segue voando
            if self.machado_disparado:
                self.contador_reset += 1
                self.x += self.velocidade_x
                self.y += self.velocidade_y
                self.rect.center = (int(self.x), int(self.y))

                self.Colisao()
                self.Animacao()
                self.Dificuldade()
                tela.blit(self.image, self.rect)

                # Reset se sair da tela ou atingir o alvo
                if leveis.boss_b:
                    if self.contador_reset >= 40:
                        self.reset_machado()
                elif leveis.boss_c:
                    if self.contador_reset >= 40:
                        self.reset_machado()


            # Se não está em movimento, apenas fica preso no personagem
            elif not self.machado_disparado:
                self.x, self.y = tasmania.rect.center
                self.rect.center = (self.x, self.y)
class Machado6(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ataques = 0
        self.ataque1 = True
        self.ataque2 = False
        self.ataque3 = False
        self.indo5 = False
        self.contador = 0
        self.contador_reset =0
        self.x = tasmania.x
        self.y = tasmania.y
        self.velocidade = 0
        self.alvo_x = 0 # Novo atributo para a posição X do alvo
        self.alvo_y = 0 # Novo atributo para a posição Y do alvo
        self.velocidade_x = 0 # Novo atributo para a velocidade X do machado
        self.velocidade_y = 0 # Novo atributo para a velocidade Y do machado
        self.machado_disparado = False # Flag para controlar o disparo
        self.x, self.y = tasmania.rect.center
        self.machado_disparado = False
        self.Sprites()

    def Sprites(self):
        self.machado = []
        for i in range (7):
            machado = carroca_machado.subsurface((i * 1024, 0), (1024, 1024))
            machado = pygame.transform.scale(machado, (1024 / 19, 1024 / 19))
            self.machado.append(machado)
        self.machado3 = []
        for i in range(7):
            machadob = carroca_machadob.subsurface((i * 1024, 0), (1024, 1024))
            machadob = pygame.transform.scale(machadob, (1024 / 19, 1024 / 19))
            self.machado3.append(machadob)


        self.image = self.machado[0]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def Animacao(self):
        if not self.ataque3:
            if self.contador >= len(self.machado):
                self.contador = 0
            self.image = self.machado[int(self.contador)]
            self.contador += 0.25
        else:
            if self.contador >= len(self.machado):
                self.contador = 0
            self.image = self.machado3[int(self.contador)]
            self.contador += 0.25

    def Colisao(self):
        self.machado6_hitbox = pygame.Rect(self.rect.x+5, self.rect.y + 5, 40, 50)
        #pygame.draw.rect(tela, (250, 200, 250), self.machado6_hitbox, 2)

        canguru_hitbox = canguru.Colisao()
        for v in canguru_hitbox:
            if self.machado6_hitbox.colliderect(v):
                if canguru.contador_colisao == 0:
                    vidas_rosto.dano = True
                    vidas_numeros.dano = True
                    canguru.contador_colisao = 1

    def update(self):

        if leveis.boss_c:

            # Se o machado ainda não foi disparado, e o tasmania está atacando, inicia o disparo
            if (tasmania.pulo or tasmania.pulando) and not self.machado_disparado:
                self.machado_disparado = True


            # Se o machado foi disparado, ele segue voando
            if self.machado_disparado:
                self.contador_reset += 1
                if self.ataque3: #ataque depois do pulo
                    self.x += 18

                elif self.ataque2: #ataque no pulo
                    self.y += 16

                elif self.ataque1: #ataque antes do pulo
                    self.x -= 17
                    if self.rect.x <=100:
                        self.x -= 10

                self.rect.center = (int(self.x), int(self.y))

                self.Colisao()
                self.Animacao()
                tela.blit(self.image, self.rect)

                # Reset se sair da tela ou atingir o alvo
                if self.contador_reset >= 28:
                    self.reset_machado()

            # Se não está em movimento, apenas fica preso no personagem
            elif not self.machado_disparado:
                self.x, self.y = tasmania.rect.center
                self.rect.center = (self.x, self.y)


    def reset_machado(self):
        """Reseta o machado para a posição inicial"""
        if self.ataque1:
            self.ataque1 = False
            self.ataque2 = True
            self.machado_disparado = False
            self.contador_reset = 0
        if self.ataque2 and self.machado_disparado:
            self.ataque2 = False
            self.ataque3 = True
            self.machado_disparado = False
            self.contador_reset = 0
        if self.ataque3 and self.machado_disparado:
            self.ataque3 = False
            self.ataque1 = True
            self.machado_disparado = False
            self.contador_reset = 0

        self.x, self.y = tasmania.rect.center
        self.rect.center = (self.x, self.y)

#------------inimigos-----------#
class Dingo (pygame.sprite.Sprite):
    def __init__(self,bumerangue,canguru):
        pygame.sprite.Sprite.__init__(self)

        self.bumerangue = bumerangue
        self.canguru = canguru
        self.andando = [] #para gerenciar x e y
        self.spawn = False
        self.spawn_on = True
        self.correndo = True
        self.ataque = False
        self.baixo = False
        self.cima = False
        self.velocidade = 5
        self.contador_dingo = 0

        self.y = choice([268, 300])
        self.x = randint (1100,1150)
        self.andando.append([self.x, self.y])

    def get_layer(self):
        # Define a camada de desenho com base no Y
        return 7.1 if self.y == 300 else 6

    def Sprites(self):

        self.dingos = []
        self.dingos.append(carroca_dingo.subsurface((0*1200,0), (1200,1200)))
        self.dingos.append(carroca_dingo.subsurface((1*1200,0), (1200,1200)))

        self.atacando_1 = []
        self.atacando_1.append(carroca_dingo.subsurface((2*1200,0), (1200,1200)))
        self.atacando_1.append(carroca_dingo.subsurface((3*1200,0), (1200,1200)))

        self.atacando_2 = []
        self.atacando_2.append(carroca_dingo.subsurface((4 * 1200, 0), (1200, 1200)))
        self.atacando_2.append(carroca_dingo.subsurface((5 * 1200, 0), (1200, 1200)))

        self.image = self.dingos[0]
        self.image = pygame.transform.scale(self.image, (1200 / 8, 1200 / 8))
        self.rect = self.image.get_rect()
        self.rect.center = -200, -200

    def Dificuldade(self):
        if leveis.lvl_0:
            if self.correndo and not self.ataque:
                self.velocidade_animacao = 0.10
                self.velocidade = 5
            elif self.ataque:
                self.velocidade_animacao = 0.05
                self.velocidade += 0.2
        if leveis.lvl_1:
            if self.correndo and not self.ataque:
                self.velocidade_animacao = 0.10
                self.velocidade = 6
            elif self.ataque:
                self.velocidade_animacao = 0.06
                self.velocidade += 0.2
        if leveis.lvl_2:
            if self.correndo and not self.ataque:
                self.velocidade_animacao = 0.12
                self.velocidade = 8
            elif self.ataque:
                self.velocidade_animacao = 0.07
                self.velocidade += 0.2
        if leveis.lvl_3:
            if self.correndo and not self.ataque:
                self.velocidade_animacao = 0.13
                self.velocidade = 9
            elif self.ataque:
                self.velocidade_animacao = 0.08
                self.velocidade += 0.3
        if leveis.lvl_4:
            if self.correndo and not self.ataque:
                self.velocidade_animacao = 0.14
                self.velocidade = 10
            elif self.ataque:
                self.velocidade_animacao = 0.09
                self.velocidade += 0.3
        if leveis.lvl_5:
            if self.correndo and not self.ataque:
                self.velocidade_animacao = 0.15
                self.velocidade = 10
            elif self.ataque:
                self.velocidade_animacao = 0.1
                self.velocidade += 0.3

    def Animacao(self):

        if self.correndo:
            if self.contador_dingo >= len(self.dingos):
                self.contador_dingo = 0
            self.image = self.dingos[int(self.contador_dingo)]
            self.contador_dingo += self.velocidade_animacao

        if self.ataque:
            if self.contador_dingo >= len(self.atacando_1):
                self.contador_dingo = 0
            self.image = self.atacando_1[int(self.contador_dingo)]
            self.contador_dingo += self.velocidade_animacao

        for i in self.andando:
            i[0] -= self.velocidade
            if i[0] <= -200 and not canguru.morreu:
                # REMOVE A POSIÇÃO ANTIGA E CRIA UMA NOVA
                self.andando.remove(i)
                self.y = choice([268, 300])  # Novo Y aleatório
                self.x = randint (1100,1150)
                self.andando.append([self.x, self.y])  # Nova posição

                # ATUALIZA cima/baixo DE FORMA SEGURA



                # RESETA ANIMAÇÃO E ESTADOS
                self.contador_dingo = 0
                self.ataque = False
                self.correndo = True
                self.spawn = False
                self.velocidade = 5
                self.spawn_on = True

                # ATUALIZA CAMADA (layer)
                grupos = self.groups()
                if grupos:
                    grupo = grupos[0]
                    grupo.change_layer(self, self.get_layer())

    def Colisao(self):
        self.dingo_hitbox = pygame.Rect(self.rect.x + 20, self.rect.y + 35, 100, 120)
        pygame.draw.rect(tela, (0, 0, 250), self.dingo_hitbox, 2)
        canguru_hitbox = canguru.Colisao()

        self.dingo_corrida_hitbox = pygame.Rect(self.rect.x - 300, self.rect.y + 50, 350, 100)
        #pygame.draw.rect(tela, (0, 0, 0), self.dingo_corrida_hitbox, 2)


        for hitbox in canguru_hitbox:
            if self.dingo_hitbox.colliderect(hitbox) and ((canguru.baixo and self.baixo) or (canguru.cima and self.cima)):
                #print("COLIDIU COM O Dingo!")
                if canguru.contador_colisao == 0:
                    vidas_rosto.dano = True
                    vidas_numeros.dano = True
                    canguru.contador_colisao = 1
            if self.dingo_corrida_hitbox.colliderect(hitbox):
                self.ataque = True
                self.correndo = True


        if bumerangue is not None:  # Se o bumerangue existe
            bumerangue_hitbox = bumerangue.Colisao() or []  # Se Colisao() retornar None, usa lista vazia

            for hitbox in bumerangue_hitbox:
                if (self.dingo_hitbox.colliderect(hitbox) and
                        ((bumerangue.baixo and self.baixo) or (bumerangue.cima and self.cima))):
                    #print("bumerangue acertou")
                    self.ataque = True
                    self.correndo = True
                    bumerangue.indo = False
                    bumerangue.voltando = True

    def update(self):
        self.Sprites()
        if self.spawn:
            self.spawn_on = False
            self.Dificuldade()
            self.Animacao()
            if self.y == 300:
                self.baixo = True
                self.cima = False

            if self.y == 268:
                self.cima = True
                self.baixo = False

            grupos = self.groups()
            if grupos:
                grupo = grupos[0]
                grupo.change_layer(self, self.get_layer())

            for i in self.andando:
                self.image = pygame.transform.scale(self.image, (1200/8,1200/8))
                self.rect = self.image.get_rect()  #image ja foi deifinido pela lista de lagartos, ele ja existe independentre
                self.rect.topright = i[0], i[1]  # Posiciona o rect conforme a posição da nuvem
                tela.blit(self.image, self.rect)
            self.Colisao()
class Dingo2 (pygame.sprite.Sprite):
    def __init__(self,bumerangue,canguru):
        pygame.sprite.Sprite.__init__(self)

        self.bumerangue = bumerangue
        self.canguru = canguru
        self.andando = [] #para gerenciar x e y
        self.spawn = False
        self.spawn_on = True
        self.correndo = True
        self.ataque = False
        self.baixo = False
        self.cima = False
        self.velocidade = 5
        self.contador_dingo = 0

        self.y = choice([268, 300])
        if self.y != dingo.y:
            self.x = randint(1100,1250)
        else:
            self.x = 1350
        self.andando.append([self.x, self.y])

    def get_layer(self):
        # Define a camada de desenho com base no Y
        return 7.1 if self.y == 300 else 6

    def Sprites(self):
        if self.y == 300:
            self.baixo = True
            self.cima = False
        else:
            self.baixo = False
            self.cima = True

        self.dingos = []
        self.dingos.append(carroca_dingo.subsurface((0*1200,0), (1200,1200)))
        self.dingos.append(carroca_dingo.subsurface((1*1200,0), (1200,1200)))

        self.atacando_1 = []
        self.atacando_1.append(carroca_dingo.subsurface((2*1200,0), (1200,1200)))
        self.atacando_1.append(carroca_dingo.subsurface((3*1200,0), (1200,1200)))

        self.atacando_2 = []
        self.atacando_2.append(carroca_dingo.subsurface((4 * 1200, 0), (1200, 1200)))
        self.atacando_2.append(carroca_dingo.subsurface((5 * 1200, 0), (1200, 1200)))

        self.image = self.dingos[0]
        self.image = pygame.transform.scale(self.image, (1200 / 8, 1200 / 8))
        self.rect = self.image.get_rect()
        self.rect.center = -200, -200

    def Dificuldade(self):
        if leveis.lvl_0:
            if self.correndo and not self.ataque:
                self.velocidade_animacao = 0.10
                self.velocidade = 5
            elif self.ataque:
                self.velocidade_animacao = 0.05
                self.velocidade += 0.2
        if leveis.lvl_1:
            if self.correndo and not self.ataque:
                self.velocidade_animacao = 0.10
                self.velocidade = 6
            elif self.ataque:
                self.velocidade_animacao = 0.06
                self.velocidade += 0.2
        if leveis.lvl_2:
            if self.correndo and not self.ataque:
                self.velocidade_animacao = 0.12
                self.velocidade = 8
            elif self.ataque:
                self.velocidade_animacao = 0.07
                self.velocidade += 0.2
        if leveis.lvl_3:
            if self.correndo and not self.ataque:
                self.velocidade_animacao = 0.13
                self.velocidade = 9
            elif self.ataque:
                self.velocidade_animacao = 0.08
                self.velocidade += 0.3
        if leveis.lvl_4:
            if self.correndo and not self.ataque:
                self.velocidade_animacao = 0.14
                self.velocidade = 10
            elif self.ataque:
                self.velocidade_animacao = 0.09
                self.velocidade += 0.3
        if leveis.lvl_5:
            if self.correndo and not self.ataque:
                self.velocidade_animacao = 0.15
                self.velocidade = 10
            elif self.ataque:
                self.velocidade_animacao = 0.1
                self.velocidade += 0.3

    def Animacao(self):

        if self.correndo:
            if self.contador_dingo >= len(self.dingos):
                self.contador_dingo = 0
            self.image = self.dingos[int(self.contador_dingo)]
            self.contador_dingo += self.velocidade_animacao

        if self.ataque:
            if self.contador_dingo >= len(self.atacando_1):
                self.contador_dingo = 0
            self.image = self.atacando_1[int(self.contador_dingo)]
            self.contador_dingo += self.velocidade_animacao

        for i in self.andando:
            i[0] -= self.velocidade
            if i[0] <= -200 and not canguru.morreu:
                # REMOVE A POSIÇÃO ANTIGA E CRIA UMA NOVA
                self.andando.remove(i)
                self.y = choice([268, 300])
                if self.y != dingo.y:
                    self.x = randint(1100, 1250)
                else:
                    self.x = 1200
                self.andando.append([self.x, self.y])  # Nova posição



                # RESETA ANIMAÇÃO E ESTADOS
                self.contador_dingo = 0
                self.ataque = False
                self.correndo = True
                self.spawn = False
                self.velocidade = 5
                self.spawn_on = True

                # ATUALIZA CAMADA (layer)
                grupos = self.groups()
                if grupos:
                    grupo = grupos[0]
                    grupo.change_layer(self, self.get_layer())

    def Colisao(self):
        self.dingo_hitbox = pygame.Rect(self.rect.x + 20, self.rect.y + 35, 100, 120)
        pygame.draw.rect(tela, (0, 0, 250), self.dingo_hitbox, 2)
        canguru_hitbox = canguru.Colisao()

        self.dingo_corrida_hitbox = pygame.Rect(self.rect.x - 300, self.rect.y + 50, 350, 100)
        #pygame.draw.rect(tela, (0, 0, 0), self.dingo_corrida_hitbox, 2)

        for hitbox in canguru_hitbox:
            if self.dingo_hitbox.colliderect(hitbox) and (
                    (canguru.baixo and self.baixo) or (canguru.cima and self.cima)):
                #print("COLIDIU COM O Dingo!")
                if canguru.contador_colisao == 0:
                    vidas_rosto.dano = True
                    vidas_numeros.dano = True
                    canguru.contador_colisao = 1
            if self.dingo_corrida_hitbox.colliderect(hitbox):
                self.ataque = True
                self.correndo = True

        if bumerangue is not None:  # Se o bumerangue existe
            bumerangue_hitbox = bumerangue.Colisao() or []  # Se Colisao() retornar None, usa lista vazia

            for hitbox in bumerangue_hitbox:
                if (self.dingo_hitbox.colliderect(hitbox) and
                        ((bumerangue.baixo and self.baixo) or (bumerangue.cima and self.cima))):
                   #print("bumerangue acertou")
                    self.ataque = True
                    self.correndo = True
                    bumerangue.indo = False
                    bumerangue.voltando = True

    def update(self):
        self.Sprites()
        if self.spawn:
            self.spawn_on = False
            self.Dificuldade()
            self.Animacao()
            if self.y == 300:
                self.baixo = True
                self.cima = False

            if self.y == 268:
                self.cima = True
                self.baixo = False

            grupos = self.groups()
            if grupos:
                grupo = grupos[0]
                grupo.change_layer(self, self.get_layer())

            for i in self.andando:
                self.image = pygame.transform.scale(self.image, (1200 / 8, 1200 / 8))
                self.rect = self.image.get_rect()  # image ja foi deifinido pela lista de lagartos, ele ja existe independentre
                self.rect.topright = i[0], i[1]  # Posiciona o rect conforme a posição da nuvem
                tela.blit(self.image, self.rect)
            self.Colisao()
class Dingo3 (pygame.sprite.Sprite):
    def __init__(self,bumerangue,canguru):
        pygame.sprite.Sprite.__init__(self)

        self.bumerangue = bumerangue
        self.canguru = canguru
        self.andando = [] #para gerenciar x e y
        self.spawn = False
        self.spawn_on = True
        self.correndo = True
        self.ataque = False
        self.baixo = False
        self.cima = False
        self.velocidade = 5
        self.contador_dingo = 0

        self.y = choice([268, 300])
        if self.y != dingo2.y:
            self.x = randint (1350,1400)
        else:
            self.x = 1350
        self.andando.append([self.x, self.y])

    def get_layer(self):
        # Define a camada de desenho com base no Y
        return 7.1 if self.y == 300 else 6

    def Sprites(self):

        self.dingos = []
        self.dingos.append(carroca_dingo.subsurface((0*1200,0), (1200,1200)))
        self.dingos.append(carroca_dingo.subsurface((1*1200,0), (1200,1200)))

        self.atacando_1 = []
        self.atacando_1.append(carroca_dingo.subsurface((2*1200,0), (1200,1200)))
        self.atacando_1.append(carroca_dingo.subsurface((3*1200,0), (1200,1200)))

        self.atacando_2 = []
        self.atacando_2.append(carroca_dingo.subsurface((4 * 1200, 0), (1200, 1200)))
        self.atacando_2.append(carroca_dingo.subsurface((5 * 1200, 0), (1200, 1200)))

        self.image = self.dingos[0]
        self.image = pygame.transform.scale(self.image, (1200 / 8, 1200 / 8))
        self.rect = self.image.get_rect()
        self.rect.center = -200, -200

    def Dificuldade(self):
        if leveis.lvl_0:
            if self.correndo and not self.ataque:
                self.velocidade_animacao = 0.10
                self.velocidade = 5
            elif self.ataque:
                self.velocidade_animacao = 0.05
                self.velocidade += 0.2
        if leveis.lvl_1:
            if self.correndo and not self.ataque:
                self.velocidade_animacao = 0.10
                self.velocidade = 6
            elif self.ataque:
                self.velocidade_animacao = 0.06
                self.velocidade += 0.2
        if leveis.lvl_2:
            if self.correndo and not self.ataque:
                self.velocidade_animacao = 0.12
                self.velocidade = 8
            elif self.ataque:
                self.velocidade_animacao = 0.07
                self.velocidade += 0.2
        if leveis.lvl_3:
            if self.correndo and not self.ataque:
                self.velocidade_animacao = 0.13
                self.velocidade = 9
            elif self.ataque:
                self.velocidade_animacao = 0.08
                self.velocidade += 0.3
        if leveis.lvl_4:
            if self.correndo and not self.ataque:
                self.velocidade_animacao = 0.14
                self.velocidade = 10
            elif self.ataque:
                self.velocidade_animacao = 0.09
                self.velocidade += 0.3
        if leveis.lvl_5:
            if self.correndo and not self.ataque:
                self.velocidade_animacao = 0.15
                self.velocidade = 10
            elif self.ataque:
                self.velocidade_animacao = 0.1
                self.velocidade += 0.3

    def Animacao(self):

        if self.correndo:
            if self.contador_dingo >= len(self.dingos):
                self.contador_dingo = 0
            self.image = self.dingos[int(self.contador_dingo)]
            self.contador_dingo += self.velocidade_animacao

        if self.ataque:
            if self.contador_dingo >= len(self.atacando_1):
                self.contador_dingo = 0
            self.image = self.atacando_1[int(self.contador_dingo)]
            self.contador_dingo += self.velocidade_animacao

        for i in self.andando:
            i[0] -= self.velocidade
            if i[0] <= -200 and not canguru.morreu:
                # REMOVE A POSIÇÃO ANTIGA E CRIA UMA NOVA
                self.andando.remove(i)
                self.y = choice([268, 300])
                if self.y != dingo2.y:
                    self.x = randint (1350,1400)
                else:
                    self.x = 1350
                self.andando.append([self.x, self.y])  # Nova posição


                # RESETA ANIMAÇÃO E ESTADOS
                self.contador_dingo = 0
                self.ataque = False
                self.correndo = True
                self.spawn = False
                self.velocidade = 5
                self.spawn_on = True

                # ATUALIZA CAMADA (layer)
                grupos = self.groups()
                if grupos:
                    grupo = grupos[0]
                    grupo.change_layer(self, self.get_layer())

    def Colisao(self):
        self.dingo_hitbox = pygame.Rect(self.rect.x + 20, self.rect.y + 35, 100, 120)
        pygame.draw.rect(tela, (0, 0, 250), self.dingo_hitbox, 2)
        canguru_hitbox = canguru.Colisao()

        self.dingo_corrida_hitbox = pygame.Rect(self.rect.x - 300, self.rect.y + 50, 350, 100)
        #pygame.draw.rect(tela, (0, 0, 0), self.dingo_corrida_hitbox, 2)

        for hitbox in canguru_hitbox:
            if self.dingo_hitbox.colliderect(hitbox) and (
                    (canguru.baixo and self.baixo) or (canguru.cima and self.cima)):
                #print("COLIDIU COM O Dingo!")
                if canguru.contador_colisao == 0:
                    vidas_rosto.dano = True
                    vidas_numeros.dano = True
                    canguru.contador_colisao = 1
            if self.dingo_corrida_hitbox.colliderect(hitbox):
                self.ataque = True
                self.correndo = True

        if bumerangue is not None:  # Se o bumerangue existe
            bumerangue_hitbox = bumerangue.Colisao() or []  # Se Colisao() retornar None, usa lista vazia

            for hitbox in bumerangue_hitbox:
                if (self.dingo_hitbox.colliderect(hitbox) and
                        ((bumerangue.baixo and self.baixo) or (bumerangue.cima and self.cima))):
                    #print("bumerangue acertou")
                    self.ataque = True
                    self.correndo = True
                    bumerangue.indo = False
                    bumerangue.voltando = True

    def update(self):
        self.Sprites()
        if self.spawn:
            self.spawn_on = False
            self.Dificuldade()
            self.Animacao()
            if self.y == 300:
                self.baixo = True
                self.cima = False

            if self.y == 268:
                self.cima = True
                self.baixo = False

            grupos = self.groups()
            if grupos:
                grupo = grupos[0]
                grupo.change_layer(self, self.get_layer())

            for i in self.andando:
                self.image = pygame.transform.scale(self.image, (1200 / 8, 1200 / 8))
                self.rect = self.image.get_rect()  # image ja foi deifinido pela lista de lagartos, ele ja existe independentre
                self.rect.topright = i[0], i[1]  # Posiciona o rect conforme a posição da nuvem
                tela.blit(self.image, self.rect)
            self.Colisao()
class Dingo4 (pygame.sprite.Sprite):
    def __init__(self,bumerangue,canguru):
        pygame.sprite.Sprite.__init__(self)

        self.bumerangue = bumerangue
        self.canguru = canguru
        self.andando = [] #para gerenciar x e y
        self.spawn = False
        self.spawn_on = True
        self.correndo = True
        self.ataque = False
        self.baixo = False
        self.cima = False
        self.velocidade = 5
        self.contador_dingo = 0

        self.y = choice([268, 300])
        if self.y != dingo3.y:
            self.x = randint(1400,1550)
        else:
            self.x = 1550
        self.andando.append([self.x, self.y])

    def get_layer(self):
        # Define a camada de desenho com base no Y
        return 7.1 if self.y == 300 else 6 #<<<baixo alto>>>

    def Sprites(self):

        self.dingos = []
        self.dingos.append(carroca_dingo.subsurface((0*1200,0), (1200,1200)))
        self.dingos.append(carroca_dingo.subsurface((1*1200,0), (1200,1200)))

        self.atacando_1 = []
        self.atacando_1.append(carroca_dingo.subsurface((2*1200,0), (1200,1200)))
        self.atacando_1.append(carroca_dingo.subsurface((3*1200,0), (1200,1200)))

        self.atacando_2 = []
        self.atacando_2.append(carroca_dingo.subsurface((4 * 1200, 0), (1200, 1200)))
        self.atacando_2.append(carroca_dingo.subsurface((5 * 1200, 0), (1200, 1200)))

        self.image = self.dingos[0]
        self.image = pygame.transform.scale(self.image, (1200 / 8, 1200 / 8))
        self.rect = self.image.get_rect()
        self.rect.center = -200, -200

    def Dificuldade(self):
        if leveis.lvl_0:
            if self.correndo and not self.ataque:
                self.velocidade_animacao = 0.10
                self.velocidade = 5
            elif self.ataque:
                self.velocidade_animacao = 0.05
                self.velocidade += 0.2
        if leveis.lvl_1:
            if self.correndo and not self.ataque:
                self.velocidade_animacao = 0.10
                self.velocidade = 6
            elif self.ataque:
                self.velocidade_animacao = 0.06
                self.velocidade += 0.2
        if leveis.lvl_2:
            if self.correndo and not self.ataque:
                self.velocidade_animacao = 0.12
                self.velocidade = 8
            elif self.ataque:
                self.velocidade_animacao = 0.07
                self.velocidade += 0.2
        if leveis.lvl_3:
            if self.correndo and not self.ataque:
                self.velocidade_animacao = 0.13
                self.velocidade = 9
            elif self.ataque:
                self.velocidade_animacao = 0.08
                self.velocidade += 0.3
        if leveis.lvl_4:
            if self.correndo and not self.ataque:
                self.velocidade_animacao = 0.14
                self.velocidade = 10
            elif self.ataque:
                self.velocidade_animacao = 0.09
                self.velocidade += 0.3
        if leveis.lvl_5:
            if self.correndo and not self.ataque:
                self.velocidade_animacao = 0.15
                self.velocidade = 10
            elif self.ataque:
                self.velocidade_animacao = 0.1
                self.velocidade += 0.3

    def Animacao(self):

        if self.correndo:
            if self.contador_dingo >= len(self.dingos):
                self.contador_dingo = 0
            self.image = self.dingos[int(self.contador_dingo)]
            self.contador_dingo += self.velocidade_animacao

        if self.ataque:
            if self.contador_dingo >= len(self.atacando_1):
                self.contador_dingo = 0
            self.image = self.atacando_1[int(self.contador_dingo)]
            self.contador_dingo += self.velocidade_animacao

        for i in self.andando:
            i[0] -= self.velocidade
            if i[0] <= -200 and not canguru.morreu:
                # REMOVE A POSIÇÃO ANTIGA E CRIA UMA NOVA
                self.andando.remove(i)
                self.y = choice([268, 300])
                if self.y != dingo3.y:
                    self.x = randint(1400, 1550)
                else:
                    self.x = 1550
                self.andando.append([self.x, self.y]) # Nova posição



                # RESETA ANIMAÇÃO E ESTADOS
                self.contador_dingo = 0
                self.ataque = False
                self.correndo = True
                self.spawn = False
                self.velocidade = 5
                self.spawn_on = True

                # ATUALIZA CAMADA (layer)
                grupos = self.groups()
                if grupos:
                    grupo = grupos[0]
                    grupo.change_layer(self, self.get_layer())

    def Colisao(self):
        self.dingo_hitbox = pygame.Rect(self.rect.x + 20, self.rect.y + 35, 100, 120)
        pygame.draw.rect(tela, (0, 0, 250), self.dingo_hitbox, 2)
        canguru_hitbox = canguru.Colisao()

        self.dingo_corrida_hitbox = pygame.Rect(self.rect.x - 300, self.rect.y + 50, 350, 100)
        #pygame.draw.rect(tela, (0, 0, 0), self.dingo_corrida_hitbox, 2)

        for hitbox in canguru_hitbox:
            if self.dingo_hitbox.colliderect(hitbox) and (
                    (canguru.baixo and self.baixo) or (canguru.cima and self.cima)):
                #print("COLIDIU COM O Dingo!")
                if canguru.contador_colisao == 0:
                    vidas_rosto.dano = True
                    vidas_numeros.dano = True
                    canguru.contador_colisao = 1
            if self.dingo_corrida_hitbox.colliderect(hitbox):
                self.ataque = True
                self.correndo = True

        if bumerangue is not None:  # Se o bumerangue existe
            bumerangue_hitbox = bumerangue.Colisao() or []  # Se Colisao() retornar None, usa lista vazia

            for hitbox in bumerangue_hitbox:
                if (self.dingo_hitbox.colliderect(hitbox) and
                        ((bumerangue.baixo and self.baixo) or (bumerangue.cima and self.cima))):
                    #print("bumerangue acertou")
                    self.ataque = True
                    self.correndo = True
                    bumerangue.indo = False
                    bumerangue.voltando = True

    def update(self):
        self.Sprites()
        if self.spawn:
            self.spawn_on = False
            self.Dificuldade()
            self.Animacao()
            if self.y == 300:
                self.baixo = True
                self.cima = False

            if self.y == 268:
                self.cima = True
                self.baixo = False

            grupos = self.groups()
            if grupos:
                grupo = grupos[0]
                grupo.change_layer(self, self.get_layer())

            for i in self.andando:
                self.image = pygame.transform.scale(self.image, (1200 / 8, 1200 / 8))
                self.rect = self.image.get_rect()  # image ja foi deifinido pela lista de lagartos, ele ja existe independentre
                self.rect.topright = i[0], i[1]  # Posiciona o rect conforme a posição da nuvem
                tela.blit(self.image, self.rect)
            self.Colisao()
class Dingo5 (pygame.sprite.Sprite):
    def __init__(self,bumerangue,canguru):
        pygame.sprite.Sprite.__init__(self)

        self.bumerangue = bumerangue
        self.canguru = canguru
        self.andando = [] #para gerenciar x e y
        self.spawn = False
        self.spawn_on = True
        self.correndo = True
        self.ataque = False
        self.baixo = False
        self.cima = False
        self.velocidade = 5
        self.contador_dingo = 0

        self.y = choice([268, 300])
        if self.y != dingo4.y:
            self.x = randint(1600,1750)
        else:
            self.x = 1650
        self.andando.append([self.x, self.y])

    def get_layer(self):
        # Define a camada de desenho com base no Y
        return 7.1 if self.y == 300 else 6 #<<<<baixo  #alto>>>

    def Sprites(self):

        self.dingos = []
        self.dingos.append(carroca_dingo.subsurface((0*1200,0), (1200,1200)))
        self.dingos.append(carroca_dingo.subsurface((1*1200,0), (1200,1200)))

        self.atacando_1 = []
        self.atacando_1.append(carroca_dingo.subsurface((2*1200,0), (1200,1200)))
        self.atacando_1.append(carroca_dingo.subsurface((3*1200,0), (1200,1200)))

        self.atacando_2 = []
        self.atacando_2.append(carroca_dingo.subsurface((4 * 1200, 0), (1200, 1200)))
        self.atacando_2.append(carroca_dingo.subsurface((5 * 1200, 0), (1200, 1200)))

        self.image = self.dingos[0]
        self.image = pygame.transform.scale(self.image, (1200 / 8, 1200 / 8))
        self.rect = self.image.get_rect()
        self.rect.center = -200, -200

    def Dificuldade(self):
        if leveis.lvl_0:
            if self.correndo and not self.ataque:
                self.velocidade_animacao = 0.10
                self.velocidade = 5
            elif self.ataque:
                self.velocidade_animacao = 0.05
                self.velocidade += 0.2
        if leveis.lvl_1:
            if self.correndo and not self.ataque:
                self.velocidade_animacao = 0.10
                self.velocidade = 6
            elif self.ataque:
                self.velocidade_animacao = 0.06
                self.velocidade += 0.2
        if leveis.lvl_2:
            if self.correndo and not self.ataque:
                self.velocidade_animacao = 0.12
                self.velocidade = 8
            elif self.ataque:
                self.velocidade_animacao = 0.07
                self.velocidade += 0.2
        if leveis.lvl_3:
            if self.correndo and not self.ataque:
                self.velocidade_animacao = 0.13
                self.velocidade = 9
            elif self.ataque:
                self.velocidade_animacao = 0.08
                self.velocidade += 0.3
        if leveis.lvl_4:
            if self.correndo and not self.ataque:
                self.velocidade_animacao = 0.14
                self.velocidade = 10
            elif self.ataque:
                self.velocidade_animacao = 0.09
                self.velocidade += 0.3
        if leveis.lvl_5:
            if self.correndo and not self.ataque:
                self.velocidade_animacao = 0.15
                self.velocidade = 10
            elif self.ataque:
                self.velocidade_animacao = 0.1
                self.velocidade += 0.3

    def Animacao(self):

        if self.correndo:
            if self.contador_dingo >= len(self.dingos):
                self.contador_dingo = 0
            self.image = self.dingos[int(self.contador_dingo)]
            self.contador_dingo += self.velocidade_animacao

        if self.ataque:
            if self.contador_dingo >= len(self.atacando_1):
                self.contador_dingo = 0
            self.image = self.atacando_1[int(self.contador_dingo)]
            self.contador_dingo += self.velocidade_animacao

        for i in self.andando:
            i[0] -= self.velocidade
            if i[0] <= -200 and not canguru.morreu:
                # REMOVE A POSIÇÃO ANTIGA E CRIA UMA NOVA
                self.andando.remove(i)
                self.y = choice([268, 300])
                if self.y != dingo4.y:
                    self.x = randint(1600, 1750)
                else:
                    self.x = 1650
                self.andando.append([self.x, self.y])

                # ATUALIZA cima/baixo DE FORMA SEGURA


                # RESETA ANIMAÇÃO E ESTADOS
                self.contador_dingo = 0
                self.ataque = False
                self.correndo = True
                self.spawn = False
                self.velocidade = 5
                self.spawn_on = True

                # ATUALIZA CAMADA (layer)
                grupos = self.groups()
                if grupos:
                    grupo = grupos[0]
                    grupo.change_layer(self, self.get_layer())

    def Colisao(self):
        self.dingo_hitbox = pygame.Rect(self.rect.x + 20, self.rect.y + 35, 100, 120)
        pygame.draw.rect(tela, (0, 0, 250), self.dingo_hitbox, 2)
        canguru_hitbox = canguru.Colisao()

        self.dingo_corrida_hitbox = pygame.Rect(self.rect.x - 300, self.rect.y + 50, 350, 100)
        #pygame.draw.rect(tela, (0, 0, 0), self.dingo_corrida_hitbox, 2)

        for hitbox in canguru_hitbox:
            if self.dingo_hitbox.colliderect(hitbox) and (
                    (canguru.baixo and self.baixo) or (canguru.cima and self.cima)):
                #print("COLIDIU COM O Dingo!")
                if canguru.contador_colisao == 0:
                    vidas_rosto.dano = True
                    vidas_numeros.dano = True
                    canguru.contador_colisao = 1
            if self.dingo_corrida_hitbox.colliderect(hitbox):
                self.ataque = True
                self.correndo = True

        if bumerangue is not None:  # Se o bumerangue existe
            bumerangue_hitbox = bumerangue.Colisao() or []  # Se Colisao() retornar None, usa lista vazia

            for hitbox in bumerangue_hitbox:
                if (self.dingo_hitbox.colliderect(hitbox) and
                        ((bumerangue.baixo and self.baixo) or (bumerangue.cima and self.cima))):
                    #print("bumerangue acertou")
                    self.ataque = True
                    self.correndo = True
                    bumerangue.indo = False
                    bumerangue.voltando = True

    def update(self):
        self.Sprites()
        if self.spawn:
            self.spawn_on = False
            self.Dificuldade()
            self.Animacao()
            if self.y == 300:
                self.baixo = True
                self.cima = False
            if self.y == 268:
                self.cima = True
                self.baixo = False

            grupos = self.groups()
            if grupos:
                grupo = grupos[0]
                grupo.change_layer(self, self.get_layer())

            for i in self.andando:
                self.image = pygame.transform.scale(self.image, (1200 / 8, 1200 / 8))
                self.rect = self.image.get_rect()  # image ja foi deifinido pela lista de lagartos, ele ja existe independentre
                self.rect.topright = i[0], i[1]  # Posiciona o rect conforme a posição da nuvem
                tela.blit(self.image, self.rect)
            self.Colisao()
class Dingo6 (pygame.sprite.Sprite):
    def __init__(self,bumerangue,canguru):
        pygame.sprite.Sprite.__init__(self)

        self.bumerangue = bumerangue
        self.canguru = canguru
        self.andando = [] #para gerenciar x e y
        self.spawn = False
        self.spawn_on = True
        self.correndo = True
        self.ataque = False
        self.baixo = False
        self.cima = False
        self.velocidade = 5
        self.contador_dingo = 0

        self.y = choice([268, 300])
        if self.y != dingo5.y:
            self.x = randint(1800,1900)
        else:
            self.x = 1850
        self.andando.append([self.x, self.y])

    def get_layer(self):
        # Define a camada de desenho com base no Y
        return 7.1 if self.y == 300 else 6

    def Sprites(self):

        self.dingos = []
        self.dingos.append(carroca_dingo.subsurface((0*1200,0), (1200,1200)))
        self.dingos.append(carroca_dingo.subsurface((1*1200,0), (1200,1200)))

        self.atacando_1 = []
        self.atacando_1.append(carroca_dingo.subsurface((2*1200,0), (1200,1200)))
        self.atacando_1.append(carroca_dingo.subsurface((3*1200,0), (1200,1200)))

        self.atacando_2 = []
        self.atacando_2.append(carroca_dingo.subsurface((4 * 1200, 0), (1200, 1200)))
        self.atacando_2.append(carroca_dingo.subsurface((5 * 1200, 0), (1200, 1200)))

        self.image = self.dingos[0]
        self.image = pygame.transform.scale(self.image, (1200 / 8, 1200 / 8))
        self.rect = self.image.get_rect()
        self.rect.center = -200, -200

    def Dificuldade(self):
        if leveis.lvl_0:
            if self.correndo and not self.ataque:
                self.velocidade_animacao = 0.10
                self.velocidade = 5
            elif self.ataque:
                self.velocidade_animacao = 0.05
                self.velocidade += 0.2
        if leveis.lvl_1:
            if self.correndo and not self.ataque:
                self.velocidade_animacao = 0.10
                self.velocidade = 6
            elif self.ataque:
                self.velocidade_animacao = 0.06
                self.velocidade += 0.2
        if leveis.lvl_2:
            if self.correndo and not self.ataque:
                self.velocidade_animacao = 0.12
                self.velocidade = 8
            elif self.ataque:
                self.velocidade_animacao = 0.07
                self.velocidade += 0.2
        if leveis.lvl_3:
            if self.correndo and not self.ataque:
                self.velocidade_animacao = 0.13
                self.velocidade = 9
            elif self.ataque:
                self.velocidade_animacao = 0.08
                self.velocidade += 0.3
        if leveis.lvl_4:
            if self.correndo and not self.ataque:
                self.velocidade_animacao = 0.14
                self.velocidade = 10
            elif self.ataque:
                self.velocidade_animacao = 0.09
                self.velocidade += 0.3
        if leveis.lvl_5:
            if self.correndo and not self.ataque:
                self.velocidade_animacao = 0.15
                self.velocidade = 10
            elif self.ataque:
                self.velocidade_animacao = 0.1
                self.velocidade += 0.3

    def Animacao(self):

        if self.correndo:
            if self.contador_dingo >= len(self.dingos):
                self.contador_dingo = 0
            self.image = self.dingos[int(self.contador_dingo)]
            self.contador_dingo += self.velocidade_animacao

        if self.ataque:
            if self.contador_dingo >= len(self.atacando_1):
                self.contador_dingo = 0
            self.image = self.atacando_1[int(self.contador_dingo)]
            self.contador_dingo += self.velocidade_animacao

        for i in self.andando:
            i[0] -= self.velocidade
            if i[0] <= -200 and not canguru.morreu:
                # REMOVE A POSIÇÃO ANTIGA E CRIA UMA NOVA
                self.andando.remove(i)
                self.y = choice([268, 300])
                if self.y != dingo5.y:
                    self.x = randint(1800, 1900)
                else:
                    self.x = 1850
                self.andando.append([self.x, self.y])  # Nova posição


                # RESETA ANIMAÇÃO E ESTADOS
                self.contador_dingo = 0
                self.ataque = False
                self.correndo = True
                self.spawn = False
                self.velocidade = 5
                self.spawn_on = True

                # ATUALIZA CAMADA (layer)
                grupos = self.groups()
                if grupos:
                    grupo = grupos[0]
                    grupo.change_layer(self, self.get_layer())

    def Colisao(self):
        self.dingo_hitbox = pygame.Rect(self.rect.x + 20, self.rect.y + 35, 100, 120)
        pygame.draw.rect(tela, (0, 0, 250), self.dingo_hitbox, 2)
        canguru_hitbox = canguru.Colisao()

        self.dingo_corrida_hitbox = pygame.Rect(self.rect.x - 300, self.rect.y + 50, 350, 100)
        #pygame.draw.rect(tela, (0, 0, 0), self.dingo_corrida_hitbox, 2)

        for hitbox in canguru_hitbox:
            if self.dingo_hitbox.colliderect(hitbox) and (
                    (canguru.baixo and self.baixo) or (canguru.cima and self.cima)):
                #print("COLIDIU COM O Dingo!")
                if canguru.contador_colisao == 0:
                    vidas_rosto.dano = True
                    vidas_numeros.dano = True
                    canguru.contador_colisao = 1
            if self.dingo_corrida_hitbox.colliderect(hitbox):
                self.ataque = True
                self.correndo = True

        if bumerangue is not None:  # Se o bumerangue existe
            bumerangue_hitbox = bumerangue.Colisao() or []  # Se Colisao() retornar None, usa lista vazia

            for hitbox in bumerangue_hitbox:
                if (self.dingo_hitbox.colliderect(hitbox) and
                        ((bumerangue.baixo and self.baixo) or (bumerangue.cima and self.cima))):
                    #print("bumerangue acertou")
                    self.ataque = True
                    self.correndo = True
                    bumerangue.indo = False
                    bumerangue.voltando = True

    def update(self):
        self.Sprites()
        if self.spawn:
            self.spawn_on = False
            self.Dificuldade()
            self.Animacao()

            if self.y == 300:
                self.baixo = True
                self.cima = False
            if self.y == 268:
                self.cima = True
                self.baixo = False

            grupos = self.groups()
            if grupos:
                grupo = grupos[0]
                grupo.change_layer(self, self.get_layer())

            for i in self.andando:
                self.image = pygame.transform.scale(self.image, (1200 / 8, 1200 / 8))
                self.rect = self.image.get_rect()  # image ja foi deifinido pela lista de lagartos, ele ja existe independentre
                self.rect.topright = i[0], i[1]  # Posiciona o rect conforme a posição da nuvem
                tela.blit(self.image, self.rect)
            self.Colisao() #aumentar distancia dos ultimos

class Lagarto(pygame.sprite.Sprite):
    def __init__(self,canguru,bumerangue):
        pygame.sprite.Sprite.__init__(self)

        self.canguru = canguru
        self.bumerangue = bumerangue
        self.x = 900
        self.y = choice ([240,272])
        self.estado_anterior = "parado"

        self.contador_bumerangue = 0
        self.contador_lagarto = 0
        self.contado_ataque = 0
        self.spawn = False
        self.spawn_on = True
        self.kill = False
        self.baixo = False
        self.cima = False
        self.ataque = False
        self.parado = True
        self.andando = [] #para gerenciar x e y
        self.andando.append([self.x, self.y])

    def Sprites(self):

        self.lagartos = []

        if self.parado and not self.kill:
            for i in (0,1):
                imagem_lagarto = carroca_lagarto.subsurface((i * 397, 0), (397, 362))
                imagem_lagarto = pygame.transform.scale(imagem_lagarto, (397 / 2, 362 /2))
                self.lagartos.append(imagem_lagarto)

        elif self.ataque and not self.kill:
            for i in [2,3,4]:
                ataque_lagarto = carroca_lagarto.subsurface((i*397,0), (397,362))
                ataque_lagarto = pygame.transform.scale(ataque_lagarto, (397 / 2, 362 /2))
                self.lagartos.append(ataque_lagarto)

        elif self.kill:
            for i in [0,1,2,3]:
                morte_lagarto = carroca_morte1.subsurface((i*400,0), (400,400))
                morte_lagarto = pygame.transform.scale(morte_lagarto, (400/2,400/2))
                self.lagartos.append(morte_lagarto)

        self.image = self.lagartos[0]
        self.rect = self.image.get_rect()
        self.rect.center = -200, -200

    def Dificuldade(self):

        if leveis.lvl_0:
            if self.ataque:
                self.velocidade_animacao = 0.15
            elif self.kill:
                self.velocidade_animacao = 0.15
            else:
                self.velocidade_animacao = 0.10
            self.velocidade = 5
        if leveis.lvl_1:
            if self.ataque:
                self.velocidade_animacao = 0.17
            elif self.kill:
                self.velocidade_animacao = 0.15
            else:
                self.velocidade_animacao = 0.11
            self.velocidade = 6
        if leveis.lvl_2:
            if self.ataque:
                self.velocidade_animacao = 0.19
            elif self.kill:
                self.velocidade_animacao = 0.15
            else:
                self.velocidade_animacao = 0.12
            self.velocidade = 7
        if leveis.lvl_3:
            if self.ataque:
                self.velocidade_animacao = 0.21
            elif self.kill:
                self.velocidade_animacao = 0.15
            else:
                self.velocidade_animacao = 0.13
            self.velocidade = 8
        if leveis.lvl_4:
            if self.ataque:
                self.velocidade_animacao = 0.23
            elif self.kill:
                self.velocidade_animacao = 0.15
            else:
                self.velocidade_animacao = 0.14
            self.velocidade = 9
        if leveis.lvl_5:
            if self.ataque:
                self.velocidade_animacao = 0.25
            elif self.kill:
                self.velocidade_animacao = 0.15
            else:
                self.velocidade_animacao = 0.15
            self.velocidade = 10

    def Animacao(self):

        if self.kill:
            estado_atual = "kill"
        elif self.ataque:
            estado_atual = "ataque"
        else:
            estado_atual = "parado"

        if estado_atual != self.estado_anterior:
            self.contador_lagarto = 0
            self.estado_anterior = estado_atual

        if self.contador_lagarto >= len(self.lagartos) and not self.kill:
            self.contador_lagarto = 0

        if not self.kill:
            self.image = self.lagartos[int(self.contador_lagarto)]
            self.contador_lagarto += self.velocidade_animacao

        elif self.kill:
            if self.contador_lagarto >= len(self.lagartos):
                self.contador_lagarto = 3
        if self.kill:
            if self.contador_lagarto <= 4:
                self.image = self.lagartos[int(self.contador_lagarto)]
                self.contador_lagarto += self.velocidade_animacao


        for i in self.andando:

            i[0] -= self.velocidade
            if i[0] < -10 and not canguru.morreu:
                self.andando.remove(i)
                self.contador_lagarto = 0  # RESET DO CONTADOR
                self.ataque = False  # VOLTA AO ESTADO INICIAL
                self.parado = True
                self.kill = False
                self.spawn = False
                self.spawn_on = True
                self.y = choice([240, 272])
                self.andando.append([self.x, self.y])
                grupos = self.groups()
                if grupos:
                    grupo = grupos[0]
                    grupo.change_layer(self, self.get_layer())
            if (not canguru.morreu and
                    100 <= i[0] - self.canguru.rect.x <= 320 and
                    not self.kill and
                    ((canguru.cima and self.cima) or (canguru.baixo and self.baixo))):
                self.ataque = True
                self.parado = False

                if self.canguru.rect.y <=120 and not self.kill :
                    self.contador_lagarto = 0

            else:
                self.ataque = False
                self.parado = True
    def get_layer(self):
        # Define a camada de desenho com base no Y
        return 6.5 if self.y == 272 else 6 #baixo<<< alto >>>

    def Colisao(self):
        if not self.kill:
            canguru_hitbox = canguru.Colisao()

            self.lagarto_hitbox_corpo = pygame.Rect(self.rect.x + 120, self.rect.y + 95, 50, 80)
            #pygame.draw.rect(tela, (0, 0, 0), self.lagarto_hitbox_corpo, 2)
            self.lagarto_hitbox_cabeca = pygame.Rect(self.rect.x + 110, self.rect.y + 75, 50, 30)
            #pygame.draw.rect(tela, (0, 0, 0), self.lagarto_hitbox_cabeca, 2)
            self.lagarto_ataque_hitbox = pygame.Rect(0, 0, 0, 0)

            if self.ataque == True:
                if self.contador_lagarto >2:
                    self.lagarto_ataque_hitbox = pygame.Rect(self.rect.x + 20, self.rect.y + 50, 40, 120)
                    #pygame.draw.rect(tela, (250, 150, 100), self.lagarto_ataque_hitbox, 2)
                elif self.contador_lagarto >1 and self.contador_lagarto <2:
                    self.lagarto_ataque_hitbox = pygame.Rect(self.rect.x + 70, self.rect.y -10, 40, 70)
                    #pygame.draw.rect(tela, (250, 150, 100), self.lagarto_ataque_hitbox, 2)
                elif self.contador_lagarto >0 and self.contador_lagarto <1:
                    self.lagarto_ataque_hitbox = pygame.Rect(self.rect.x + 70, self.rect.y + 95, 50, 50)
                    #pygame.draw.rect(tela, (250, 150, 100), self.lagarto_ataque_hitbox, 2)
            else:
                self.lagarto_hitbox_arma = pygame.Rect(self.rect.x + 70, self.rect.y + 95, 50, 50)
                #pygame.draw.rect(tela, (50, 150, 200), self.lagarto_hitbox_arma, 2)

           #Colisao canguru
            for hitbox in canguru_hitbox:
                if self.ataque:
                    if ((self.lagarto_hitbox_corpo.colliderect(hitbox) or self.lagarto_hitbox_cabeca.colliderect(hitbox)
                             or self.lagarto_ataque_hitbox.colliderect(hitbox)) and ((canguru.cima and self.cima)
                            or (canguru.baixo and self.baixo))):
                        #print("COLIDIU COM O lagarto!")
                        if canguru.contador_colisao == 0:
                            vidas_rosto.dano = True
                            vidas_numeros.dano = True
                            canguru.contador_colisao = 1
                else:
                    if ((self.lagarto_hitbox_corpo.colliderect(hitbox) or self.lagarto_hitbox_cabeca.colliderect(hitbox))
                            and ((canguru.cima and self.cima) or (canguru.baixo and self.baixo))):
                        #print("COLIDIU COM O lagarto!")
                        if canguru.contador_colisao == 0:
                            vidas_rosto.dano = True
                            vidas_numeros.dano = True
                            canguru.contador_colisao = 1
                    #colisao bumerangue
            if bumerangue is not None:  # Se o bumerangue existe
                bumerangue_hitbox = bumerangue.Colisao() or []  # Se Colisao() retornar None, usa lista vazia
                for hitbox in bumerangue_hitbox:
                    if self.cima and (self.lagarto_hitbox_corpo.colliderect(hitbox)
                                      or self.lagarto_hitbox_cabeca.colliderect(hitbox)):
                        #print("bumerangue acertou")
                        bumerangue.indo = False
                        bumerangue.voltando = True
                        bumerangue.acertou = True
                        self.kill = True

    def update(self):
        self.Sprites()
        if self.spawn:
            self.spawn_on = False
            self.Dificuldade()
            self.Animacao()

            if self.y == 272:
                self.baixo = True
                self.cima = False

            if self.y == 240:
                self.cima = True
                self.baixo = False

            grupos = self.groups()
            if grupos:
                grupo = grupos[0].change_layer(self, self.get_layer()) #forma de fazer em 1 linha só
            for i in self.andando:
                self.rect = self.image.get_rect()  #image ja foi deifinido pela lista de lagartos, ele ja existe independentre
                self.rect.topright = i[0], i[1]  # Posiciona o rect conforme a posição da nuvem
                tela.blit(self.image, self.rect)

            self.Colisao()
class Lagarto2(pygame.sprite.Sprite):
    def __init__(self,canguru,bumerangue):
        pygame.sprite.Sprite.__init__(self)

        self.canguru = canguru
        self.bumerangue = bumerangue
        self.x = 1250
        self.y = choice ([240,272])
        self.estado_anterior = "parado"

        self.contador_bumerangue = 0
        self.contador_lagarto = 0
        self.contado_ataque = 0
        self.spawn = False
        self.spawn_on = True
        self.kill = False
        self.baixo = False
        self.cima = False
        self.ataque = False
        self.parado = True
        self.andando = [] #para gerenciar x e y
        self.andando.append([self.x, self.y])

    def get_layer(self):
        # Define a camada de desenho com base no Y
        return 6.5 if self.y == 272 else 6 #8 / 6.5

    def Sprites(self):

        self.lagartos = []

        if self.parado and not self.kill:
            for i in (0,1):
                imagem_lagarto = carroca_lagarto.subsurface((i * 397, 0), (397, 362))
                imagem_lagarto = pygame.transform.scale(imagem_lagarto, (397 / 2, 362 /2))
                self.lagartos.append(imagem_lagarto)

        elif self.ataque and not self.kill:
            for i in [2,3,4]:
                ataque_lagarto = carroca_lagarto.subsurface((i*397,0), (397,362))
                ataque_lagarto = pygame.transform.scale(ataque_lagarto, (397 / 2, 362 /2))
                self.lagartos.append(ataque_lagarto)

        elif self.kill:
            for i in [0,1,2,3]:
                morte_lagarto = carroca_morte1.subsurface((i*400,0), (400,400))
                morte_lagarto = pygame.transform.scale(morte_lagarto, (400/2,400/2))
                self.lagartos.append(morte_lagarto)

        self.image = self.lagartos[0]
        self.rect = self.image.get_rect()
        self.rect.center = -200, -200

    def Dificuldade(self):

        if leveis.lvl_0:
            if self.ataque:
                self.velocidade_animacao = 0.15
            elif self.kill:
                self.velocidade_animacao = 0.15
            else:
                self.velocidade_animacao = 0.10
            self.velocidade = 5
        if leveis.lvl_1:
            if self.ataque:
                self.velocidade_animacao = 0.17
            elif self.kill:
                self.velocidade_animacao = 0.15
            else:
                self.velocidade_animacao = 0.11
            self.velocidade = 6
        if leveis.lvl_2:
            if self.ataque:
                self.velocidade_animacao = 0.19
            elif self.kill:
                self.velocidade_animacao = 0.15
            else:
                self.velocidade_animacao = 0.12
            self.velocidade = 7
        if leveis.lvl_3:
            if self.ataque:
                self.velocidade_animacao = 0.21
            elif self.kill:
                self.velocidade_animacao = 0.15
            else:
                self.velocidade_animacao = 0.13
            self.velocidade = 8
        if leveis.lvl_4:
            if self.ataque:
                self.velocidade_animacao = 0.23
            elif self.kill:
                self.velocidade_animacao = 0.15
            else:
                self.velocidade_animacao = 0.14
            self.velocidade = 9
        if leveis.lvl_5:
            if self.ataque:
                self.velocidade_animacao = 0.25
            elif self.kill:
                self.velocidade_animacao = 0.15
            else:
                self.velocidade_animacao = 0.15
            self.velocidade = 10

    def Animacao(self):

        if self.kill:
            estado_atual = "kill"
        elif self.ataque:
            estado_atual = "ataque"
        else:
            estado_atual = "parado"

        if estado_atual != self.estado_anterior:
            self.contador_lagarto = 0
            self.estado_anterior = estado_atual

        if self.contador_lagarto >= len(self.lagartos) and not self.kill:
            self.contador_lagarto = 0

        if not self.kill:
            self.image = self.lagartos[int(self.contador_lagarto)]
            self.contador_lagarto += self.velocidade_animacao

        elif self.kill:
            if self.contador_lagarto >= len(self.lagartos):
                self.contador_lagarto = 3
        if self.kill:
            if self.contador_lagarto <= 4:
                self.image = self.lagartos[int(self.contador_lagarto)]
                self.contador_lagarto += self.velocidade_animacao


        for i in self.andando:

            i[0] -= self.velocidade
            if i[0] < -10 and not canguru.morreu:
                self.andando.remove(i)
                self.contador_lagarto = 0  # RESET DO CONTADOR
                self.ataque = False  # VOLTA AO ESTADO INICIAL
                self.parado = True
                self.kill = False
                self.spawn = False
                self.spawn_on = True
                self.x = 1250
                self.y = choice([240, 272])
                self.andando.append([self.x, self.y])
                grupos = self.groups()
                if grupos:
                    grupo = grupos[0]
                    grupo.change_layer(self, self.get_layer())
            if (not canguru.morreu and
                    100 <= i[0] - self.canguru.rect.x <= 320 and
                    not self.kill and
                    ((canguru.cima and self.cima) or (canguru.baixo and self.baixo))):
                self.ataque = True
                self.parado = False

                if self.canguru.rect.y <= 120 and not self.kill:
                    self.contador_lagarto = 0

            else:
                self.ataque = False
                self.parado = True

    def Colisao(self):
        if not self.kill:
            canguru_hitbox = canguru.Colisao()

            self.lagarto_hitbox_corpo = pygame.Rect(self.rect.x + 120, self.rect.y + 95, 50, 80)
            #pygame.draw.rect(tela, (0, 0, 0), self.lagarto_hitbox_corpo, 2)
            self.lagarto_hitbox_cabeca = pygame.Rect(self.rect.x + 110, self.rect.y + 75, 50, 30)
            #pygame.draw.rect(tela, (0, 0, 0), self.lagarto_hitbox_cabeca, 2)
            self.lagarto_ataque_hitbox = pygame.Rect(0, 0, 0, 0)

            if self.ataque == True:
                if self.contador_lagarto >2:
                    self.lagarto_ataque_hitbox = pygame.Rect(self.rect.x + 20, self.rect.y + 50, 40, 120)
                    #pygame.draw.rect(tela, (250, 150, 100), self.lagarto_ataque_hitbox, 2)
                elif self.contador_lagarto >1 and self.contador_lagarto <2:
                    self.lagarto_ataque_hitbox = pygame.Rect(self.rect.x + 70, self.rect.y -10, 40, 70)
                    #pygame.draw.rect(tela, (250, 150, 100), self.lagarto_ataque_hitbox, 2)
                elif self.contador_lagarto >0 and self.contador_lagarto <1:
                    self.lagarto_ataque_hitbox = pygame.Rect(self.rect.x + 70, self.rect.y + 95, 50, 50)
                    #pygame.draw.rect(tela, (250, 150, 100), self.lagarto_ataque_hitbox, 2)
            else:
                self.lagarto_hitbox_arma = pygame.Rect(self.rect.x + 70, self.rect.y + 95, 50, 50)
                #pygame.draw.rect(tela, (50, 150, 200), self.lagarto_hitbox_arma, 2)

           #Colisao canguru
            for hitbox in canguru_hitbox:
                if self.ataque:
                    if ((self.lagarto_hitbox_corpo.colliderect(hitbox) or self.lagarto_hitbox_cabeca.colliderect(hitbox)
                             or self.lagarto_ataque_hitbox.colliderect(hitbox)) and ((canguru.cima and self.cima)
                            or (canguru.baixo and self.baixo))):
                        #print("COLIDIU COM O lagarto!")
                        if canguru.contador_colisao == 0:
                            vidas_rosto.dano = True
                            vidas_numeros.dano = True
                            canguru.contador_colisao = 1
                else:
                    if ((self.lagarto_hitbox_corpo.colliderect(hitbox) or self.lagarto_hitbox_cabeca.colliderect(hitbox))
                            and ((canguru.cima and self.cima) or (canguru.baixo and self.baixo))):
                        #print("COLIDIU COM O lagarto!")
                        if canguru.contador_colisao == 0:
                            vidas_rosto.dano = True
                            vidas_numeros.dano = True
                            canguru.contador_colisao = 1
                    #colisao bumerangue
            if bumerangue is not None:  # Se o bumerangue existe
                bumerangue_hitbox = bumerangue.Colisao() or []  # Se Colisao() retornar None, usa lista vazia
                for hitbox in bumerangue_hitbox:
                    if self.cima and (self.lagarto_hitbox_corpo.colliderect(hitbox)
                                      or self.lagarto_hitbox_cabeca.colliderect(hitbox)):
                        #print("bumerangue acertou")
                        bumerangue.indo = False
                        bumerangue.voltando = True
                        bumerangue.acertou = True
                        self.kill = True


    def update(self):
        self.Sprites()
        if self.spawn:
            self.spawn_on = False
            self.Dificuldade()
            self.Animacao()

            if self.y == 272:
                self.baixo = True
                self.cima = False

            if self.y == 240:
                self.cima = True
                self.baixo = False

            grupos = self.groups()
            if grupos:
                grupo = grupos[0]
                grupo.change_layer(self, self.get_layer())

            for i in self.andando:
                self.rect = self.image.get_rect()  #image ja foi deifinido pela lista de lagartos, ele ja existe independentre
                self.rect.topright = i[0], i[1]  # Posiciona o rect conforme a posição da nuvem
                tela.blit(self.image, self.rect)

            self.Colisao()
class Lagarto3(pygame.sprite.Sprite):
    def __init__(self,canguru,bumerangue):
        pygame.sprite.Sprite.__init__(self)

        self.canguru = canguru
        self.bumerangue = bumerangue
        self.x = randint(1500,1500)
        self.y = choice ([240,272])
        self.estado_anterior = "parado"

        self.contador_bumerangue = 0
        self.contador_lagarto = 0
        self.contado_ataque = 0
        self.spawn = False
        self.spawn_on = True
        self.kill = False
        self.baixo = False
        self.cima = False
        self.ataque = False
        self.parado = True
        self.andando = [] #para gerenciar x e y
        self.andando.append([self.x, self.y])

    def get_layer(self):
        # Define a camada de desenho com base no Y
        return 6.5 if self.y == 272 else 6

    def Sprites(self):

        self.lagartos = []

        if self.parado and not self.kill:
            for i in (0,1):
                imagem_lagarto = carroca_lagarto.subsurface((i * 397, 0), (397, 362))
                imagem_lagarto = pygame.transform.scale(imagem_lagarto, (397 / 2, 362 /2))
                self.lagartos.append(imagem_lagarto)

        elif self.ataque and not self.kill:
            for i in [2,3,4]:
                ataque_lagarto = carroca_lagarto.subsurface((i*397,0), (397,362))
                ataque_lagarto = pygame.transform.scale(ataque_lagarto, (397 / 2, 362 /2))
                self.lagartos.append(ataque_lagarto)

        elif self.kill:
            for i in [0,1,2,3]:
                morte_lagarto = carroca_morte1.subsurface((i*400,0), (400,400))
                morte_lagarto = pygame.transform.scale(morte_lagarto, (400/2,400/2))
                self.lagartos.append(morte_lagarto)

        self.image = self.lagartos[0]
        self.rect = self.image.get_rect()
        self.rect.center = -200, -200

    def Dificuldade(self):

        if leveis.lvl_0:
            if self.ataque:
                self.velocidade_animacao = 0.15
            elif self.kill:
                self.velocidade_animacao = 0.15
            else:
                self.velocidade_animacao = 0.10
            self.velocidade = 5
        if leveis.lvl_1:
            if self.ataque:
                self.velocidade_animacao = 0.17
            elif self.kill:
                self.velocidade_animacao = 0.15
            else:
                self.velocidade_animacao = 0.11
            self.velocidade = 6
        if leveis.lvl_2:
            if self.ataque:
                self.velocidade_animacao = 0.19
            elif self.kill:
                self.velocidade_animacao = 0.15
            else:
                self.velocidade_animacao = 0.12
            self.velocidade = 7
        if leveis.lvl_3:
            if self.ataque:
                self.velocidade_animacao = 0.21
            elif self.kill:
                self.velocidade_animacao = 0.15
            else:
                self.velocidade_animacao = 0.13
            self.velocidade = 8
        if leveis.lvl_4:
            if self.ataque:
                self.velocidade_animacao = 0.23
            elif self.kill:
                self.velocidade_animacao = 0.15
            else:
                self.velocidade_animacao = 0.14
            self.velocidade = 9
        if leveis.lvl_5:
            if self.ataque:
                self.velocidade_animacao = 0.25
            elif self.kill:
                self.velocidade_animacao = 0.15
            else:
                self.velocidade_animacao = 0.15
            self.velocidade = 10

    def Animacao(self):

        if self.kill:
            estado_atual = "kill"
        elif self.ataque:
            estado_atual = "ataque"
        else:
            estado_atual = "parado"

        if estado_atual != self.estado_anterior:
            self.contador_lagarto = 0
            self.estado_anterior = estado_atual

        if self.contador_lagarto >= len(self.lagartos) and not self.kill:
            self.contador_lagarto = 0

        if not self.kill:
            self.image = self.lagartos[int(self.contador_lagarto)]
            self.contador_lagarto += self.velocidade_animacao

        elif self.kill:
            if self.contador_lagarto >= len(self.lagartos):
                self.contador_lagarto = 3
        if self.kill:
            if self.contador_lagarto <= 4:
                self.image = self.lagartos[int(self.contador_lagarto)]
                self.contador_lagarto += self.velocidade_animacao


        for i in self.andando:

            i[0] -= self.velocidade
            if i[0] < -10 and not canguru.morreu:
                self.andando.remove(i)
                self.contador_lagarto = 0  # RESET DO CONTADOR
                self.ataque = False  # VOLTA AO ESTADO INICIAL
                self.parado = True
                self.kill = False
                self.spawn = False
                self.spawn_on = True
                self.x = 1500
                self.y = choice([240, 272])
                self.andando.append([self.x, self.y])
                grupos = self.groups()
                if grupos:
                    grupo = grupos[0]
                    grupo.change_layer(self, self.get_layer())
            if (not canguru.morreu and
                    100 <= i[0] - self.canguru.rect.x <= 320 and
                    not self.kill and
                    ((canguru.cima and self.cima) or (canguru.baixo and self.baixo))):
                self.ataque = True
                self.parado = False

                if self.canguru.rect.y <= 120 and not self.kill:
                    self.contador_lagarto = 0

            else:
                self.ataque = False
                self.parado = True

    def Colisao(self):
        if not self.kill:
            canguru_hitbox = canguru.Colisao()

            self.lagarto_hitbox_corpo = pygame.Rect(self.rect.x + 120, self.rect.y + 95, 50, 80)
            #pygame.draw.rect(tela, (0, 0, 0), self.lagarto_hitbox_corpo, 2)
            self.lagarto_hitbox_cabeca = pygame.Rect(self.rect.x + 110, self.rect.y + 75, 50, 30)
            #pygame.draw.rect(tela, (0, 0, 0), self.lagarto_hitbox_cabeca, 2)
            self.lagarto_ataque_hitbox = pygame.Rect(0, 0, 0, 0)

            if self.ataque == True:
                if self.contador_lagarto >2:
                    self.lagarto_ataque_hitbox = pygame.Rect(self.rect.x + 20, self.rect.y + 50, 40, 120)
                    #pygame.draw.rect(tela, (250, 150, 100), self.lagarto_ataque_hitbox, 2)
                elif self.contador_lagarto >1 and self.contador_lagarto <2:
                    self.lagarto_ataque_hitbox = pygame.Rect(self.rect.x + 70, self.rect.y -10, 40, 70)
                    #pygame.draw.rect(tela, (250, 150, 100), self.lagarto_ataque_hitbox, 2)
                elif self.contador_lagarto >0 and self.contador_lagarto <1:
                    self.lagarto_ataque_hitbox = pygame.Rect(self.rect.x + 70, self.rect.y + 95, 50, 50)
                    #pygame.draw.rect(tela, (250, 150, 100), self.lagarto_ataque_hitbox, 2)
            else:
                self.lagarto_hitbox_arma = pygame.Rect(self.rect.x + 70, self.rect.y + 95, 50, 50)
                #pygame.draw.rect(tela, (50, 150, 200), self.lagarto_hitbox_arma, 2)

           #Colisao canguru
            for hitbox in canguru_hitbox:
                if self.ataque:
                    if ((self.lagarto_hitbox_corpo.colliderect(hitbox) or self.lagarto_hitbox_cabeca.colliderect(hitbox)
                             or self.lagarto_ataque_hitbox.colliderect(hitbox)) and ((canguru.cima and self.cima)
                            or (canguru.baixo and self.baixo))):
                        #print("COLIDIU COM O lagarto!")
                        if canguru.contador_colisao == 0:
                            vidas_rosto.dano = True
                            vidas_numeros.dano = True
                            canguru.contador_colisao = 1
                else:
                    if ((self.lagarto_hitbox_corpo.colliderect(hitbox) or self.lagarto_hitbox_cabeca.colliderect(hitbox))
                            and ((canguru.cima and self.cima) or (canguru.baixo and self.baixo))):
                        #print("COLIDIU COM O lagarto!")
                        if canguru.contador_colisao == 0:
                            vidas_rosto.dano = True
                            vidas_numeros.dano = True
                            canguru.contador_colisao = 1
                    #colisao bumerangue
            if bumerangue is not None:  # Se o bumerangue existe
                bumerangue_hitbox = bumerangue.Colisao() or []  # Se Colisao() retornar None, usa lista vazia
                for hitbox in bumerangue_hitbox:
                    if self.cima and (self.lagarto_hitbox_corpo.colliderect(hitbox)
                                      or self.lagarto_hitbox_cabeca.colliderect(hitbox)):
                        #print("bumerangue acertou")
                        bumerangue.indo = False
                        bumerangue.voltando = True
                        bumerangue.acertou = True
                        self.kill = True


    def update(self):
        self.Sprites()
        if self.spawn:
            self.spawn_on = False
            self.Dificuldade()
            self.Animacao()

            if self.y == 272:
                self.baixo = True
                self.cima = False

            if self.y == 240:
                self.cima = True
                self.baixo = False

            grupos = self.groups()
            if grupos:
                grupo = grupos[0]
                grupo.change_layer(self, self.get_layer())

            for i in self.andando:
                self.rect = self.image.get_rect()  #image ja foi deifinido pela lista de lagartos, ele ja existe independentre
                self.rect.topright = i[0], i[1]  # Posiciona o rect conforme a posição da nuvem
                tela.blit(self.image, self.rect)

            self.Colisao()
class Lagarto4(pygame.sprite.Sprite):
    def __init__(self,canguru,bumerangue):
        pygame.sprite.Sprite.__init__(self)

        self.canguru = canguru
        self.bumerangue = bumerangue
        self.x = randint(1600,1750)
        self.y = choice ([240,272])
        self.estado_anterior = "parado"

        self.contador_bumerangue = 0
        self.contador_lagarto = 0
        self.contado_ataque = 0
        self.spawn = False
        self.spawn_on = True
        self.kill = False
        self.baixo = False
        self.cima = False
        self.ataque = False
        self.parado = True
        self.andando = [] #para gerenciar x e y
        self.andando.append([self.x, self.y])

    def Sprites(self):

        self.lagartos = []

        if self.parado and not self.kill:
            for i in (0,1):
                imagem_lagarto = carroca_lagarto.subsurface((i * 397, 0), (397, 362))
                imagem_lagarto = pygame.transform.scale(imagem_lagarto, (397 / 2, 362 /2))
                self.lagartos.append(imagem_lagarto)

        elif self.ataque and not self.kill:
            for i in [2,3,4]:
                ataque_lagarto = carroca_lagarto.subsurface((i*397,0), (397,362))
                ataque_lagarto = pygame.transform.scale(ataque_lagarto, (397 / 2, 362 /2))
                self.lagartos.append(ataque_lagarto)

        elif self.kill:
            for i in [0,1,2,3]:
                morte_lagarto = carroca_morte1.subsurface((i*400,0), (400,400))
                morte_lagarto = pygame.transform.scale(morte_lagarto, (400/2,400/2))
                self.lagartos.append(morte_lagarto)

        self.image = self.lagartos[0]
        self.rect = self.image.get_rect()
        self.rect.center = -200, -200

    def Dificuldade(self):

        if leveis.lvl_0:
            if self.ataque:
                self.velocidade_animacao = 0.15
            elif self.kill:
                self.velocidade_animacao = 0.15
            else:
                self.velocidade_animacao = 0.10
            self.velocidade = 5
        if leveis.lvl_1:
            if self.ataque:
                self.velocidade_animacao = 0.17
            elif self.kill:
                self.velocidade_animacao = 0.15
            else:
                self.velocidade_animacao = 0.11
            self.velocidade = 6
        if leveis.lvl_2:
            if self.ataque:
                self.velocidade_animacao = 0.19
            elif self.kill:
                self.velocidade_animacao = 0.15
            else:
                self.velocidade_animacao = 0.12
            self.velocidade = 7
        if leveis.lvl_3:
            if self.ataque:
                self.velocidade_animacao = 0.21
            elif self.kill:
                self.velocidade_animacao = 0.15
            else:
                self.velocidade_animacao = 0.13
            self.velocidade = 8
        if leveis.lvl_4:
            if self.ataque:
                self.velocidade_animacao = 0.23
            elif self.kill:
                self.velocidade_animacao = 0.15
            else:
                self.velocidade_animacao = 0.14
            self.velocidade = 9
        if leveis.lvl_5:
            if self.ataque:
                self.velocidade_animacao = 0.25
            elif self.kill:
                self.velocidade_animacao = 0.15
            else:
                self.velocidade_animacao = 0.15
            self.velocidade = 10

    def Animacao(self):

        if self.kill:
            estado_atual = "kill"
        elif self.ataque:
            estado_atual = "ataque"
        else:
            estado_atual = "parado"

        if estado_atual != self.estado_anterior:
            self.contador_lagarto = 0
            self.estado_anterior = estado_atual

        if self.contador_lagarto >= len(self.lagartos) and not self.kill:
            self.contador_lagarto = 0

        if not self.kill:
            self.image = self.lagartos[int(self.contador_lagarto)]
            self.contador_lagarto += self.velocidade_animacao

        elif self.kill:
            if self.contador_lagarto >= len(self.lagartos):
                self.contador_lagarto = 3
        if self.kill:
            if self.contador_lagarto <= 4:
                self.image = self.lagartos[int(self.contador_lagarto)]
                self.contador_lagarto += self.velocidade_animacao


        for i in self.andando:

            i[0] -= self.velocidade
            if i[0] < -10 and not canguru.morreu:
                self.andando.remove(i)
                self.contador_lagarto = 0  # RESET DO CONTADOR
                self.ataque = False  # VOLTA AO ESTADO INICIAL
                self.parado = True
                self.kill = False
                self.spawn = False
                self.spawn_on = True
                self.x = randint(1600, 1750)
                self.y = choice([240, 272])
                self.andando.append([self.x, self.y])
                grupos = self.groups()
                if grupos:
                    grupo = grupos[0]
                    grupo.change_layer(self, self.get_layer())
            if (not canguru.morreu and
                    100 <= i[0] - self.canguru.rect.x <= 320 and
                    not self.kill and
                    ((canguru.cima and self.cima) or (canguru.baixo and self.baixo))):
                self.ataque = True
                self.parado = False

                if self.canguru.rect.y <= 120 and not self.kill:
                    self.contador_lagarto = 0

            else:
                self.ataque = False
                self.parado = True
    def get_layer(self):
        # Define a camada de desenho com base no Y
        return 6.5 if self.y == 272 else 6
    def Colisao(self):
        if not self.kill:
            canguru_hitbox = canguru.Colisao()

            self.lagarto_hitbox_corpo = pygame.Rect(self.rect.x + 120, self.rect.y + 95, 50, 80)
            #pygame.draw.rect(tela, (0, 0, 0), self.lagarto_hitbox_corpo, 2)
            self.lagarto_hitbox_cabeca = pygame.Rect(self.rect.x + 110, self.rect.y + 75, 50, 30)
            #pygame.draw.rect(tela, (0, 0, 0), self.lagarto_hitbox_cabeca, 2)
            self.lagarto_ataque_hitbox = pygame.Rect(0, 0, 0, 0)

            if self.ataque == True:
                if self.contador_lagarto >2:
                    self.lagarto_ataque_hitbox = pygame.Rect(self.rect.x + 20, self.rect.y + 50, 40, 120)
                    #pygame.draw.rect(tela, (250, 150, 100), self.lagarto_ataque_hitbox, 2)
                elif self.contador_lagarto >1 and self.contador_lagarto <2:
                    self.lagarto_ataque_hitbox = pygame.Rect(self.rect.x + 70, self.rect.y -10, 40, 70)
                    #pygame.draw.rect(tela, (250, 150, 100), self.lagarto_ataque_hitbox, 2)
                elif self.contador_lagarto >0 and self.contador_lagarto <1:
                    self.lagarto_ataque_hitbox = pygame.Rect(self.rect.x + 70, self.rect.y + 95, 50, 50)
                    #pygame.draw.rect(tela, (250, 150, 100), self.lagarto_ataque_hitbox, 2)
            else:
                self.lagarto_hitbox_arma = pygame.Rect(self.rect.x + 70, self.rect.y + 95, 50, 50)
                #pygame.draw.rect(tela, (50, 150, 200), self.lagarto_hitbox_arma, 2)

           #Colisao canguru
            for hitbox in canguru_hitbox:
                if self.ataque:
                    if ((self.lagarto_hitbox_corpo.colliderect(hitbox) or self.lagarto_hitbox_cabeca.colliderect(hitbox)
                             or self.lagarto_ataque_hitbox.colliderect(hitbox)) and ((canguru.cima and self.cima)
                            or (canguru.baixo and self.baixo))):
                        #print("COLIDIU COM O lagarto!")
                        if canguru.contador_colisao == 0:
                            vidas_rosto.dano = True
                            vidas_numeros.dano = True
                            canguru.contador_colisao = 1
                else:
                    if ((self.lagarto_hitbox_corpo.colliderect(hitbox) or self.lagarto_hitbox_cabeca.colliderect(hitbox))
                            and ((canguru.cima and self.cima) or (canguru.baixo and self.baixo))):
                        #print("COLIDIU COM O lagarto!")
                        if canguru.contador_colisao == 0:
                            vidas_rosto.dano = True
                            vidas_numeros.dano = True
                            canguru.contador_colisao = 1
                    #colisao bumerangue
            if bumerangue is not None:  # Se o bumerangue existe
                bumerangue_hitbox = bumerangue.Colisao() or []  # Se Colisao() retornar None, usa lista vazia
                for hitbox in bumerangue_hitbox:
                    if self.cima and (self.lagarto_hitbox_corpo.colliderect(hitbox)
                                      or self.lagarto_hitbox_cabeca.colliderect(hitbox)):
                        #print("bumerangue acertou")
                        bumerangue.indo = False
                        bumerangue.voltando = True
                        bumerangue.acertou = True
                        self.kill = True


    def update(self):
        self.Sprites()
        if self.spawn:
            self.spawn_on = False
            self.Dificuldade()
            self.Animacao()

            if self.y == 272:
                self.baixo = True
                self.cima = False

            if self.y == 240:
                self.cima = True
                self.baixo = False

            grupos = self.groups()
            if grupos:
                grupo = grupos[0]
                grupo.change_layer(self, self.get_layer())

            for i in self.andando:
                self.rect = self.image.get_rect()  #image ja foi deifinido pela lista de lagartos, ele ja existe independentre
                self.rect.topright = i[0], i[1]  # Posiciona o rect conforme a posição da nuvem
                tela.blit(self.image, self.rect)

            self.Colisao()
class Lagarto5(pygame.sprite.Sprite):
    def __init__(self,canguru,bumerangue):
        pygame.sprite.Sprite.__init__(self)

        self.canguru = canguru
        self.bumerangue = bumerangue
        self.x = randint(1800,1900)
        self.y = choice ([240,272])
        self.estado_anterior = "parado"

        self.contador_bumerangue = 0
        self.contador_lagarto = 0
        self.contado_ataque = 0
        self.spawn = False
        self.spawn_on = True
        self.kill = False
        self.baixo = False
        self.cima = False
        self.ataque = False
        self.parado = True
        self.andando = [] #para gerenciar x e y
        self.andando.append([self.x, self.y])

    def Sprites(self):

        self.lagartos = []

        if self.parado and not self.kill:
            for i in (0,1):
                imagem_lagarto = carroca_lagarto.subsurface((i * 397, 0), (397, 362))
                imagem_lagarto = pygame.transform.scale(imagem_lagarto, (397 / 2, 362 /2))
                self.lagartos.append(imagem_lagarto)

        elif self.ataque and not self.kill:
            for i in [2,3,4]:
                ataque_lagarto = carroca_lagarto.subsurface((i*397,0), (397,362))
                ataque_lagarto = pygame.transform.scale(ataque_lagarto, (397 / 2, 362 /2))
                self.lagartos.append(ataque_lagarto)

        elif self.kill:
            for i in [0,1,2,3]:
                morte_lagarto = carroca_morte1.subsurface((i*400,0), (400,400))
                morte_lagarto = pygame.transform.scale(morte_lagarto, (400/2,400/2))
                self.lagartos.append(morte_lagarto)

        self.image = self.lagartos[0]
        self.rect = self.image.get_rect()
        self.rect.center = -200, -200
    def get_layer(self):
        # Define a camada de desenho com base no Y
        return 6.5 if self.y == 272 else 6

    def Dificuldade(self):

        if leveis.lvl_0:
            if self.ataque:
                self.velocidade_animacao = 0.15
            elif self.kill:
                self.velocidade_animacao = 0.15
            else:
                self.velocidade_animacao = 0.10
            self.velocidade = 5
        if leveis.lvl_1:
            if self.ataque:
                self.velocidade_animacao = 0.17
            elif self.kill:
                self.velocidade_animacao = 0.15
            else:
                self.velocidade_animacao = 0.11
            self.velocidade = 6
        if leveis.lvl_2:
            if self.ataque:
                self.velocidade_animacao = 0.19
            elif self.kill:
                self.velocidade_animacao = 0.15
            else:
                self.velocidade_animacao = 0.12
            self.velocidade = 7
        if leveis.lvl_3:
            if self.ataque:
                self.velocidade_animacao = 0.21
            elif self.kill:
                self.velocidade_animacao = 0.15
            else:
                self.velocidade_animacao = 0.13
            self.velocidade = 8
        if leveis.lvl_4:
            if self.ataque:
                self.velocidade_animacao = 0.23
            elif self.kill:
                self.velocidade_animacao = 0.15
            else:
                self.velocidade_animacao = 0.14
            self.velocidade = 9
        if leveis.lvl_5:
            if self.ataque:
                self.velocidade_animacao = 0.25
            elif self.kill:
                self.velocidade_animacao = 0.15
            else:
                self.velocidade_animacao = 0.15
            self.velocidade = 10

    def Animacao(self):

        if self.kill:
            estado_atual = "kill"
        elif self.ataque:
            estado_atual = "ataque"
        else:
            estado_atual = "parado"

        if estado_atual != self.estado_anterior:
            self.contador_lagarto = 0
            self.estado_anterior = estado_atual


        if self.contador_lagarto >= len(self.lagartos) and not self.kill:
            self.contador_lagarto = 0

        if not self.kill:
            self.image = self.lagartos[int(self.contador_lagarto)]
            self.contador_lagarto += self.velocidade_animacao

        elif self.kill:
            if self.contador_lagarto >= len(self.lagartos):
                self.contador_lagarto = 3
        if self.kill:
            if self.contador_lagarto <= 4:
                self.image = self.lagartos[int(self.contador_lagarto)]
                self.contador_lagarto += self.velocidade_animacao


        for i in self.andando:

            i[0] -= self.velocidade
            if i[0] < -10 and not canguru.morreu:
                self.andando.remove(i)
                self.contador_lagarto = 0  # RESET DO CONTADOR
                self.ataque = False  # VOLTA AO ESTADO INICIAL
                self.parado = True
                self.kill = False
                self.spawn = False
                self.spawn_on = True
                self.x = randint(1800, 1900)
                self.y = choice([240, 272])
                self.andando.append([self.x, self.y])
                grupos = self.groups()
                if grupos:
                    grupo = grupos[0]
                    grupo.change_layer(self, self.get_layer())
            if (not canguru.morreu and
                    100 <= i[0] - self.canguru.rect.x <= 320 and
                    not self.kill and
                    ((canguru.cima and self.cima) or (canguru.baixo and self.baixo))):
                self.ataque = True
                self.parado = False

                if self.canguru.rect.y <= 120 and not self.kill:
                    self.contador_lagarto = 0

            else:
                self.ataque = False
                self.parado = True

    def Colisao(self):
        if not self.kill:
            canguru_hitbox = canguru.Colisao()

            self.lagarto_hitbox_corpo = pygame.Rect(self.rect.x + 120, self.rect.y + 95, 50, 80)
            #pygame.draw.rect(tela, (0, 0, 0), self.lagarto_hitbox_corpo, 2)
            self.lagarto_hitbox_cabeca = pygame.Rect(self.rect.x + 110, self.rect.y + 75, 50, 30)
            #pygame.draw.rect(tela, (0, 0, 0), self.lagarto_hitbox_cabeca, 2)
            self.lagarto_ataque_hitbox = pygame.Rect(0, 0, 0, 0)

            if self.ataque == True:
                if self.contador_lagarto >2:
                    self.lagarto_ataque_hitbox = pygame.Rect(self.rect.x + 20, self.rect.y + 50, 40, 120)
                    #pygame.draw.rect(tela, (250, 150, 100), self.lagarto_ataque_hitbox, 2)
                elif self.contador_lagarto >1 and self.contador_lagarto <2:
                    self.lagarto_ataque_hitbox = pygame.Rect(self.rect.x + 70, self.rect.y -10, 40, 70)
                    #pygame.draw.rect(tela, (250, 150, 100), self.lagarto_ataque_hitbox, 2)
                elif self.contador_lagarto >0 and self.contador_lagarto <1:
                    self.lagarto_ataque_hitbox = pygame.Rect(self.rect.x + 70, self.rect.y + 95, 50, 50)
                    #pygame.draw.rect(tela, (250, 150, 100), self.lagarto_ataque_hitbox, 2)
            else:
                self.lagarto_hitbox_arma = pygame.Rect(self.rect.x + 70, self.rect.y + 95, 50, 50)
                #pygame.draw.rect(tela, (50, 150, 200), self.lagarto_hitbox_arma, 2)

           #Colisao canguru
            for hitbox in canguru_hitbox:
                if self.ataque:
                    if ((self.lagarto_hitbox_corpo.colliderect(hitbox) or self.lagarto_hitbox_cabeca.colliderect(hitbox)
                             or self.lagarto_ataque_hitbox.colliderect(hitbox)) and ((canguru.cima and self.cima)
                            or (canguru.baixo and self.baixo))):
                        #print("COLIDIU COM O lagarto!")
                        if canguru.contador_colisao == 0:
                            vidas_rosto.dano = True
                            vidas_numeros.dano = True
                            canguru.contador_colisao = 1
                else:
                    if ((self.lagarto_hitbox_corpo.colliderect(hitbox) or self.lagarto_hitbox_cabeca.colliderect(hitbox))
                            and ((canguru.cima and self.cima) or (canguru.baixo and self.baixo))):
                        #print("COLIDIU COM O lagarto!")
                        if canguru.contador_colisao == 0:
                            vidas_rosto.dano = True
                            vidas_numeros.dano = True
                            canguru.contador_colisao = 1
                    #colisao bumerangue
            if bumerangue is not None:  # Se o bumerangue existe
                bumerangue_hitbox = bumerangue.Colisao() or []  # Se Colisao() retornar None, usa lista vazia
                for hitbox in bumerangue_hitbox:
                    if self.cima and (self.lagarto_hitbox_corpo.colliderect(hitbox)
                                      or self.lagarto_hitbox_cabeca.colliderect(hitbox)):
                        #print("bumerangue acertou")
                        bumerangue.indo = False
                        bumerangue.voltando = True
                        bumerangue.acertou = True
                        self.kill = True


    def update(self):
        self.Sprites()
        if self.spawn:
            self.spawn_on = False
            self.Dificuldade()
            self.Animacao()

            if self.y == 272:
                self.baixo = True
                self.cima = False

            if self.y == 240:
                self.cima = True
                self.baixo = False

            grupos = self.groups()
            if grupos:
                grupo = grupos[0]
                grupo.change_layer(self, self.get_layer())

            for i in self.andando:
                self.rect = self.image.get_rect()  #image ja foi deifinido pela lista de lagartos, ele ja existe independentre
                self.rect.topright = i[0], i[1]  # Posiciona o rect conforme a posição da nuvem
                tela.blit(self.image, self.rect)

            self.Colisao()

class Rato(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


        self.estado_anterior = "parado"
        self.contador = 0
        self.contador_ataque = 0
        self.velocidade_voo = 0
        self.velocidade = 0.10
        self.altura = [10,69,200]
        #self.ataques = [500]

        self.atacar = randint(450,570)
        self.x = 1000
        self.y = 0
        self.voando = [] #para gerenciar x e y
        self.voando.append([self.x, self.y])
        self.spawn = False
        self.spawn_on = True
        self.kill = False
        self.atacando = False
        self.atacou = False
        self.voar = True
        self.morto = False

    def sprites (self):

        self.lista_morte =[]
        for i in [0,1,2,3]:
            morte_rato = carroca_morte2.subsurface((i*400,0), (400,400))
            self.lista_morte.append(morte_rato)

        self.lista_aereo = []
        self.lista_aereo.append(carroca_rato.subsurface((0*500,0),(500,500)))
        self.lista_aereo.append(carroca_rato.subsurface((1*500,0),(500,500)))

        self.lista_atacou = []
        self.lista_atacou.append(carroca_rato.subsurface((4*500,0), (500,500)))
        self.lista_atacou.append(carroca_rato.subsurface((5*500,0), (500,500)))

        self.lista_atacando = []
        self.lista_atacando.append(carroca_rato.subsurface((2*500,0),(500,500)))
        self.lista_atacando.append(carroca_rato.subsurface((3* 500, 0), (500, 500)))

        self.image = self.lista_aereo[int(self.velocidade)]
        self.image = pygame.transform.scale(self.image, (500 // 4, 500 // 4))
        self.rect = self.image.get_rect()
        self.rect.center = (-200, -200)

    def ataque(self):
        if not canguru.morreu:
            if self.rect.x <= self.atacar + 5 and self.rect.x >= self.atacar - 5 and not self.atacando and not self.kill:
                self.voar = False
                self.atacando = True

    def Dificuldade(self):
        if leveis.lvl_0:
            self.velocidade = 0.05
            self.velocidade_voo = 4
            if self.kill:
                self.velocidade = 0.15
        if leveis.lvl_1:  # Só verifica se lvl_0 for False
            self.velocidade = 0.08
            self.velocidade_voo = 5
            if self.kill:
                self.velocidade = 0.15
        if leveis.lvl_2:  # Só verifica se os anteriores forem False
            self.velocidade = 0.10
            self.velocidade_voo = 6
            if self.kill:
                self.velocidade = 0.15
        if leveis.lvl_3:
            self.velocidade = 0.13
            self.velocidade_voo = 7
            if self.kill:
                self.velocidade = 0.15
        if leveis.lvl_4:
            self.velocidade = 0.15
            self.velocidade_voo = 8
            if self.kill:
                self.velocidade = 0.15
        if leveis.lvl_5:
            self.velocidade = 0.16
            self.velocidade_voo = 8
            if self.kill:
                self.velocidade = 0.15

    def animar(self):

        if self.kill:
            estado_atual = 'morte'
        elif self.atacando:
            estado_atual = 'atacando'
        elif self.atacou:
            estado_atual = 'atacou'
        elif self.voar:
            estado_atual = 'voando'
        else:
            estado_atual = 'idle'

        if hasattr(self, 'estado_anterior') and self.estado_anterior != estado_atual:
            self.contador = 0
        self.estado_anterior = estado_atual

        if self.kill:
            self.atacou = False
            self.atacando = False
            self.voar = True
            if self.contador >= len(self.lista_morte):
                self.contador= 3
            if self.contador <= 4:
                self.image = self.lista_morte[int(self.contador)]
                self.contador += self.velocidade

        elif self.atacando and not self.kill:
            if self.contador >= len(self.lista_atacando):
                self.atacando = False
                self.atacou = True
                self.contador = 0
            self.image = self.lista_atacando[int(self.contador)]
            self.contador += self.velocidade

        elif self.voar and not self.kill:
            if self.contador >= len(self.lista_aereo):
                self.contador = 0
            self.image = self.lista_aereo[int(self.contador)]
            self.contador += self.velocidade

        elif self.atacou and not self.atacando and not self.kill:
            if self.contador >= len(self.lista_atacou):
                self.contador = 0
            self.image = self.lista_atacou[int(self.contador)]
            self.contador += self.velocidade

        for i in self.voando:
            i[0] -= self.velocidade_voo
            if i[0] < -1 and not canguru.morreu:
                self.atacar = randint(450,570)
                self.atacou = False
                self.atacando = False
                self.voar = True
                self.voando.remove(i)
                self.morto = False
                self.kill = False
                self.contador = 0
                self.y = 0
                self.voando.append([self.x, self.y])
                self.spawn = False
                self.spawn_on = True

    def colisao(self):
        if not self.kill:
            canguru_hitbox = canguru.Colisao()

            for i in self.voando:

                self.image = pygame.transform.scale(self.image, (500 // 4, 500 // 4))
                corpo_hitbox = pygame.Rect(self.rect.x + 40, self.rect.y + 80, 40, 40)
                #pygame.draw.rect(tela, (255, 0, 0), corpo_hitbox, 2)
                cabeca_hitbox = pygame.Rect(self.rect.x + 20, self.rect.y + 40, 40, 40)
                #pygame.draw.rect(tela, (255, 0, 0), cabeca_hitbox, 2)
                rato_hitbox = pygame.Rect(self.rect.x + 40, self.rect.y + 0, 40, 80)
                #pygame.draw.rect(tela, (255, 0, 0), rato_hitbox, 2)


                for hitbox in canguru_hitbox:
                    if (corpo_hitbox.colliderect(hitbox) or cabeca_hitbox.colliderect(hitbox)
                            or rato_hitbox.colliderect(hitbox)):
                        #print("COLIDIU COM O Rato!")
                        if canguru.contador_colisao == 0:
                            vidas_rosto.dano = True
                            vidas_numeros.dano = True
                            canguru.contador_colisao = 1

                if bumerangue is not None:  # Se o bumerangue existe
                    bumerangue_hitbox = bumerangue.Colisao() or []  # Se Colisao() retornar None, usa lista vazia
                    for hitbox in bumerangue_hitbox:
                        if (corpo_hitbox.colliderect(hitbox) or cabeca_hitbox.colliderect(hitbox)
                            or rato_hitbox.colliderect(hitbox)):
                            #print("bumerangue acertou rato")
                            bumerangue.indo = False
                            bumerangue.voltando = True
                            bumerangue.acertou = True
                            self.kill = True

    def update(self):
        self.sprites()

        if self.spawn:
            self.spawn_on = False
            self.Dificuldade()
            self.animar()
            for i in self.voando:
                if self.kill:
                    self.image = pygame.transform.scale(self.image, (400 // 3, 400 // 2.8))
                    if self.kill and not self.morto:
                        i[1] -= 30
                        self.morto = True
                else:
                    self.image = pygame.transform.scale(self.image, (500 // 4, 500 // 4))

                self.rect = self.image.get_rect()  # Atualiza o rect da nuvem
                self.rect.topright = i[0], i[1]  # Posiciona o rect conforme a posição da nuvem
                tela.blit(self.image, self.rect)

            self.ataque()
            self.colisao()
class Rato2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.estado_anterior = "parado"
        self.contador = 0
        self.contador_ataque = 0
        self.velocidade_voo = 0
        self.velocidade = 0.10
        self.altura = [10,69,200]


        self.atacar = randint(450,570)
        self.x = 1080
        self.y = 50
        self.voando = [] #para gerenciar x e y
        self.voando.append([self.x, self.y])
        self.spawn = False
        self.spawn_on = True
        self.kill = False
        self.atacando = False
        self.atacou = False
        self.voar = True
        self.morto = False


    def sprites (self):

        self.lista_morte =[]
        for i in [0,1,2,3]:
            morte_rato = carroca_morte2.subsurface((i*400,0), (400,400))
            self.lista_morte.append(morte_rato)

        self.lista_aereo = []
        self.lista_aereo.append(carroca_rato.subsurface((0*500,0),(500,500)))
        self.lista_aereo.append(carroca_rato.subsurface((1*500,0),(500,500)))

        self.lista_atacou = []
        self.lista_atacou.append(carroca_rato.subsurface((4*500,0), (500,500)))
        self.lista_atacou.append(carroca_rato.subsurface((5*500,0), (500,500)))

        self.lista_atacando = []
        self.lista_atacando.append(carroca_rato.subsurface((2*500,0),(500,500)))
        self.lista_atacando.append(carroca_rato.subsurface((3* 500, 0), (500, 500)))

        self.image = self.lista_aereo[int(self.velocidade)]
        self.image = pygame.transform.scale(self.image, (500 // 4, 500 // 4))
        self.rect = self.image.get_rect()
        self.rect.center = (-200, -200)

    def ataque(self):
        if not canguru.morreu:
            if self.rect.x <= self.atacar + 5 and self.rect.x >= self.atacar - 5 and not self.atacando and not self.kill:
                self.voar = False
                self.atacando = True

    def Dificuldade(self):
        if leveis.lvl_0:
            self.velocidade = 0.05
            self.velocidade_voo = 4
            if self.kill:
                self.velocidade = 0.15
        if leveis.lvl_1:  # Só verifica se lvl_0 for False
            self.velocidade = 0.08
            self.velocidade_voo = 5
            if self.kill:
                self.velocidade = 0.15
        if leveis.lvl_2:  # Só verifica se os anteriores forem False
            self.velocidade = 0.10
            self.velocidade_voo = 6
            if self.kill:
                self.velocidade = 0.15
        if leveis.lvl_3:
            self.velocidade = 0.13
            self.velocidade_voo = 7
            if self.kill:
                self.velocidade = 0.15
        if leveis.lvl_4:
            self.velocidade = 0.15
            self.velocidade_voo = 8
            if self.kill:
                self.velocidade = 0.15
        if leveis.lvl_5:
            self.velocidade = 0.16
            self.velocidade_voo = 8
            if self.kill:
                self.velocidade = 0.15

    def animar(self):

        if self.kill:
            estado_atual = 'morte'
        elif self.atacando:
            estado_atual = 'atacando'
        elif self.atacou:
            estado_atual = 'atacou'
        elif self.voar:
            estado_atual = 'voando'
        else:
            estado_atual = 'idle'

        if hasattr(self, 'estado_anterior') and self.estado_anterior != estado_atual:
            self.contador = 0
        self.estado_anterior = estado_atual

        if self.kill:
            self.atacou = False
            self.atacando = False
            self.voar = True
            if self.contador >= len(self.lista_morte):
                self.contador= 3
            if self.contador <= 4:
                self.image = self.lista_morte[int(self.contador)]
                self.contador += self.velocidade

        elif self.atacando and not self.kill:
            if self.contador >= len(self.lista_atacando):
                self.atacando = False
                self.atacou = True
                self.contador = 0
            self.image = self.lista_atacando[int(self.contador)]
            self.contador += self.velocidade

        elif self.voar and not self.kill:
            if self.contador >= len(self.lista_aereo):
                self.contador = 0
            self.image = self.lista_aereo[int(self.contador)]
            self.contador += self.velocidade

        elif self.atacou and not self.atacando and not self.kill:
            if self.contador >= len(self.lista_atacou):
                self.contador = 0
            self.image = self.lista_atacou[int(self.contador)]
            self.contador += self.velocidade

        for i in self.voando:
            i[0] -= self.velocidade_voo
            if i[0] < -1 and not canguru.morreu:
                self.atacar = randint(450, 570)
                self.atacou = False
                self.atacando = False
                self.voar = True
                self.voando.remove(i)
                self.morto = False
                self.kill = False
                self.contador = 0
                self.y = 50
                self.voando.append([self.x, self.y])
                self.spawn = False
                self.spawn_on = True

    def colisao(self):
        if not self.kill:
            canguru_hitbox = canguru.Colisao()

            for i in self.voando:

                self.image = pygame.transform.scale(self.image, (500 // 4, 500 // 4))
                corpo_hitbox = pygame.Rect(self.rect.x + 40, self.rect.y + 80, 40, 40)
                #pygame.draw.rect(tela, (255, 0, 0), corpo_hitbox, 2)
                cabeca_hitbox = pygame.Rect(self.rect.x + 20, self.rect.y + 40, 40, 40)
                #pygame.draw.rect(tela, (255, 0, 0), cabeca_hitbox, 2)
                rato_hitbox = pygame.Rect(self.rect.x + 40, self.rect.y + 0, 40, 80)
                #pygame.draw.rect(tela, (255, 0, 0), rato_hitbox, 2)


                for hitbox in canguru_hitbox:
                    if (corpo_hitbox.colliderect(hitbox) or cabeca_hitbox.colliderect(hitbox)
                            or rato_hitbox.colliderect(hitbox)):
                        #print("COLIDIU COM O Rato!")
                        if canguru.contador_colisao == 0:
                            vidas_rosto.dano = True
                            vidas_numeros.dano = True
                            canguru.contador_colisao = 1

                if bumerangue is not None:  # Se o bumerangue existe
                    bumerangue_hitbox = bumerangue.Colisao() or []  # Se Colisao() retornar None, usa lista vazia
                    for hitbox in bumerangue_hitbox:
                        if (corpo_hitbox.colliderect(hitbox) or cabeca_hitbox.colliderect(hitbox)
                            or rato_hitbox.colliderect(hitbox)):
                            #print("bumerangue acertou rato")
                            bumerangue.indo = False
                            bumerangue.voltando = True
                            bumerangue.acertou = True
                            self.kill = True

    def update(self):
        self.sprites()

        if self.spawn:
            self.spawn_on = False
            self.Dificuldade()
            self.animar()
            for i in self.voando:
                if self.kill:
                    self.image = pygame.transform.scale(self.image, (400 // 3, 400 // 2.8))
                    if self.kill and not self.morto:
                        i[1] -= 30
                        self.morto = True
                else:
                    self.image = pygame.transform.scale(self.image, (500 // 4, 500 // 4))

                self.rect = self.image.get_rect()  # Atualiza o rect da nuvem
                self.rect.topright = i[0], i[1]  # Posiciona o rect conforme a posição da nuvem
                tela.blit(self.image, self.rect)

            self.ataque()
            self.colisao()
class Rato3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.estado_anterior = "parado"
        self.contador = 0
        self.contador_ataque = 0
        self.velocidade_voo = 0
        self.velocidade = 0.10
        self.altura = [10,69,200]


        self.atacar = randint(450,570)
        self.x = 1000
        self.y = 100
        self.voando = [] #para gerenciar x e y
        self.voando.append([self.x, self.y])
        self.spawn = False
        self.spawn_on = True
        self.kill = False
        self.atacando = False
        self.atacou = False
        self.voar = True
        self.morto = False


    def sprites (self):

        self.lista_morte =[]
        for i in [0,1,2,3]:
            morte_rato = carroca_morte2.subsurface((i*400,0), (400,400))
            self.lista_morte.append(morte_rato)

        self.lista_aereo = []
        self.lista_aereo.append(carroca_rato.subsurface((0*500,0),(500,500)))
        self.lista_aereo.append(carroca_rato.subsurface((1*500,0),(500,500)))

        self.lista_atacou = []
        self.lista_atacou.append(carroca_rato.subsurface((4*500,0), (500,500)))
        self.lista_atacou.append(carroca_rato.subsurface((5*500,0), (500,500)))

        self.lista_atacando = []
        self.lista_atacando.append(carroca_rato.subsurface((2*500,0),(500,500)))
        self.lista_atacando.append(carroca_rato.subsurface((3* 500, 0), (500, 500)))

        self.image = self.lista_aereo[int(self.velocidade)]
        self.image = pygame.transform.scale(self.image, (500 // 4, 500 // 4))
        self.rect = self.image.get_rect()
        self.rect.center = (-200, -200)

    def ataque(self):
        if not canguru.morreu:
            if self.rect.x <= self.atacar + 5 and self.rect.x >= self.atacar - 5 and not self.atacando and not self.kill:
                self.voar = False
                self.atacando = True

    def Dificuldade(self):
        if leveis.lvl_0:
            self.velocidade = 0.05
            self.velocidade_voo = 4
            if self.kill:
                self.velocidade = 0.15
        if leveis.lvl_1:  # Só verifica se lvl_0 for False
            self.velocidade = 0.08
            self.velocidade_voo = 5
            if self.kill:
                self.velocidade = 0.15
        if leveis.lvl_2:  # Só verifica se os anteriores forem False
            self.velocidade = 0.10
            self.velocidade_voo = 6
            if self.kill:
                self.velocidade = 0.15
        if leveis.lvl_3:
            self.velocidade = 0.13
            self.velocidade_voo = 7
            if self.kill:
                self.velocidade = 0.15
        if leveis.lvl_4:
            self.velocidade = 0.15
            self.velocidade_voo = 8
            if self.kill:
                self.velocidade = 0.15
        if leveis.lvl_5:
            self.velocidade = 0.16
            self.velocidade_voo = 8
            if self.kill:
                self.velocidade = 0.15

    def animar(self):

        if self.kill:
            estado_atual = 'morte'
        elif self.atacando:
            estado_atual = 'atacando'
        elif self.atacou:
            estado_atual = 'atacou'
        elif self.voar:
            estado_atual = 'voando'
        else:
            estado_atual = 'idle'

        if hasattr(self, 'estado_anterior') and self.estado_anterior != estado_atual:
            self.contador = 0
        self.estado_anterior = estado_atual

        if self.kill:
            self.atacou = False
            self.atacando = False
            self.voar = True
            if self.contador >= len(self.lista_morte):
                self.contador= 3
            if self.contador <= 4:
                self.image = self.lista_morte[int(self.contador)]
                self.contador += self.velocidade

        elif self.atacando and not self.kill:
            if self.contador >= len(self.lista_atacando):
                self.atacando = False
                self.atacou = True
                self.contador = 0
            self.image = self.lista_atacando[int(self.contador)]
            self.contador += self.velocidade

        elif self.voar and not self.kill:
            if self.contador >= len(self.lista_aereo):
                self.contador = 0
            self.image = self.lista_aereo[int(self.contador)]
            self.contador += self.velocidade

        elif self.atacou and not self.atacando and not self.kill:
            if self.contador >= len(self.lista_atacou):
                self.contador = 0
            self.image = self.lista_atacou[int(self.contador)]
            self.contador += self.velocidade

        for i in self.voando:
            i[0] -= self.velocidade_voo
            if i[0] < -1 and not canguru.morreu:
                self.atacar = randint(450, 570)
                self.atacou = False
                self.atacando = False
                self.voar = True
                self.voando.remove(i)
                self.morto = False
                self.kill = False
                self.contador = 0
                self.y = 100
                self.voando.append([self.x, self.y])
                self.spawn = False
                self.spawn_on = True


    def colisao(self):
        if not self.kill:
            canguru_hitbox = canguru.Colisao()

            for i in self.voando:

                self.image = pygame.transform.scale(self.image, (500 // 4, 500 // 4))
                corpo_hitbox = pygame.Rect(self.rect.x + 40, self.rect.y + 80, 40, 40)
                #pygame.draw.rect(tela, (255, 0, 0), corpo_hitbox, 2)
                cabeca_hitbox = pygame.Rect(self.rect.x + 20, self.rect.y + 40, 40, 40)
                #pygame.draw.rect(tela, (255, 0, 0), cabeca_hitbox, 2)
                rato_hitbox = pygame.Rect(self.rect.x + 40, self.rect.y + 0, 40, 80)
                #pygame.draw.rect(tela, (255, 0, 0), rato_hitbox, 2)


                for hitbox in canguru_hitbox:
                    if (corpo_hitbox.colliderect(hitbox) or cabeca_hitbox.colliderect(hitbox)
                            or rato_hitbox.colliderect(hitbox)):
                        #print("COLIDIU COM O Rato!")
                        if canguru.contador_colisao == 0:
                            vidas_rosto.dano = True
                            vidas_numeros.dano = True
                            canguru.contador_colisao = 1

                if bumerangue is not None:  # Se o bumerangue existe
                    bumerangue_hitbox = bumerangue.Colisao() or []  # Se Colisao() retornar None, usa lista vazia
                    for hitbox in bumerangue_hitbox:
                        if (corpo_hitbox.colliderect(hitbox) or cabeca_hitbox.colliderect(hitbox)
                            or rato_hitbox.colliderect(hitbox)):
                            #print("bumerangue acertou rato")
                            bumerangue.indo = False
                            bumerangue.voltando = True
                            bumerangue.acertou = True
                            self.kill = True

    def update(self):
        self.sprites()

        if self.spawn:
            self.spawn_on = False
            self.Dificuldade()
            self.animar()
            for i in self.voando:
                if self.kill:
                    self.image = pygame.transform.scale(self.image, (400 // 3, 400 // 2.8))
                    if self.kill and not self.morto:
                        i[1] -= 30
                        self.morto = True
                else:
                    self.image = pygame.transform.scale(self.image, (500 // 4, 500 // 4))

                self.rect = self.image.get_rect()  # Atualiza o rect da nuvem
                self.rect.topright = i[0], i[1]  # Posiciona o rect conforme a posição da nuvem
                tela.blit(self.image, self.rect)

            self.ataque()
            self.colisao()
class Rato4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.estado_anterior = "parado"
        self.contador = 0
        self.contador_ataque = 0
        self.velocidade_voo = 0
        self.velocidade = 0.10
        self.altura = [10,69,200]
        #self.ataques = [500]

        self.atacar = randint(450,570)
        self.x = 1080
        self.y = 150
        self.voando = [] #para gerenciar x e y
        self.voando.append([self.x, self.y])
        self.spawn = False
        self.spawn_on = True
        self.kill = False
        self.atacando = False
        self.atacou = False
        self.voar = True
        self.morto = False


    def sprites (self):

        self.lista_morte =[]
        for i in [0,1,2,3]:
            morte_rato = carroca_morte2.subsurface((i*400,0), (400,400))
            self.lista_morte.append(morte_rato)

        self.lista_aereo = []
        self.lista_aereo.append(carroca_rato.subsurface((0*500,0),(500,500)))
        self.lista_aereo.append(carroca_rato.subsurface((1*500,0),(500,500)))

        self.lista_atacou = []
        self.lista_atacou.append(carroca_rato.subsurface((4*500,0), (500,500)))
        self.lista_atacou.append(carroca_rato.subsurface((5*500,0), (500,500)))

        self.lista_atacando = []
        self.lista_atacando.append(carroca_rato.subsurface((2*500,0),(500,500)))
        self.lista_atacando.append(carroca_rato.subsurface((3* 500, 0), (500, 500)))

        self.image = self.lista_aereo[int(self.velocidade)]
        self.image = pygame.transform.scale(self.image, (500 // 4, 500 // 4))
        self.rect = self.image.get_rect()
        self.rect.center = (-200, -200)

    def ataque(self):
        if not canguru.morreu:
            if self.rect.x <= self.atacar + 5 and self.rect.x >= self.atacar - 5 and not self.atacando and not self.kill:
                self.voar = False
                self.atacando = True

    def Dificuldade(self):
        if leveis.lvl_0:
            self.velocidade = 0.05
            self.velocidade_voo = 4
            if self.kill:
                self.velocidade = 0.15
        if leveis.lvl_1:  # Só verifica se lvl_0 for False
            self.velocidade = 0.08
            self.velocidade_voo = 5
            if self.kill:
                self.velocidade = 0.15
        if leveis.lvl_2:  # Só verifica se os anteriores forem False
            self.velocidade = 0.10
            self.velocidade_voo = 6
            if self.kill:
                self.velocidade = 0.15
        if leveis.lvl_3:
            self.velocidade = 0.13
            self.velocidade_voo = 7
            if self.kill:
                self.velocidade = 0.15
        if leveis.lvl_4:
            self.velocidade = 0.15
            self.velocidade_voo = 8
            if self.kill:
                self.velocidade = 0.15
        if leveis.lvl_5:
            self.velocidade = 0.16
            self.velocidade_voo = 8
            if self.kill:
                self.velocidade = 0.15

    def animar(self):

        if self.kill:
            estado_atual = 'morte'
        elif self.atacando:
            estado_atual = 'atacando'
        elif self.atacou:
            estado_atual = 'atacou'
        elif self.voar:
            estado_atual = 'voando'
        else:
            estado_atual = 'idle'

        if hasattr(self, 'estado_anterior') and self.estado_anterior != estado_atual:
            self.contador = 0
        self.estado_anterior = estado_atual

        if self.kill:
            self.atacou = False
            self.atacando = False
            self.voar = True
            if self.contador >= len(self.lista_morte):
                self.contador= 3
            if self.contador <= 4:
                self.image = self.lista_morte[int(self.contador)]
                self.contador += self.velocidade

        elif self.atacando and not self.kill:
            if self.contador >= len(self.lista_atacando):
                self.atacando = False
                self.atacou = True
                self.contador = 0
            self.image = self.lista_atacando[int(self.contador)]
            self.contador += self.velocidade

        elif self.voar and not self.kill:
            if self.contador >= len(self.lista_aereo):
                self.contador = 0
            self.image = self.lista_aereo[int(self.contador)]
            self.contador += self.velocidade

        elif self.atacou and not self.atacando and not self.kill:
            if self.contador >= len(self.lista_atacou):
                self.contador = 0
            self.image = self.lista_atacou[int(self.contador)]
            self.contador += self.velocidade

        for i in self.voando:
            i[0] -= self.velocidade_voo
            if i[0] < -1 and not canguru.morreu:
                self.atacar = randint(450, 570)
                self.atacou = False
                self.atacando = False
                self.voar = True
                self.voando.remove(i)
                self.morto = False
                self.kill = False
                self.contador = 0
                self.y = 150
                self.voando.append([self.x, self.y])
                self.spawn = False
                self.spawn_on = True


    def colisao(self):
        if not self.kill:
            canguru_hitbox = canguru.Colisao()

            for i in self.voando:

                self.image = pygame.transform.scale(self.image, (500 // 4, 500 // 4))
                corpo_hitbox = pygame.Rect(self.rect.x + 40, self.rect.y + 80, 40, 40)
                #pygame.draw.rect(tela, (255, 0, 0), corpo_hitbox, 2)
                cabeca_hitbox = pygame.Rect(self.rect.x + 20, self.rect.y + 40, 40, 40)
                #pygame.draw.rect(tela, (255, 0, 0), cabeca_hitbox, 2)
                rato_hitbox = pygame.Rect(self.rect.x + 40, self.rect.y + 0, 40, 80)
                #pygame.draw.rect(tela, (255, 0, 0), rato_hitbox, 2)


                for hitbox in canguru_hitbox:
                    if (corpo_hitbox.colliderect(hitbox) or cabeca_hitbox.colliderect(hitbox)
                            or rato_hitbox.colliderect(hitbox)):
                        #print("COLIDIU COM O Rato!")
                        if canguru.contador_colisao == 0:
                            vidas_rosto.dano = True
                            vidas_numeros.dano = True
                            canguru.contador_colisao = 1

                if bumerangue is not None:  # Se o bumerangue existe
                    bumerangue_hitbox = bumerangue.Colisao() or []  # Se Colisao() retornar None, usa lista vazia
                    for hitbox in bumerangue_hitbox:
                        if (corpo_hitbox.colliderect(hitbox) or cabeca_hitbox.colliderect(hitbox)
                            or rato_hitbox.colliderect(hitbox)):
                            #print("bumerangue acertou rato")
                            bumerangue.indo = False
                            bumerangue.voltando = True
                            bumerangue.acertou = True
                            self.kill = True

    def update(self):
        self.sprites()

        if self.spawn:
            self.spawn_on = False
            self.Dificuldade()
            self.animar()
            for i in self.voando:
                if self.kill:
                    self.image = pygame.transform.scale(self.image, (400 // 3, 400 // 2.8))
                    if self.kill and not self.morto:
                        i[1] -= 30
                        self.morto = True
                else:
                    self.image = pygame.transform.scale(self.image, (500 // 4, 500 // 4))

                self.rect = self.image.get_rect()  # Atualiza o rect da nuvem
                self.rect.topright = i[0], i[1]  # Posiciona o rect conforme a posição da nuvem
                tela.blit(self.image, self.rect)

            self.ataque()
            self.colisao()
class Rato5(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.estado_anterior = "parado"
        self.contador = 0
        self.contador_ataque = 0
        self.velocidade_voo = 0
        self.velocidade = 0.10
        self.altura = [10,69,200]
        #self.ataques = [500]

        self.atacar = randint(450,570)
        self.x = 1000
        self.y = 200
        self.voando = [] #para gerenciar x e y
        self.voando.append([self.x, self.y])
        self.spawn = False
        self.spawn_on = True
        self.kill = False
        self.atacando = False
        self.atacou = False
        self.voar = True
        self.morto = False


    def sprites (self):

        self.lista_morte =[]
        for i in [0,1,2,3]:
            morte_rato = carroca_morte2.subsurface((i*400,0), (400,400))
            self.lista_morte.append(morte_rato)

        self.lista_aereo = []
        self.lista_aereo.append(carroca_rato.subsurface((0*500,0),(500,500)))
        self.lista_aereo.append(carroca_rato.subsurface((1*500,0),(500,500)))

        self.lista_atacou = []
        self.lista_atacou.append(carroca_rato.subsurface((4*500,0), (500,500)))
        self.lista_atacou.append(carroca_rato.subsurface((5*500,0), (500,500)))

        self.lista_atacando = []
        self.lista_atacando.append(carroca_rato.subsurface((2*500,0),(500,500)))
        self.lista_atacando.append(carroca_rato.subsurface((3* 500, 0), (500, 500)))

        self.image = self.lista_aereo[int(self.velocidade)]
        self.image = pygame.transform.scale(self.image, (500 // 4, 500 // 4))
        self.rect = self.image.get_rect()
        self.rect.center = (-200, -200)

    def ataque(self):
        if not canguru.morreu:
            if self.rect.x <= self.atacar + 5 and self.rect.x >= self.atacar - 5 and not self.atacando and not self.kill:
                self.voar = False
                self.atacando = True

    def Dificuldade(self):
        if leveis.lvl_0:
            self.velocidade = 0.05
            self.velocidade_voo = 4
            if self.kill:
                self.velocidade = 0.15
        if leveis.lvl_1:  # Só verifica se lvl_0 for False
            self.velocidade = 0.08
            self.velocidade_voo = 5
            if self.kill:
                self.velocidade = 0.15
        if leveis.lvl_2:  # Só verifica se os anteriores forem False
            self.velocidade = 0.10
            self.velocidade_voo = 6
            if self.kill:
                self.velocidade = 0.15
        if leveis.lvl_3:
            self.velocidade = 0.13
            self.velocidade_voo = 7
            if self.kill:
                self.velocidade = 0.15
        if leveis.lvl_4:
            self.velocidade = 0.15
            self.velocidade_voo = 8
            if self.kill:
                self.velocidade = 0.15
        if leveis.lvl_5:
            self.velocidade = 0.16
            self.velocidade_voo = 8
            if self.kill:
                self.velocidade = 0.15

    def animar(self):

        if self.kill:
            estado_atual = 'morte'
        elif self.atacando:
            estado_atual = 'atacando'
        elif self.atacou:
            estado_atual = 'atacou'
        elif self.voar:
            estado_atual = 'voando'
        else:
            estado_atual = 'idle'

        if hasattr(self, 'estado_anterior') and self.estado_anterior != estado_atual:
            self.contador = 0
        self.estado_anterior = estado_atual

        if self.kill:
            self.atacou = False
            self.atacando = False
            self.voar = True
            if self.contador >= len(self.lista_morte):
                self.contador= 3
            if self.contador <= 4:
                self.image = self.lista_morte[int(self.contador)]
                self.contador += self.velocidade

        elif self.atacando and not self.kill:
            if self.contador >= len(self.lista_atacando):
                self.atacando = False
                self.atacou = True
                self.contador = 0
            self.image = self.lista_atacando[int(self.contador)]
            self.contador += self.velocidade

        elif self.voar and not self.kill:
            if self.contador >= len(self.lista_aereo):
                self.contador = 0
            self.image = self.lista_aereo[int(self.contador)]
            self.contador += self.velocidade

        elif self.atacou and not self.atacando and not self.kill:
            if self.contador >= len(self.lista_atacou):
                self.contador = 0
            self.image = self.lista_atacou[int(self.contador)]
            self.contador += self.velocidade

        for i in self.voando:
            i[0] -= self.velocidade_voo
            if i[0] < -1 and not canguru.morreu:
                self.atacar = randint(450, 570)
                self.atacou = False
                self.atacando = False
                self.voar = True
                self.voando.remove(i)
                self.morto = False
                self.kill = False
                self.contador = 0
                self.y = 200
                self.voando.append([self.x, self.y])
                self.spawn = False
                self.spawn_on = True


    def colisao(self):
        if not self.kill:
            canguru_hitbox = canguru.Colisao()

            for i in self.voando:

                self.image = pygame.transform.scale(self.image, (500 // 4, 500 // 4))
                corpo_hitbox = pygame.Rect(self.rect.x + 40, self.rect.y + 80, 40, 40)
                #pygame.draw.rect(tela, (255, 0, 0), corpo_hitbox, 2)
                cabeca_hitbox = pygame.Rect(self.rect.x + 20, self.rect.y + 40, 40, 40)
                #pygame.draw.rect(tela, (255, 0, 0), cabeca_hitbox, 2)
                rato_hitbox = pygame.Rect(self.rect.x + 40, self.rect.y + 0, 40, 80)
                #pygame.draw.rect(tela, (255, 0, 0), rato_hitbox, 2)


                for hitbox in canguru_hitbox:
                    if (corpo_hitbox.colliderect(hitbox) or cabeca_hitbox.colliderect(hitbox)
                            or rato_hitbox.colliderect(hitbox)):
                        #print("COLIDIU COM O Rato!")
                        if canguru.contador_colisao == 0:
                            vidas_rosto.dano = True
                            vidas_numeros.dano = True
                            canguru.contador_colisao = 1

                if bumerangue is not None:  # Se o bumerangue existe
                    bumerangue_hitbox = bumerangue.Colisao() or []  # Se Colisao() retornar None, usa lista vazia
                    for hitbox in bumerangue_hitbox:
                        if (corpo_hitbox.colliderect(hitbox) or cabeca_hitbox.colliderect(hitbox)
                            or rato_hitbox.colliderect(hitbox)):
                            #print("bumerangue acertou rato")
                            bumerangue.indo = False
                            bumerangue.voltando = True
                            bumerangue.acertou = True
                            self.kill = True

    def update(self):
        self.sprites()

        if self.spawn:
            self.spawn_on = False
            self.Dificuldade()
            self.animar()
            for i in self.voando:
                if self.kill:
                    self.image = pygame.transform.scale(self.image, (400 // 3, 400 // 2.8))
                    if self.kill and not self.morto:
                        i[1] -= 30
                        self.morto = True
                else:
                    self.image = pygame.transform.scale(self.image, (500 // 4, 500 // 4))

                self.rect = self.image.get_rect()  # Atualiza o rect da nuvem
                self.rect.topright = i[0], i[1]  # Posiciona o rect conforme a posição da nuvem
                tela.blit(self.image, self.rect)

            self.ataque()
            self.colisao()
class Rato6(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.estado_anterior = "parado"
        self.contador = 0
        self.contador_ataque = 0
        self.velocidade_voo = 0
        self.velocidade = 0.10
        self.altura = [10,69,200]
        #self.ataques = [500]

        self.atacar = randint(450,570)
        self.x = 1600
        self.y = 50
        self.voando = [] #para gerenciar x e y
        self.voando.append([self.x, self.y])
        self.spawn = False
        self.spawn_on = True
        self.kill = False
        self.atacando = False
        self.atacou = False
        self.voar = True
        self.morto = False


    def sprites (self):

        self.lista_morte =[]
        for i in [0,1,2,3]:
            morte_rato = carroca_morte2.subsurface((i*400,0), (400,400))
            self.lista_morte.append(morte_rato)

        self.lista_aereo = []
        self.lista_aereo.append(carroca_rato.subsurface((0*500,0),(500,500)))
        self.lista_aereo.append(carroca_rato.subsurface((1*500,0),(500,500)))

        self.lista_atacou = []
        self.lista_atacou.append(carroca_rato.subsurface((4*500,0), (500,500)))
        self.lista_atacou.append(carroca_rato.subsurface((5*500,0), (500,500)))

        self.lista_atacando = []
        self.lista_atacando.append(carroca_rato.subsurface((2*500,0),(500,500)))
        self.lista_atacando.append(carroca_rato.subsurface((3* 500, 0), (500, 500)))

        self.image = self.lista_aereo[int(self.velocidade)]
        self.image = pygame.transform.scale(self.image, (500 // 4, 500 // 4))
        self.rect = self.image.get_rect()
        self.rect.center = (-200, -200)

    def ataque(self):
        if not canguru.morreu:
            if self.rect.x <= self.atacar + 5 and self.rect.x >= self.atacar - 5 and not self.atacando and not self.kill:
                self.voar = False
                self.atacando = True

    def Dificuldade(self):
        if leveis.lvl_0:
            self.velocidade = 0.05
            self.velocidade_voo = 4
            if self.kill:
                self.velocidade = 0.15
        if leveis.lvl_1:  # Só verifica se lvl_0 for False
            self.velocidade = 0.08
            self.velocidade_voo = 5
            if self.kill:
                self.velocidade = 0.15
        if leveis.lvl_2:  # Só verifica se os anteriores forem False
            self.velocidade = 0.10
            self.velocidade_voo = 6
            if self.kill:
                self.velocidade = 0.15
        if leveis.lvl_3:
            self.velocidade = 0.13
            self.velocidade_voo = 7
            if self.kill:
                self.velocidade = 0.15
        if leveis.lvl_4:
            self.velocidade = 0.15
            self.velocidade_voo = 8
            if self.kill:
                self.velocidade = 0.15
        if leveis.lvl_5:
            self.velocidade = 0.16
            self.velocidade_voo = 8
            if self.kill:
                self.velocidade = 0.15

    def animar(self):

        if self.kill:
            estado_atual = 'morte'
        elif self.atacando:
            estado_atual = 'atacando'
        elif self.atacou:
            estado_atual = 'atacou'
        elif self.voar:
            estado_atual = 'voando'
        else:
            estado_atual = 'idle'

        if hasattr(self, 'estado_anterior') and self.estado_anterior != estado_atual:
            self.contador = 0
        self.estado_anterior = estado_atual

        if self.kill:
            self.atacou = False
            self.atacando = False
            self.voar = True
            if self.contador >= len(self.lista_morte):
                self.contador= 3
            if self.contador <= 4:
                self.image = self.lista_morte[int(self.contador)]
                self.contador += self.velocidade

        elif self.atacando and not self.kill:
            if self.contador >= len(self.lista_atacando):
                self.atacando = False
                self.atacou = True
                self.contador = 0
            self.image = self.lista_atacando[int(self.contador)]
            self.contador += self.velocidade

        elif self.voar and not self.kill:
            if self.contador >= len(self.lista_aereo):
                self.contador = 0
            self.image = self.lista_aereo[int(self.contador)]
            self.contador += self.velocidade

        elif self.atacou and not self.atacando and not self.kill:
            if self.contador >= len(self.lista_atacou):
                self.contador = 0
            self.image = self.lista_atacou[int(self.contador)]
            self.contador += self.velocidade

        for i in self.voando:
            i[0] -= self.velocidade_voo
            if i[0] < -1 and not canguru.morreu:
                self.atacar = randint(450, 570)
                self.atacou = False
                self.atacando = False
                self.voar = True
                self.voando.remove(i)
                self.morto = False
                self.kill = False
                self.contador = 0

                self.y = 50
                self.voando.append([self.x, self.y])
                self.spawn = False
                self.spawn_on = True


    def colisao(self):
        if not self.kill:
            canguru_hitbox = canguru.Colisao()

            for i in self.voando:

                self.image = pygame.transform.scale(self.image, (500 // 4, 500 // 4))
                corpo_hitbox = pygame.Rect(self.rect.x + 40, self.rect.y + 80, 40, 40)
                #pygame.draw.rect(tela, (255, 0, 0), corpo_hitbox, 2)
                cabeca_hitbox = pygame.Rect(self.rect.x + 20, self.rect.y + 40, 40, 40)
                #pygame.draw.rect(tela, (255, 0, 0), cabeca_hitbox, 2)
                rato_hitbox = pygame.Rect(self.rect.x + 40, self.rect.y + 0, 40, 80)
                #pygame.draw.rect(tela, (255, 0, 0), rato_hitbox, 2)


                for hitbox in canguru_hitbox:
                    if (corpo_hitbox.colliderect(hitbox) or cabeca_hitbox.colliderect(hitbox)
                            or rato_hitbox.colliderect(hitbox)):
                        #print("COLIDIU COM O Rato!")
                        if canguru.contador_colisao == 0:
                            vidas_rosto.dano = True
                            vidas_numeros.dano = True
                            canguru.contador_colisao = 1

                if bumerangue is not None:  # Se o bumerangue existe
                    bumerangue_hitbox = bumerangue.Colisao() or []  # Se Colisao() retornar None, usa lista vazia
                    for hitbox in bumerangue_hitbox:
                        if (corpo_hitbox.colliderect(hitbox) or cabeca_hitbox.colliderect(hitbox)
                            or rato_hitbox.colliderect(hitbox)):
                            #print("bumerangue acertou rato")
                            bumerangue.indo = False
                            bumerangue.voltando = True
                            bumerangue.acertou = True
                            self.kill = True

    def update(self):
        self.sprites()

        if self.spawn:
            self.spawn_on = False
            self.Dificuldade()
            self.animar()
            for i in self.voando:
                if self.kill:
                    self.image = pygame.transform.scale(self.image, (400 // 3, 400 // 2.8))
                    if self.kill and not self.morto:
                        i[1] -= 30
                        self.morto = True
                else:
                    self.image = pygame.transform.scale(self.image, (500 // 4, 500 // 4))

                self.rect = self.image.get_rect()  # Atualiza o rect da nuvem
                self.rect.topright = i[0], i[1]  # Posiciona o rect conforme a posição da nuvem
                tela.blit(self.image, self.rect)

            self.ataque()
            self.colisao()

class Osso(pygame.sprite.Sprite):
    def __init__(self,rato,canguru):
        pygame.sprite.Sprite.__init__(self)
        self.contador_osso = 0
        self.rato = rato
        self.canguru = canguru

        self.atirar = False
        self.Sprites()
        self.x = 0
        self.y = 0
        self.velocidade = 8

    def Sprites(self):
        self.osso = []
        for i in range (6,14):
            imagem_osso = carroca_rato.subsurface((i * 500, 0), (500, 500))
            imagem_osso = pygame.transform.scale(imagem_osso, (500/3, 500/3))
            self.osso.append(imagem_osso)
        self.image = self.osso[0]
        self.rect = self.image.get_rect()
        self.rect.center = (-100, -100)

    def osso_on(self):
        # Animação do osso (se houver)
        # Mantém a lógica de animação original
        self.contador_osso += 0.5
        if hasattr(self, 'osso') and self.osso:  # Garante que self.osso existe e não está vazio
            if self.contador_osso >= len(self.osso):
                self.contador_osso = 0
            self.image = self.osso[int(self.contador_osso) % len(self.osso)]

        # Verifica se deve iniciar um novo ataque
        if self.rato.atacando and not self.atirar:
            self.atirar = True
            # Define a posição inicial do osso como a posição atual do rato
            self.rect.center = self.rato.rect.center
            self.x, self.y = self.rect.center

            # Pega a posição ATUAL do canguru no momento do disparo
            alvo_x, alvo_y = self.canguru.rect.center

            # --- DEBUG: Imprimir coordenadas no momento do disparo (descomente se precisar) ---
            # print(f"Disparo iniciado! Rato: ({self.x:.2f}, {self.y:.2f}), Canguru: ({alvo_x}, {alvo_y})")
            # -----------------------------------------------------------------------------

            # Calcula o vetor de direção do rato para o canguru
            delta_x = alvo_x - self.x
            delta_y = alvo_y - self.y

            # Calcula a distância (magnitude do vetor)
            # Usamos max(1, ...) para evitar divisão por zero se a distância for muito pequena ou zero
            distancia = max(1, math.sqrt(delta_x ** 2 + delta_y ** 2))

            # --- AJUSTE PRINCIPAL: Aumentar a velocidade total do osso ---
            # Experimente valores diferentes aqui se necessário (ex: 15, 20, 25)
            velocidade_total_osso = 18 # Valor anterior era 8, aumentamos significativamente


                # -------------------------------------------------------------

            # Calcula as componentes X e Y da velocidade
            # Normaliza o vetor (divide pela distância) e multiplica pela velocidade total
            self.velocidade_x = (delta_x / distancia) * velocidade_total_osso
            self.velocidade_y = (delta_y / distancia) * velocidade_total_osso

            # --- DEBUG: Imprimir vetor e velocidades calculadas (descomente se precisar) ---
            # print(f"  Delta: ({delta_x:.2f}, {delta_y:.2f}), Dist: {distancia:.2f}")
            # print(f"  Velocidade Calculada: ({self.velocidade_x:.2f}, {self.velocidade_y:.2f})")
            # -----------------------------------------------------------------------------

        # Movimenta o osso se ele foi atirado
        if self.atirar:
            if rato.rect.x - canguru.rect.x <= 200:
                self.x += self.velocidade_x -5
                self.y += self.velocidade_y -5
                self.rect.center = (int(self.x), int(self.y))

            else:
                # Atualiza a posição X e Y com base nas componentes de velocidade calculadas
                self.x += self.velocidade_x - 2
                self.y += self.velocidade_y - 5
                self.rect.center = (int(self.x), int(self.y))

            # --- DEBUG: Imprimir posição atual do osso (descomente se precisar) ---
            # print(f"  Osso em movimento: ({self.x:.2f}, {self.y:.2f})")
            # ---------------------------------------------------------------------

            # Condição de reset (ex: saiu da tela)
            # Considerar adicionar mais condições (sair pela direita, por cima, por baixo)
            # Exemplo: if self.rect.right < 0 or self.rect.left > LARGURA_TELA or self.rect.bottom < 0 or self.rect.top > ALTURA_TELA:
            if self.rect.right < 0:  # Mantendo sua condição original por enquanto

                self.contador_osso = 0  # Reinicia a animação
                # Reposiciona fora da tela para evitar colisões indesejadas até o próximo tiro
                self.rect.center = (-100, -100)
                self.x, self.y = self.rect.center
                # print("Osso resetado.") # Debug
            if rato.rect.x <= -10:
                self.atirar = False

    def Colisao(self):
        osso_hitbox = pygame.Rect(self.rect.x + 55, self.rect.y + 70, 40, 30)
        #pygame.draw.rect(tela, (250, 105, 180), osso_hitbox, 2)
        canguru_hitbox = canguru.Colisao()

        for hitbox in canguru_hitbox:
            if osso_hitbox.colliderect(hitbox):
                #print("COLIDIU COM O Osso!")
                if canguru.contador_colisao == 0:
                    vidas_rosto.dano = True
                    vidas_numeros.dano = True
                    canguru.contador_colisao = 1

    def update(self):
        self.osso_on()
        self.Colisao()
class Osso2(pygame.sprite.Sprite):
    def __init__(self,rato2,canguru):
        pygame.sprite.Sprite.__init__(self)
        self.contador_osso = 0

        self.rato2 = rato2
        self.canguru = canguru

        self.atirar = False
        self.Sprites()
        self.x = 0
        self.y = 0
        self.velocidade = 8

    def Sprites(self):
        self.osso = []
        for i in range (6,14):
            imagem_osso = carroca_rato.subsurface((i * 500, 0), (500, 500))
            imagem_osso = pygame.transform.scale(imagem_osso, (500/3, 500/3))
            self.osso.append(imagem_osso)
        self.image = self.osso[0]
        self.rect = self.image.get_rect()
        self.rect.center = (-100, -100)

    def osso_on(self):
        # Animação do osso (se houver)
        # Mantém a lógica de animação original
        self.contador_osso += 0.5
        if hasattr(self, 'osso') and self.osso:  # Garante que self.osso existe e não está vazio
            if self.contador_osso >= len(self.osso):
                self.contador_osso = 0
            self.image = self.osso[int(self.contador_osso) % len(self.osso)]

        # Verifica se deve iniciar um novo ataque
        if self.rato2.atacando and not self.atirar:
            self.atirar = True
            # Define a posição inicial do osso como a posição atual do rato
            self.rect.center = self.rato2.rect.center
            self.x, self.y = self.rect.center

            # Pega a posição ATUAL do canguru no momento do disparo
            alvo_x, alvo_y = self.canguru.rect.center

            # --- DEBUG: Imprimir coordenadas no momento do disparo (descomente se precisar) ---
            # print(f"Disparo iniciado! Rato: ({self.x:.2f}, {self.y:.2f}), Canguru: ({alvo_x}, {alvo_y})")
            # -----------------------------------------------------------------------------

            # Calcula o vetor de direção do rato para o canguru
            delta_x = alvo_x - self.x
            delta_y = alvo_y - self.y

            # Calcula a distância (magnitude do vetor)
            # Usamos max(1, ...) para evitar divisão por zero se a distância for muito pequena ou zero
            distancia = max(1, math.sqrt(delta_x ** 2 + delta_y ** 2))

            # --- AJUSTE PRINCIPAL: Aumentar a velocidade total do osso ---
            # Experimente valores diferentes aqui se necessário (ex: 15, 20, 25)
            velocidade_total_osso = 18 # Valor anterior era 8, aumentamos significativamente


                # -------------------------------------------------------------

            # Calcula as componentes X e Y da velocidade
            # Normaliza o vetor (divide pela distância) e multiplica pela velocidade total
            self.velocidade_x = (delta_x / distancia) * velocidade_total_osso
            self.velocidade_y = (delta_y / distancia) * velocidade_total_osso

            # --- DEBUG: Imprimir vetor e velocidades calculadas (descomente se precisar) ---
            # print(f"  Delta: ({delta_x:.2f}, {delta_y:.2f}), Dist: {distancia:.2f}")
            # print(f"  Velocidade Calculada: ({self.velocidade_x:.2f}, {self.velocidade_y:.2f})")
            # -----------------------------------------------------------------------------

        # Movimenta o osso se ele foi atirado
        if self.atirar:
            if self.rato2.rect.x - canguru.rect.x <= 200:
                self.x += self.velocidade_x -5
                self.y += self.velocidade_y -5
                self.rect.center = (int(self.x), int(self.y))

            else:
                # Atualiza a posição X e Y com base nas componentes de velocidade calculadas
                self.x += self.velocidade_x - 2
                self.y += self.velocidade_y - 5
                self.rect.center = (int(self.x), int(self.y))

            # --- DEBUG: Imprimir posição atual do osso (descomente se precisar) ---
            # print(f"  Osso em movimento: ({self.x:.2f}, {self.y:.2f})")
            # ---------------------------------------------------------------------

            # Condição de reset (ex: saiu da tela)
            # Considerar adicionar mais condições (sair pela direita, por cima, por baixo)
            # Exemplo: if self.rect.right < 0 or self.rect.left > LARGURA_TELA or self.rect.bottom < 0 or self.rect.top > ALTURA_TELA:
            if self.rect.right < 0:  # Mantendo sua condição original por enquanto

                self.contador_osso = 0  # Reinicia a animação
                # Reposiciona fora da tela para evitar colisões indesejadas até o próximo tiro
                self.rect.center = (-100, -100)
                self.x, self.y = self.rect.center
                # print("Osso resetado.") # Debug
            if self.rato2.rect.x <= -10:
                self.atirar = False



    def Colisao(self):
        osso_hitbox = pygame.Rect(self.rect.x + 55, self.rect.y + 70, 40, 30)
        #pygame.draw.rect(tela, (250, 105, 180), osso_hitbox, 2)
        canguru_hitbox = canguru.Colisao()

        for hitbox in canguru_hitbox:
            if osso_hitbox.colliderect(hitbox):
                #print("COLIDIU COM O Osso!")
                if canguru.contador_colisao == 0:
                    vidas_rosto.dano = True
                    vidas_numeros.dano = True
                    canguru.contador_colisao = 1

    def update(self):
        self.osso_on()
        self.Colisao()
class Osso3(pygame.sprite.Sprite):
    def __init__(self,rato3,canguru):
        pygame.sprite.Sprite.__init__(self)
        self.contador_osso = 0

        self.rato3 = rato3
        self.canguru = canguru

        self.atirar = False
        self.Sprites()
        self.x = 0
        self.y = 0
        self.velocidade = 8

    def Sprites(self):
        self.osso = []
        for i in range (6,14):
            imagem_osso = carroca_rato.subsurface((i * 500, 0), (500, 500))
            imagem_osso = pygame.transform.scale(imagem_osso, (500/3, 500/3))
            self.osso.append(imagem_osso)
        self.image = self.osso[0]
        self.rect = self.image.get_rect()
        self.rect.center = (-100, -100)

    def osso_on(self):
        # Animação do osso (se houver)
        # Mantém a lógica de animação original
        self.contador_osso += 0.5
        if hasattr(self, 'osso') and self.osso:  # Garante que self.osso existe e não está vazio
            if self.contador_osso >= len(self.osso):
                self.contador_osso = 0
            self.image = self.osso[int(self.contador_osso) % len(self.osso)]

        # Verifica se deve iniciar um novo ataque
        if self.rato3.atacando and not self.atirar:
            self.atirar = True
            # Define a posição inicial do osso como a posição atual do rato
            self.rect.center = self.rato3.rect.center
            self.x, self.y = self.rect.center

            # Pega a posição ATUAL do canguru no momento do disparo
            alvo_x, alvo_y = self.canguru.rect.center

            # --- DEBUG: Imprimir coordenadas no momento do disparo (descomente se precisar) ---
            # print(f"Disparo iniciado! Rato: ({self.x:.2f}, {self.y:.2f}), Canguru: ({alvo_x}, {alvo_y})")
            # -----------------------------------------------------------------------------

            # Calcula o vetor de direção do rato para o canguru
            delta_x = alvo_x - self.x
            delta_y = alvo_y - self.y

            # Calcula a distância (magnitude do vetor)
            # Usamos max(1, ...) para evitar divisão por zero se a distância for muito pequena ou zero
            distancia = max(1, math.sqrt(delta_x ** 2 + delta_y ** 2))

            # --- AJUSTE PRINCIPAL: Aumentar a velocidade total do osso ---
            # Experimente valores diferentes aqui se necessário (ex: 15, 20, 25)
            self.velocidade_total_osso = 18 # Valor anterior era 8, aumentamos significativamente


                # -------------------------------------------------------------

            # Calcula as componentes X e Y da velocidade
            # Normaliza o vetor (divide pela distância) e multiplica pela velocidade total
            self.velocidade_x = (delta_x / distancia) * self.velocidade_total_osso
            self.velocidade_y = (delta_y / distancia) * self.velocidade_total_osso

            # --- DEBUG: Imprimir vetor e velocidades calculadas (descomente se precisar) ---
            # print(f"  Delta: ({delta_x:.2f}, {delta_y:.2f}), Dist: {distancia:.2f}")
            # print(f"  Velocidade Calculada: ({self.velocidade_x:.2f}, {self.velocidade_y:.2f})")
            # -----------------------------------------------------------------------------

        # Movimenta o osso se ele foi atirado
        if self.atirar:
            if self.rato3.rect.x - canguru.rect.x <= 200:
                self.x += self.velocidade_x -5
                self.y += self.velocidade_y -5
                self.rect.center = (int(self.x), int(self.y))

            else:
                # Atualiza a posição X e Y com base nas componentes de velocidade calculadas
                self.x += self.velocidade_x - 2
                self.y += self.velocidade_y - 5
                self.rect.center = (int(self.x), int(self.y))

            # --- DEBUG: Imprimir posição atual do osso (descomente se precisar) ---
            # print(f"  Osso em movimento: ({self.x:.2f}, {self.y:.2f})")
            # ---------------------------------------------------------------------

            # Condição de reset (ex: saiu da tela)
            # Considerar adicionar mais condições (sair pela direita, por cima, por baixo)
            # Exemplo: if self.rect.right < 0 or self.rect.left > LARGURA_TELA or self.rect.bottom < 0 or self.rect.top > ALTURA_TELA:
            if self.rect.right < 0:  # Mantendo sua condição original por enquanto

                self.contador_osso = 0  # Reinicia a animação
                # Reposiciona fora da tela para evitar colisões indesejadas até o próximo tiro
                self.rect.center = (-100, -100)
                self.x, self.y = self.rect.center
                # print("Osso resetado.") # Debug
            if self.rato3.rect.x <= -10:
                self.atirar = False



    def Colisao(self):
        osso_hitbox = pygame.Rect(self.rect.x + 55, self.rect.y + 70, 40, 30)
        #pygame.draw.rect(tela, (250, 105, 180), osso_hitbox, 2)
        canguru_hitbox = canguru.Colisao()

        for hitbox in canguru_hitbox:
            if osso_hitbox.colliderect(hitbox):
                #print("COLIDIU COM O Osso!")
                if canguru.contador_colisao == 0:
                    vidas_rosto.dano = True
                    vidas_numeros.dano = True
                    canguru.contador_colisao = 1

    def update(self):
        self.osso_on()
        self.Colisao()
class Osso4(pygame.sprite.Sprite):
    def __init__(self,rato4,canguru):
        pygame.sprite.Sprite.__init__(self)
        self.contador_osso = 0

        self.rato4 = rato4
        self.canguru = canguru

        self.atirar = False
        self.Sprites()
        self.x = 0
        self.y = 0
        self.velocidade = 8

    def Sprites(self):
        self.osso = []
        for i in range (6,14):
            imagem_osso = carroca_rato.subsurface((i * 500, 0), (500, 500))
            imagem_osso = pygame.transform.scale(imagem_osso, (500/3, 500/3))
            self.osso.append(imagem_osso)
        self.image = self.osso[0]
        self.rect = self.image.get_rect()
        self.rect.center = (-100, -100)

    def osso_on(self):
        # Animação do osso (se houver)
        # Mantém a lógica de animação original
        self.contador_osso += 0.5
        if hasattr(self, 'osso') and self.osso:  # Garante que self.osso existe e não está vazio
            if self.contador_osso >= len(self.osso):
                self.contador_osso = 0
            self.image = self.osso[int(self.contador_osso) % len(self.osso)]

        # Verifica se deve iniciar um novo ataque
        if self.rato4.atacando and not self.atirar:
            self.atirar = True
            # Define a posição inicial do osso como a posição atual do rato
            self.rect.center = self.rato4.rect.center
            self.x, self.y = self.rect.center

            # Pega a posição ATUAL do canguru no momento do disparo
            alvo_x, alvo_y = self.canguru.rect.center

            # --- DEBUG: Imprimir coordenadas no momento do disparo (descomente se precisar) ---
            # print(f"Disparo iniciado! Rato: ({self.x:.2f}, {self.y:.2f}), Canguru: ({alvo_x}, {alvo_y})")
            # -----------------------------------------------------------------------------

            # Calcula o vetor de direção do rato para o canguru
            delta_x = alvo_x - self.x
            delta_y = alvo_y - self.y

            # Calcula a distância (magnitude do vetor)
            # Usamos max(1, ...) para evitar divisão por zero se a distância for muito pequena ou zero
            distancia = max(1, math.sqrt(delta_x ** 2 + delta_y ** 2))

            # --- AJUSTE PRINCIPAL: Aumentar a velocidade total do osso ---
            # Experimente valores diferentes aqui se necessário (ex: 15, 20, 25)
            velocidade_total_osso = 18 # Valor anterior era 8, aumentamos significativamente


                # -------------------------------------------------------------

            # Calcula as componentes X e Y da velocidade
            # Normaliza o vetor (divide pela distância) e multiplica pela velocidade total
            self.velocidade_x = (delta_x / distancia) * velocidade_total_osso
            self.velocidade_y = (delta_y / distancia) * velocidade_total_osso

            # --- DEBUG: Imprimir vetor e velocidades calculadas (descomente se precisar) ---
            # print(f"  Delta: ({delta_x:.2f}, {delta_y:.2f}), Dist: {distancia:.2f}")
            # print(f"  Velocidade Calculada: ({self.velocidade_x:.2f}, {self.velocidade_y:.2f})")
            # -----------------------------------------------------------------------------

        # Movimenta o osso se ele foi atirado
        if self.atirar:
            if self.rato4.rect.x - canguru.rect.x <= 200:
                self.x += self.velocidade_x -5
                self.y += self.velocidade_y -5
                self.rect.center = (int(self.x), int(self.y))

            else:
                # Atualiza a posição X e Y com base nas componentes de velocidade calculadas
                self.x += self.velocidade_x - 2
                self.y += self.velocidade_y - 5
                self.rect.center = (int(self.x), int(self.y))

            # --- DEBUG: Imprimir posição atual do osso (descomente se precisar) ---
            # print(f"  Osso em movimento: ({self.x:.2f}, {self.y:.2f})")
            # ---------------------------------------------------------------------

            # Condição de reset (ex: saiu da tela)
            # Considerar adicionar mais condições (sair pela direita, por cima, por baixo)
            # Exemplo: if self.rect.right < 0 or self.rect.left > LARGURA_TELA or self.rect.bottom < 0 or self.rect.top > ALTURA_TELA:
            if self.rect.right < 0:  # Mantendo sua condição original por enquanto

                self.contador_osso = 0  # Reinicia a animação
                # Reposiciona fora da tela para evitar colisões indesejadas até o próximo tiro
                self.rect.center = (-100, -100)
                self.x, self.y = self.rect.center
                # print("Osso resetado.") # Debug
            if self.rato4.rect.x <= -10:
                self.atirar = False



    def Colisao(self):
        osso_hitbox = pygame.Rect(self.rect.x + 55, self.rect.y + 70, 40, 30)
        #pygame.draw.rect(tela, (250, 105, 180), osso_hitbox, 2)
        canguru_hitbox = canguru.Colisao()

        for hitbox in canguru_hitbox:
            if osso_hitbox.colliderect(hitbox):
                #print("COLIDIU COM O Osso!")
                if canguru.contador_colisao == 0:
                    vidas_rosto.dano = True
                    vidas_numeros.dano = True
                    canguru.contador_colisao = 1

    def update(self):
        self.osso_on()
        self.Colisao()
class Osso5(pygame.sprite.Sprite):
    def __init__(self,rato5,canguru):
        pygame.sprite.Sprite.__init__(self)
        self.contador_osso = 0

        self.rato5 = rato5
        self.canguru = canguru

        self.atirar = False
        self.Sprites()
        self.x = 0
        self.y = 0
        self.velocidade = 8

    def Sprites(self):
        self.osso = []
        for i in range (6,14):
            imagem_osso = carroca_rato.subsurface((i * 500, 0), (500, 500))
            imagem_osso = pygame.transform.scale(imagem_osso, (500/3, 500/3))
            self.osso.append(imagem_osso)
        self.image = self.osso[0]
        self.rect = self.image.get_rect()
        self.rect.center = (-100, -100)

    def osso_on(self):
        # Animação do osso (se houver)
        # Mantém a lógica de animação original
        self.contador_osso += 0.5
        if hasattr(self, 'osso') and self.osso:  # Garante que self.osso existe e não está vazio
            if self.contador_osso >= len(self.osso):
                self.contador_osso = 0
            self.image = self.osso[int(self.contador_osso) % len(self.osso)]

        # Verifica se deve iniciar um novo ataque
        if self.rato5.atacando and not self.atirar:
            self.atirar = True
            # Define a posição inicial do osso como a posição atual do rato
            self.rect.center = self.rato5.rect.center
            self.x, self.y = self.rect.center

            # Pega a posição ATUAL do canguru no momento do disparo
            alvo_x, alvo_y = self.canguru.rect.center

            # --- DEBUG: Imprimir coordenadas no momento do disparo (descomente se precisar) ---
            # print(f"Disparo iniciado! Rato: ({self.x:.2f}, {self.y:.2f}), Canguru: ({alvo_x}, {alvo_y})")
            # -----------------------------------------------------------------------------

            # Calcula o vetor de direção do rato para o canguru
            delta_x = alvo_x - self.x
            delta_y = alvo_y - self.y

            # Calcula a distância (magnitude do vetor)
            # Usamos max(1, ...) para evitar divisão por zero se a distância for muito pequena ou zero
            distancia = max(1, math.sqrt(delta_x ** 2 + delta_y ** 2))

            # --- AJUSTE PRINCIPAL: Aumentar a velocidade total do osso ---
            # Experimente valores diferentes aqui se necessário (ex: 15, 20, 25)
            velocidade_total_osso = 18 # Valor anterior era 8, aumentamos significativamente


                # -------------------------------------------------------------

            # Calcula as componentes X e Y da velocidade
            # Normaliza o vetor (divide pela distância) e multiplica pela velocidade total
            self.velocidade_x = (delta_x / distancia) * velocidade_total_osso
            self.velocidade_y = (delta_y / distancia) * velocidade_total_osso

            # --- DEBUG: Imprimir vetor e velocidades calculadas (descomente se precisar) ---
            # print(f"  Delta: ({delta_x:.2f}, {delta_y:.2f}), Dist: {distancia:.2f}")
            # print(f"  Velocidade Calculada: ({self.velocidade_x:.2f}, {self.velocidade_y:.2f})")
            # -----------------------------------------------------------------------------

        # Movimenta o osso se ele foi atirado
        if self.atirar:
            if self.rato5.rect.x - canguru.rect.x <= 200:
                self.x += self.velocidade_x -5
                self.y += self.velocidade_y -5
                self.rect.center = (int(self.x), int(self.y))

            else:
                # Atualiza a posição X e Y com base nas componentes de velocidade calculadas
                self.x += self.velocidade_x - 2
                self.y += self.velocidade_y - 5
                self.rect.center = (int(self.x), int(self.y))

            # --- DEBUG: Imprimir posição atual do osso (descomente se precisar) ---
            # print(f"  Osso em movimento: ({self.x:.2f}, {self.y:.2f})")
            # ---------------------------------------------------------------------

            # Condição de reset (ex: saiu da tela)
            # Considerar adicionar mais condições (sair pela direita, por cima, por baixo)
            # Exemplo: if self.rect.right < 0 or self.rect.left > LARGURA_TELA or self.rect.bottom < 0 or self.rect.top > ALTURA_TELA:
            if self.rect.right < 0:  # Mantendo sua condição original por enquanto

                self.contador_osso = 0  # Reinicia a animação
                # Reposiciona fora da tela para evitar colisões indesejadas até o próximo tiro
                self.rect.center = (-100, -100)
                self.x, self.y = self.rect.center
                # print("Osso resetado.") # Debug
            if self.rato5.rect.x <= -10:
                self.atirar = False



    def Colisao(self):
        osso_hitbox = pygame.Rect(self.rect.x + 55, self.rect.y + 70, 40, 30)
        #pygame.draw.rect(tela, (250, 105, 180), osso_hitbox, 2)
        canguru_hitbox = canguru.Colisao()

        for hitbox in canguru_hitbox:
            if osso_hitbox.colliderect(hitbox):
                #print("COLIDIU COM O Osso!")
                if canguru.contador_colisao == 0:
                    vidas_rosto.dano = True
                    vidas_numeros.dano = True
                    canguru.contador_colisao = 1

    def update(self):
        self.osso_on()
        self.Colisao()
class Osso6(pygame.sprite.Sprite):
    def __init__(self,rato6,canguru):
        pygame.sprite.Sprite.__init__(self)
        self.contador_osso = 0

        self.rato6 = rato6
        self.canguru = canguru

        self.atirar = False
        self.Sprites()
        self.x = 0
        self.y = 0
        self.velocidade = 8

    def Sprites(self):
        self.osso = []
        for i in range (6,14):
            imagem_osso = carroca_rato.subsurface((i * 500, 0), (500, 500))
            imagem_osso = pygame.transform.scale(imagem_osso, (500/3, 500/3))
            self.osso.append(imagem_osso)
        self.image = self.osso[0]
        self.rect = self.image.get_rect()
        self.rect.center = (-100, -100)

    def osso_on(self):
        # Animação do osso (se houver)
        # Mantém a lógica de animação original
        self.contador_osso += 0.5
        if hasattr(self, 'osso') and self.osso:  # Garante que self.osso existe e não está vazio
            if self.contador_osso >= len(self.osso):
                self.contador_osso = 0
            self.image = self.osso[int(self.contador_osso) % len(self.osso)]

        # Verifica se deve iniciar um novo ataque
        if self.rato6.atacando and not self.atirar:
            self.atirar = True
            # Define a posição inicial do osso como a posição atual do rato
            self.rect.center = self.rato6.rect.center
            self.x, self.y = self.rect.center

            # Pega a posição ATUAL do canguru no momento do disparo
            alvo_x, alvo_y = self.canguru.rect.center

            # --- DEBUG: Imprimir coordenadas no momento do disparo (descomente se precisar) ---
            # print(f"Disparo iniciado! Rato: ({self.x:.2f}, {self.y:.2f}), Canguru: ({alvo_x}, {alvo_y})")
            # -----------------------------------------------------------------------------

            # Calcula o vetor de direção do rato para o canguru
            delta_x = alvo_x - self.x
            delta_y = alvo_y - self.y

            # Calcula a distância (magnitude do vetor)
            # Usamos max(1, ...) para evitar divisão por zero se a distância for muito pequena ou zero
            distancia = max(1, math.sqrt(delta_x ** 2 + delta_y ** 2))

            # --- AJUSTE PRINCIPAL: Aumentar a velocidade total do osso ---
            # Experimente valores diferentes aqui se necessário (ex: 15, 20, 25)
            velocidade_total_osso = 18 # Valor anterior era 8, aumentamos significativamente


                # -------------------------------------------------------------

            # Calcula as componentes X e Y da velocidade
            # Normaliza o vetor (divide pela distância) e multiplica pela velocidade total
            self.velocidade_x = (delta_x / distancia) * velocidade_total_osso
            self.velocidade_y = (delta_y / distancia) * velocidade_total_osso

            # --- DEBUG: Imprimir vetor e velocidades calculadas (descomente se precisar) ---
            # print(f"  Delta: ({delta_x:.2f}, {delta_y:.2f}), Dist: {distancia:.2f}")
            # print(f"  Velocidade Calculada: ({self.velocidade_x:.2f}, {self.velocidade_y:.2f})")
            # -----------------------------------------------------------------------------

        # Movimenta o osso se ele foi atirado
        if self.atirar:
            if self.rato6.rect.x - canguru.rect.x <= 200:
                self.x += self.velocidade_x -5
                self.y += self.velocidade_y -5
                self.rect.center = (int(self.x), int(self.y))

            else:
                # Atualiza a posição X e Y com base nas componentes de velocidade calculadas
                self.x += self.velocidade_x - 2
                self.y += self.velocidade_y - 5
                self.rect.center = (int(self.x), int(self.y))

            # --- DEBUG: Imprimir posição atual do osso (descomente se precisar) ---
            # print(f"  Osso em movimento: ({self.x:.2f}, {self.y:.2f})")
            # ---------------------------------------------------------------------

            # Condição de reset (ex: saiu da tela)
            # Considerar adicionar mais condições (sair pela direita, por cima, por baixo)
            # Exemplo: if self.rect.right < 0 or self.rect.left > LARGURA_TELA or self.rect.bottom < 0 or self.rect.top > ALTURA_TELA:
            if self.rect.right < 0:  # Mantendo sua condição original por enquanto

                self.contador_osso = 0  # Reinicia a animação
                # Reposiciona fora da tela para evitar colisões indesejadas até o próximo tiro
                self.rect.center = (-100, -100)
                self.x, self.y = self.rect.center
                # print("Osso resetado.") # Debug
            if self.rato6.rect.x <= -10:
                self.atirar = False



    def Colisao(self):
        osso_hitbox = pygame.Rect(self.rect.x + 55, self.rect.y + 70, 40, 30)
        #pygame.draw.rect(tela, (250, 105, 180), osso_hitbox, 2)
        canguru_hitbox = canguru.Colisao()

        for hitbox in canguru_hitbox:
            if osso_hitbox.colliderect(hitbox):
                #print("COLIDIU COM O Osso!")
                if canguru.contador_colisao == 0:
                    vidas_rosto.dano = True
                    vidas_numeros.dano = True
                    canguru.contador_colisao = 1

    def update(self):
        self.osso_on()
        self.Colisao()

#------------Cenario-----------#
class Nuvem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.spawn = True
        self.x = randint(800,1200)
        self.y = randint(0,45)
        self.velocidade = -1
        self.movimento = []
        self.movimento.append([self.x, self.y])

    def Sprites(self):
        if self.spawn:
            self.sorteio = [0, 1, 2,3]
            self.sorteado = choice(self.sorteio)
            self.nuvem = []
            imagem_nuvem = carroca_nuvem.subsurface((self.sorteado * 600, 0), (600, 300))
            imagem_nuvem = pygame.transform.scale(imagem_nuvem, (600 / 4, 300 / 4))
            self.nuvem.append(imagem_nuvem)
            self.image = self.nuvem[0]
            self.spawn = False

    #def Dificuldade(self):
        #if leveis.lvl_0:
            #self.velocidade = -1


    def Animar(self):
        for i in self.movimento[:]:
            i[0] += self.velocidade

            if i[0] <= -200:
                self.movimento.remove(i)
                self.spawn = True
                self.sorteado = choice(self.sorteio)
                self.x = randint(800, 1200)
                self.y = randint(0,45)
                self.movimento.append([self.x, self.y])



    def update(self):
        if canguru.morreu or leveis.fim_velocidade:
            self.velocidade = -0.2
        if self.spawn:
            self.Sprites()
        #self.Dificuldade()
        self.Animar()

        for i in self.movimento:
            self.rect = self.image.get_rect()
            self.rect.topright = i[0], i[1]
            tela.blit(self.image, self.rect)

        if leveis.boss or leveis.fim:
            self.velocidade *= 0.98
            if self.velocidade > -0.20:
                self.velocidade = -0.1
        else:
            self.velocidade = -1
class Nuvem2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.spawn = True
        self.x = randint(800,1200)
        self.y = randint(55,130)
        self.velocidade = -1
        self.movimento = []
        self.movimento.append([self.x, self.y])

    def Sprites(self):
        if self.spawn:
            self.sorteio = [0, 1, 2,3]
            self.sorteado = choice(self.sorteio)
            self.nuvem = []
            imagem_nuvem = carroca_nuvem.subsurface((self.sorteado * 600, 0), (600, 300))
            imagem_nuvem = pygame.transform.scale(imagem_nuvem, (600 / 4, 300 / 4))
            self.nuvem.append(imagem_nuvem)
            self.image = self.nuvem[0]
            self.spawn = False

    def Animar(self):
        for i in self.movimento[:]:
            i[0] += self.velocidade

            if i[0] <= -200:
                self.movimento.remove(i)
                self.spawn = True
                self.sorteado = choice(self.sorteio)
                self.x = randint(900, 1000)
                self.y = randint(55, 130)
                self.movimento.append([self.x, self.y])

    def update(self):
        if canguru.morreu or leveis.fim_velocidade:
            self.velocidade = -0.2
        if self.spawn:
            self.Sprites()
        self.Animar()

        for i in self.movimento:
            self.rect = self.image.get_rect()
            self.rect.topright = i[0], i[1]
            tela.blit(self.image, self.rect)

        if leveis.boss or leveis.fim:
            self.velocidade *= 0.98

            if self.velocidade > -0.20:
                self.velocidade = -0.1
        else:
            self.velocidade = -1
class Nuvem3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.spawn = True
        self.x = randint(800,1200)
        self.y = randint(150,250)
        self.velocidade = -1
        self.movimento = []
        self.movimento.append([self.x, self.y])

    def Sprites(self):
        if self.spawn:
            self.sorteio = [0, 1, 2,3]
            self.sorteado = choice(self.sorteio)
            self.nuvem = []
            imagem_nuvem = carroca_nuvem.subsurface((self.sorteado * 600, 0), (600, 300))
            imagem_nuvem = pygame.transform.scale(imagem_nuvem, (600 / 4, 300 / 4))
            self.nuvem.append(imagem_nuvem)
            self.image = self.nuvem[0]
            self.spawn = False

    def Animar(self):
        for i in self.movimento[:]:
            i[0] += self.velocidade

            if i[0] <= -200:
                self.movimento.remove(i)
                self.spawn = True
                self.sorteado = choice(self.sorteio)
                self.x = randint(900, 1200)
                self.y = randint(150, 200)
                self.movimento.append([self.x, self.y])

    def update(self):
        if canguru.morreu or leveis.fim_velocidade:
            self.velocidade = -0.2

        if self.spawn:
            self.Sprites()
        self.Animar()

        for i in self.movimento:
            self.rect = self.image.get_rect()
            self.rect.topright = i[0], i[1]
            tela.blit(self.image, self.rect)

        if leveis.boss or leveis.fim:
            self.velocidade *= 0.98

            if self.velocidade > -0.20:
                self.velocidade = -0.1
        else:
            self.velocidade = -1
class Nuvem4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.spawn = True
        self.x = randint(1400,1600 )
        self.y = randint(150, 250)
        self.velocidade = -1
        self.movimento = []
        self.movimento.append([self.x, self.y])

    def Sprites(self):
        if self.spawn:
            self.sorteio = [0, 1, 2, 3]
            self.sorteado = choice(self.sorteio)
            self.nuvem = []
            imagem_nuvem = carroca_nuvem.subsurface((self.sorteado * 600, 0), (600, 300))
            imagem_nuvem = pygame.transform.scale(imagem_nuvem, (600 / 4, 300 / 4))
            self.nuvem.append(imagem_nuvem)
            self.image = self.nuvem[0]
            self.spawn = False

    def Animar(self):
        for i in self.movimento[:]:
            i[0] += self.velocidade

            if i[0] <= -200:
                self.movimento.remove(i)
                self.spawn = True
                self.sorteado = choice(self.sorteio)
                self.x = randint(900, 1200)
                self.y = randint(150, 200)
                self.movimento.append([self.x, self.y])

    def update(self):
        if canguru.morreu or leveis.fim_velocidade:
            self.velocidade = -0.2

        if self.spawn:
            self.Sprites()
        self.Animar()

        for i in self.movimento:
            self.rect = self.image.get_rect()
            self.rect.topright = i[0], i[1]
            tela.blit(self.image, self.rect)

        if leveis.boss or leveis.fim:
            self.velocidade *= 0.98

            if self.velocidade > -0.20:
                self.velocidade = -0.1
        else:
            self.velocidade = -1
class Nuvem5(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.spawn = True
        self.x = randint(1400,1600 )
        self.y = randint(150, 250)
        self.velocidade = -1
        self.movimento = []
        self.movimento.append([self.x, self.y])

    def Sprites(self):
        if self.spawn:
            self.sorteio = [0, 1, 2, 3]
            self.sorteado = choice(self.sorteio)
            self.nuvem = []
            imagem_nuvem = carroca_nuvem.subsurface((self.sorteado * 600, 0), (600, 300))
            imagem_nuvem = pygame.transform.scale(imagem_nuvem, (600 / 4, 300 / 4))
            self.nuvem.append(imagem_nuvem)
            self.image = self.nuvem[0]
            self.spawn = False

    def Animar(self):
        for i in self.movimento[:]:
            i[0] += self.velocidade

            if i[0] <= -200:
                self.movimento.remove(i)
                self.spawn = True
                self.sorteado = choice(self.sorteio)
                self.x = randint(900, 1200)
                self.y = randint(150, 200)
                self.movimento.append([self.x, self.y])

    def update(self):
        if canguru.morreu or leveis.fim_velocidade:
            self.velocidade = -0.2

        if self.spawn:
            self.Sprites()
        self.Animar()

        for i in self.movimento:
            self.rect = self.image.get_rect()
            self.rect.topright = i[0], i[1]
            tela.blit(self.image, self.rect)

        if leveis.boss or leveis.fim:
            self.velocidade *= 0.98

            if self.velocidade > -0.20:
                self.velocidade = -0.1
        else:
            self.velocidade = -1

class Montanha(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.contador = 0
        self.velocidade = -0.5
        self.Sprites()


    def Sprites(self):
        if self.contador == 0:
            self.x = 320
            self.y = 235
            self.montanha = carroca_montanha2
            self.montanha = pygame.transform.scale(self.montanha, (1500 / 2, 600 / 2))

        elif self.contador == 1:
            self.x = 1100
            self.y = 185
            self.montanha = carroca_montanha1
            self.montanha = pygame.transform.scale(self.montanha, (1000, 500))


        self.image = self.montanha
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)

    def update(self):
        if canguru.morreu or leveis.fim_velocidade:
            self.velocidade = 0

        if self.x <= -450:
            if self.contador == 0:
                self.contador +=1
                self.Sprites()
            elif self.contador == 1:
                self.contador = 0
                self.Sprites()
                self.x = 1000

        self.image = self.montanha
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.x += self.velocidade

        if leveis.boss or leveis.fim:
            self.velocidade *= 0.98

            if self.velocidade > -0.10:
                self.velocidade = 0
        else:
            self.velocidade = -0.5
class Montanhas(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.spawn = True
        self.velocidade = -0.5
        self.x = -200


    def Sprites(self):
        self.y = 250
        self.sorteado = choice([0,1,2,3,4])
        self.sorteio2 = [x for x in [0, 1, 2, 3] if x != self.sorteado]
        self.montanhas = []

        imagem_montanhas = carroca_montanhas.subsurface((self.sorteado * 1536, 0), (1536, 1024))
        imagem_montanhas = pygame.transform.scale(imagem_montanhas, (1536 / 6, 1024 / 6))
        self.montanhas.append(imagem_montanhas)
        self.image = self.montanhas[0]
        self.spawn = False
        self.movimento = []
        self.movimento.append([self.x, self.y])

    def Animar(self):
        for i in self.movimento[:]:
            i[0] += self.velocidade

            if self.spawn == True:
                self.movimento.remove(i)



    def update(self):
        if canguru.morreu or leveis.fim_velocidade:
            self.velocidade = 0

        if montanha.x <= 200 and montanha.x >= 195:
            self.spawn = True
            self.x = 900
        if self.spawn:
            self.Sprites()


        self.Animar()

        for i in self.movimento:
            self.rect = self.image.get_rect()
            self.rect.topright = i[0], i[1]
            tela.blit(self.image, self.rect)

        if leveis.boss or leveis.fim:
            self.velocidade *= 0.98

            if self.velocidade > -0.10:
                self.velocidade = 0
        else:
            self.velocidade = -0.5
class Montanhas2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.numeros = [0, 1, 2]
        self.spawn = True
        self.velocidade = -0.5
        self.x = -200

    def Sprites(self):
        self.y = 250

        self.sorteado = choice(montanhas.sorteio2)

        self.montanhas = []

        imagem_montanhas = carroca_montanhas.subsurface((self.sorteado * 1536, 0), (1536, 1024))
        imagem_montanhas = pygame.transform.scale(imagem_montanhas, (1536 / 6, 1024 / 6))
        self.montanhas.append(imagem_montanhas)
        self.image = self.montanhas[0]
        self.spawn = False
        self.movimento = []
        self.movimento.append([self.x, self.y])

    def Animar(self):
        for i in self.movimento[:]:
            i[0] += self.velocidade

            if self.spawn == True:
                self.movimento.remove(i)

    def update(self):
        if canguru.morreu or leveis.fim_velocidade:
            self.velocidade = 0

        if montanha.x <= -150 and montanha.x >= -155:
            self.spawn = True
            self.x = 900
        if self.spawn:
            self.Sprites()

        self.Animar()

        for i in self.movimento:
            self.rect = self.image.get_rect()
            self.rect.topright = i[0], i[1]
            tela.blit(self.image, self.rect)

        if leveis.boss or leveis.fim:
            self.velocidade *= 0.98

            if self.velocidade > -0.10:
                self.velocidade = 0

        else:
            self.velocidade = -0.5

class Elementos(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.numeros = [2] #outros numeros estao nos outros elementos
        self.cenario = choice (self.numeros)
        self.spawn = True
        self.x = 900
        self.velocidade = -2
        self.contador_frames_reducao = 0



    def Sprites(self):

        if self.spawn and self.cenario == 2:

            self.sorteio = [1]
            self.sorteado = choice(self.sorteio)
            self.ossos = []
            imagem_osso = carroca_osso.subsurface((self.sorteado * 300, 0), (300, 300))

            if self.sorteado == 1: #260,270 = /2
                lugares_osso =[335,340,345]
                self.y = choice(lugares_osso)
                if self.y == 345:
                    imagem_osso = pygame.transform.scale(imagem_osso, (300 /4.5, 300 /4.5))
                elif self.y == 335:
                    imagem_osso = pygame.transform.scale(imagem_osso, (300 / 6.5, 300 / 6.5))
                elif self.y == 340:
                    imagem_osso = pygame.transform.scale(imagem_osso, (300 /4, 300 /4))

                self.ossos.append(imagem_osso)
            self.image = self.ossos[0]
            self.spawn = False
            self.movimento = []
            self.movimento.append([self.x, self.y])

    def Animar (self):
        for i in self.movimento[:]:
            i[0] += self.velocidade

            if i[0] <= -500:
                self.movimento.remove(i)
                self.cenario = choice(self.numeros)
                self.spawn = True
                self.sorteado = choice(self.sorteio)
                self.y = choice ([335,340,345])
                self.movimento.append([self.x, self.y])

    def update(self):
        #print (self.cenario)
        if canguru.morreu or leveis.fim_velocidade:
            self.velocidade = 0
        if self.spawn:
            self.Sprites()
        self.Animar()

        for i in self.movimento:
            self.rect = self.image.get_rect()
            self.rect.topright = i[0], i[1]
            tela.blit(self.image, self.rect)




        if leveis.boss or leveis.fim:
            self.velocidade *= 0.98

            # Incrementa o contador para a redução (opcional, pode usar outra lógica)
            self.contador_frames_reducao += 1

            if self.velocidade > -0.30:
                self.velocidade = 0

        else:
            self.velocidade = -2
class Elementos2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.numeros = [0,1]
        self.cenario = choice(self.numeros)
        self.spawn = True
        self.x = 1200
        self.velocidade = -2
        self.contador_frames_reducao = 0

    def get_layer(self):
        # Define a camada de desenho com base no Y
        return 4.7 if self.cenario == 0 and self.y == 360 else 4

    def Sprites(self):
        if self.spawn and self.cenario == 0:
            self.y = choice([315,330,360])
            self.sorteio = [1]
            self.sorteado = choice(self.sorteio)
            self.areias = []
            imagem_areia = carroca_areia.subsurface((self.sorteado * 800, 0), (800, 200))
            imagem_areia = pygame.transform.scale(imagem_areia, (800 / 4, 200 / 4))
            self.areias.append(imagem_areia)
            self.image = self.areias[0]
            self.spawn = False
            self.movimento = []
            self.movimento.append([self.x, self.y])

        if self.spawn and self.cenario == 1:
            self.y = randint(225, 225) #216,270
            self.sorteio = [1]
            self.sorteado = choice(self.sorteio)
            self.cactos = []
            imagem_cacto = carroca_cacto.subsurface((self.sorteado * 1536, 0), (1536, 1024))
            imagem_cacto = pygame.transform.scale(imagem_cacto, (1536 / 6, 1024 / 6))
            self.cactos.append(imagem_cacto)
            self.image = self.cactos[0]
            self.spawn = False
            self.movimento = []
            self.movimento.append([self.x, self.y])


            self.spawn = False
            self.movimento = []
            self.movimento.append([self.x, self.y])

    def Animar(self):
        for i in self.movimento[:]:
            i[0] += self.velocidade

            if i[0] <= -300:
                self.movimento.remove(i)
                self.cenario = choice(self.numeros)
                self.spawn = True
                self.sorteado = choice(self.sorteio)
                if self.cenario == 0:
                    self.y = choice([315,330,360])
                else:
                    self.y = randint(225, 225)
                self.movimento.append([self.x, self.y])

    def update(self):
        if canguru.morreu or leveis.fim_velocidade:
            self.velocidade = 0
        if self.spawn:
            self.Sprites()
        self.Animar()

        grupos = self.groups()
        if grupos:
            grupo = grupos[0]
            grupo.change_layer(self, self.get_layer())

        for i in self.movimento:
            self.rect = self.image.get_rect()
            self.rect.topright = i[0], i[1]
            tela.blit(self.image, self.rect)

        if leveis.boss or leveis.fim:
            self.velocidade *= 0.98

            # Incrementa o contador para a redução (opcional, pode usar outra lógica)
            self.contador_frames_reducao += 1

            if self.velocidade > -0.30:
                self.velocidade = 0
        else:
            self.velocidade = -2
class Elementos3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.numeros = [0,1,2]
        self.cenario = choice(self.numeros)
        self.spawn = True
        self.x = 1500
        self.velocidade = -2
        self.contador_frames_reducao = 0

    def Sprites(self):
        if self.spawn and self.cenario == 0:
            self.y = randint(310, 364)
            self.sorteio = [2]
            self.sorteado = choice(self.sorteio)
            self.areias = []
            imagem_areia = carroca_areia.subsurface((self.sorteado * 800, 0), (800, 200))
            imagem_areia = pygame.transform.scale(imagem_areia, (800 / 4, 200 / 4))
            self.areias.append(imagem_areia)
            self.image = self.areias[0]
            self.spawn = False
            self.movimento = []
            self.movimento.append([self.x, self.y])

        if self.spawn and self.cenario == 1:
            self.y = randint(216, 270)
            self.sorteio = [2]
            self.sorteado = choice(self.sorteio)
            self.cactos = []
            imagem_cacto = carroca_cacto.subsurface((self.sorteado * 1536, 0), (1536, 1024))
            imagem_cacto = pygame.transform.scale(imagem_cacto, (1536 / 6, 1024 / 6))
            self.cactos.append(imagem_cacto)
            self.image = self.cactos[0]
            self.spawn = False
            self.movimento = []
            self.movimento.append([self.x, self.y])

        if self.spawn and self.cenario == 2:

            self.sorteio = [0]
            self.sorteado = choice(self.sorteio)
            self.ossos = []
            imagem_osso = carroca_osso.subsurface((self.sorteado * 300, 0), (300, 300))

            if self.sorteado == 0:

                lugares_osso = [330]
                self.y = choice(lugares_osso)
                if self.y == 325:
                    imagem_osso = pygame.transform.scale(imagem_osso, (300 / 6.5, 300 / 6.5))
                elif self.y == 330:
                    imagem_osso = pygame.transform.scale(imagem_osso, (300 / 5, 300 / 5))
                elif self.y == 340:
                    imagem_osso = pygame.transform.scale(imagem_osso, (300 / 4, 300 / 4))

                self.ossos.append(imagem_osso)

            elif self.sorteado == 1:  # 260,270 = /2
                lugares_osso = [265, 270, 275, 280, 290]
                self.y = choice(lugares_osso)
                if self.y in (265, 270):
                    imagem_osso = pygame.transform.scale(imagem_osso, (300 / 2, 300 / 2))
                elif self.y in (275, 280):
                    imagem_osso = pygame.transform.scale(imagem_osso, (300 / 2.5, 300 / 2.5))
                elif self.y == 290:
                    imagem_osso = pygame.transform.scale(imagem_osso, (300 / 3, 300 / 3))

                self.ossos.append(imagem_osso)
            self.image = self.ossos[0]
            self.spawn = False
            self.movimento = []
            self.movimento.append([self.x, self.y])

    def Animar(self):
        for i in self.movimento[:]:
            i[0] += self.velocidade

            if i[0] <= -100:
                self.movimento.remove(i)
                self.cenario = choice(self.numeros)
                self.spawn = True
                self.sorteado = choice(self.sorteio)
                self.y = randint(310, 364)
                self.movimento.append([self.x, self.y])

    def update(self):
        if canguru.morreu or leveis.fim_velocidade:
            self.velocidade = 0
        if self.spawn:
            self.Sprites()
        self.Animar()

        for i in self.movimento:
            self.rect = self.image.get_rect()
            self.rect.topright = i[0], i[1]
            tela.blit(self.image, self.rect)

        if leveis.boss or leveis.fim:
            self.velocidade *= 0.98

            # Incrementa o contador para a redução (opcional, pode usar outra lógica)
            self.contador_frames_reducao += 1

            if self.velocidade > -0.30:
                self.velocidade = 0
        else:
            self.velocidade = -2

class Grama(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.numeros = [0,1,2]
        self.cenario = choice(self.numeros)
        self.spawn = True
        self.x = 200
        self.velocidade = -2

    def Sprites(self):

        self.y = randint(315, 320)
        self.sorteio = [3,4,5]
        self.sorteado = choice(self.sorteio)
        self.gramas = []
        imagem_grama = carroca_grama.subsurface((self.sorteado * 600, 0), (600, 600))
        imagem_grama = pygame.transform.scale(imagem_grama, (600 / 6, 600 / 6))
        self.gramas.append(imagem_grama)
        self.image = self.gramas[0]
        self.spawn = False
        self.movimento = []
        self.movimento.append([self.x, self.y])

    def Animar(self):
        for i in self.movimento[:]:
            i[0] += self.velocidade

            if i[0] <= -100:
                self.movimento.remove(i)
                self.cenario = choice(self.numeros)
                self.spawn = True
                self.sorteado = choice(self.sorteio)
                self.x = 900
                self.y = randint(315, 320)
                self.movimento.append([self.x, self.y])

    def update(self):
        if canguru.morreu or leveis.fim_velocidade:
            self.velocidade = 0
        if self.spawn:
            self.Sprites()
        self.Animar()

        for i in self.movimento:
            self.rect = self.image.get_rect()
            self.rect.topright = i[0], i[1]
            tela.blit(self.image, self.rect)

        if leveis.boss or leveis.fim:
            self.velocidade *= 0.98

            if self.velocidade > -0.30:
                self.velocidade = 0
        else:
            self.velocidade = -2
class Grama2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.numeros = [0,1,2]
        self.cenario = choice(self.numeros)
        self.spawn = True
        self.x = 500
        self.velocidade = -2

    def Sprites(self):

        self.y = randint(315, 320)
        self.sorteio = [0,1,2]
        self.sorteado = choice(self.sorteio)
        self.gramas = []
        imagem_grama = carroca_grama.subsurface((self.sorteado * 600, 0), (600, 600))
        imagem_grama = pygame.transform.scale(imagem_grama, (600 / 6, 600 / 6))
        self.gramas.append(imagem_grama)
        self.image = self.gramas[0]
        self.spawn = False
        self.movimento = []
        self.movimento.append([self.x, self.y])

    def Animar(self):
        for i in self.movimento[:]:
            i[0] += self.velocidade

            if i[0] <= -100:
                self.movimento.remove(i)
                self.cenario = choice(self.numeros)
                self.spawn = True
                self.sorteado = choice(self.sorteio)
                self.x = 1200
                self.y = randint(315, 320)
                self.movimento.append([self.x, self.y])

    def update(self):
        if canguru.morreu or leveis.fim_velocidade:
            self.velocidade = 0
        if self.spawn:
            self.Sprites()
        self.Animar()

        for i in self.movimento:
            self.rect = self.image.get_rect()
            self.rect.topright = i[0], i[1]
            tela.blit(self.image, self.rect)

        if leveis.boss or leveis.fim:
            self.velocidade *= 0.98

            if self.velocidade > -0.30:
                self.velocidade = 0

        else:
            self.velocidade = -2
class Grama3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.numeros = [0,1,2,3,4,5]
        self.cenario = choice(self.numeros)
        self.spawn = True
        self.x = 900
        self.velocidade = -2

    def Sprites(self):

        self.y = randint(315, 320)
        self.sorteio = [0,1,2]
        self.sorteado = choice(self.sorteio)
        self.gramas = []
        imagem_grama = carroca_grama.subsurface((self.sorteado * 600, 0), (600, 600))
        imagem_grama = pygame.transform.scale(imagem_grama, (600 / 6, 600 / 6))
        self.gramas.append(imagem_grama)
        self.image = self.gramas[0]
        self.spawn = False
        self.movimento = []
        self.movimento.append([self.x, self.y])

    def Animar(self):
        for i in self.movimento[:]:
            i[0] += self.velocidade

            if i[0] <= -100:
                self.movimento.remove(i)
                self.cenario = choice(self.numeros)
                self.spawn = True
                self.sorteado = choice(self.sorteio)
                self.x = 1400
                self.y = randint(315, 320)
                self.movimento.append([self.x, self.y])

    def update(self):
        if canguru.morreu or leveis.fim_velocidade:
            self.velocidade = 0
        if self.spawn:
            self.Sprites()
        self.Animar()

        for i in self.movimento:
            self.rect = self.image.get_rect()
            self.rect.topright = i[0], i[1]
            tela.blit(self.image, self.rect)

        if leveis.boss or leveis.fim:
            self.velocidade *= 0.98

            if self.velocidade > -0.30:
                self.velocidade = 0

        else:
            self.velocidade = -2

class Tufo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.contador_liberar = 0
        self.atual_tufo = 0
        self.velocidade = 4
        self.x = 700
        self.y = choice([320, 350])
        self.spawn = False
        self.contador = True
        self.movimento = [[self.x, self.y]]

        self.Sprites()

    def get_layer(self):
        # Define a camada de desenho com base no Y
        return 2.9 if self.y == 320 else 4.7

    def Sprites(self):
        self.tufo = []
        for i in range(5):
            imagem_tufo = carroca_tufo.subsurface((i * 1536, 0), (1536, 1024))
            if self.y == 350:
                imagem_tufo = pygame.transform.scale(imagem_tufo, (1536 // 15, 1024 // 15))
            elif self.y == 320:
                imagem_tufo = pygame.transform.scale(imagem_tufo, (1536 // 20, 1024 // 20))
            self.tufo.append(imagem_tufo)

        self.image = self.tufo[0]
        self.rect = self.image.get_rect()
        self.rect.topright = 0, 0

    def Animar(self):
        self.contador = False
        self.image = self.tufo[int(self.atual_tufo)]
        self.atual_tufo += 0.20
        if self.atual_tufo >= len(self.tufo):
            self.atual_tufo = 0

        for i in self.movimento:
            i[0] -= self.velocidade
            self.rect = self.image.get_rect()
            self.rect.topright = i[0], i[1]
            tela.blit(self.image, self.rect)

            if i[0] <= -1:
                self.movimento.remove(i)
                self.x = 700
                self.y = choice([320, 350])
                self.movimento.append([self.x, self.y])
                self.Sprites()  #Redimensiona com base no novo Y
                self.contador = True
                self.spawn = False
                grupos = self.groups()
                if grupos:
                    grupo = grupos[0]
                    grupo.change_layer(self, self.get_layer())

    def update(self):
        if self.contador:
            self.contador_liberar += 1
            if self.contador_liberar >= 100:
                self.sorteio = randint(0,400)
                if self.sorteio == 1:
                    self.spawn = True
        if self.spawn:
            self.Animar()
        grupos = self.groups()
        if grupos:
            grupo = grupos[0]
            grupo.change_layer(self, self.get_layer())
        if leveis.boss or leveis.fim:
            self.velocidade *= 0.98

            if self.velocidade < 1: #2
                self.velocidade = 1 #2
        else:
            self.velocidade = 4 #3

class Chao(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 183
        self.y = 418
        self.velocidade = -1
        self.contador_frames_reducao = 0


        self.chao = carroca_chao
        self.chao = pygame.transform.scale(self.chao, (1469/4,1024/4))

        self.image = self.chao
        self.movimento = [[self.x, self.y]]  # apenas uma lista com a posição

        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y

    def Animar(self):
        for i in self.movimento[:]:
            i[0] += self.velocidade
            if i[0] <= -184:
                self.x = 914
                self.y = 420
                self.image = self.chao
                self.movimento = [[self.x, self.y]]


    def update(self):
        if canguru.morreu or leveis.fim_velocidade:
            self.velocidade = 0
        self.Animar()

        if leveis.boss or leveis.fim:
            self.velocidade *= 0.98


            # Incrementa o contador para a redução (opcional, pode usar outra lógica)
            self.contador_frames_reducao += 1

            if self.velocidade > -0.10:
                self.velocidade = 0
        else:
            self.velocidade = -1



        for i in self.movimento:
            self.rect = self.image.get_rect()
            self.rect.center = i[0], i[1]
            tela.blit(self.image, self.rect)
class Chao2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 550
        self.y = 418
        self.velocidade = -1
        self.contador_frames_reducao = 0


        self.chao = carroca_chao
        self.chao = pygame.transform.scale(self.chao, (1469/4,1024/4))

        self.image = self.chao
        self.movimento = [[self.x, self.y]]  # apenas uma lista com a posição

        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y

    def Animar(self):
        for i in self.movimento[:]:
            i[0] += self.velocidade
            if i[0] <= -184:
                self.x = 914
                self.y = 420
                self.image = self.chao
                self.movimento = [[self.x, self.y]]


    def update(self):
        if canguru.morreu or leveis.fim_velocidade:
            self.velocidade = 0
        self.Animar()

        if leveis.boss or leveis.fim:
            self.velocidade *= 0.98

            # Incrementa o contador para a redução (opcional, pode usar outra lógica)
            self.contador_frames_reducao += 1

            if self.velocidade > -0.10:
                self.velocidade = 0

        else:
            self.velocidade = -1


        for i in self.movimento:
            self.rect = self.image.get_rect()
            self.rect.center = i[0], i[1]
            tela.blit(self.image, self.rect)
class Chao3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 914
        self.y = 418
        self.velocidade = -1
        self.contador_frames_reducao =0

        self.chao = carroca_chao
        self.chao = pygame.transform.scale(self.chao, (1469/4,1024/4))

        self.image = self.chao
        self.movimento = [[self.x, self.y]]  # apenas uma lista com a posição

        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y

    def Animar(self):
        for i in self.movimento[:]:
            i[0] += self.velocidade
            if i[0] <= -184:
                self.x = 914
                self.y = 420
                self.image = self.chao
                self.movimento = [[self.x, self.y]]




    def update(self):

        if canguru.morreu or leveis.fim_velocidade:
            self.velocidade = 0
        self.Animar()

        if leveis.boss or leveis.fim:
            self.velocidade *= 0.98


            # Incrementa o contador para a redução (opcional, pode usar outra lógica)
            self.contador_frames_reducao += 1

            if self.velocidade > -0.10:
                self.velocidade = 0

        else:
            self.velocidade = -1

        for i in self.movimento:
            self.rect = self.image.get_rect()
            self.rect.center = i[0], i[1]
            tela.blit(self.image, self.rect)

class Dia(pygame.sprite.Sprite):
    def __init__(self, noite,lua):
        pygame.sprite.Sprite.__init__(self)
        self.reset = False
        self.noite = noite
        self.x = 300
        self.y = 230
        self.velocidade = 0
        self.fase1 = carroca_dia
        self.fase1 = pygame.transform.scale(self.fase1, (1536 / 2, 1024 / 2))
        self.image = self.fase1
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)


    def update(self):
        if lua.amanheceu:
            self.velocidade = 10
            if self.y == 230:
                self.velocidade = 0

        elif sol.anoiteceu:
            self.velocidade = 10
            if self.y >= 650:
                self.velocidade = 0
                self.y = -160
                sol.anoiteceu = False #virou noite

        self.y += self.velocidade
        self.image = self.fase1
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
class Noite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.chao = False

        self.x = 300
        self.y = -160
        self.velocidade = 0
        self.noite = carroca_noite
        self.noite = pygame.transform.scale(self.noite, (1536 / 2, 1024 / 2))
        self.image = self.noite
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)


    def update(self):


        if sol.anoiteceu:
            self.velocidade = 10
            if self.y == 230:
                self.velocidade = 0

        elif lua.amanheceu:
            self.velocidade = 10
            if self.y >= 650:
                self.velocidade = 0
                self.y = -160
                lua.amanheceu = False #virou noite
        self.y += self.velocidade
        self.image = self.noite
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
class Chaodia(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.saiu = False
        self.entrou = False
        self.fundo = True
        self.x = 300
        self.y = 230
        self.velocidade = 10
        self.fase1 = carroca_chao_dia
        self.fase1 = pygame.transform.scale(self.fase1, (1536 / 2.2, 1024 / 2.2))
        self.image = self.fase1
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def get_layer(self):
        # Define a camada de desenho com base no Y
        return 1 if self.fundo else 2.1
#for entrrar, camada 1
    def update(self):
#se for amanhecer, dia camada baixo
        if dia.y >= 100:
            self.velocidade = 10
            self.y -= self.velocidade
            if self.y > 230:
                self.velocidade = 10
                self.y -= self.velocidade
            else:
                self.y = 230
                self.velocidade = 0




        elif noite.y == 230:

            self.velocidade = 10
            self.y += self.velocidade
            if self.y >= 460:
                self.y = 460
                self.fundo = True
                chaonoite.fundo = False



        grupos = self.groups()
        if grupos:
            grupo = grupos[0]
            grupo.change_layer(self, self.get_layer())
        self.image = self.fase1
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
class Chaonoite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.saiu = False
        self.manha = True
        self.noite = False
        self.fundo = False
        self.entrou = False
        self.escureceu = False
        self.x = 300
        self.y = 460
        self.velocidade = 10
        self.fase1 = carroca_chao_noite
        self.fase1 = pygame.transform.scale(self.fase1, (1536 / 2.2, 1024 / 2.2))
        self.image = self.fase1
        self.rect = self.image.get_rect()
        self.rect.center = (-1000, -1000)

    def get_layer(self):
        return 0.9

    def update(self):

        if noite.y >= 100:
            self.velocidade = 10
            self.y -= self.velocidade
            if self.y > 230:
                self.velocidade = 10
                self.y -= self.velocidade
            else:
                self.y = 230
                self.velocidade = 0


        elif dia.y == 230:
            self.velocidade = 10
            self.y += self.velocidade
            if self.y >= 460:
                self.y = 460
                self.saiu = True
                self.fundo= True
                chaodia.fundo = False

        self.image = self.fase1
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

class Sol(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.anoiteceu = False
        self.reset = False
        self.x = 550
        self.y = -70
        self.velocidade = 0
        self.sol = carroca_sol
        self.sol = pygame.transform.scale(self.sol, (1024/6,1024/6))
        self.image = self.sol
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)

    def update(self):
        if dia.y >= 230 and not self.anoiteceu:
            self.velocidade = 0.05

        if self.y >= 450:
            self.anoiteceu = True
            self.velocidade =0
            self.y = -70  # Volta para o topo

        self.y += self.velocidade
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
class Lua(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.amanheceu = False
        self.x = 100
        self.y = -65
        self.velocidade = 0
        self.lua = carroca_lua
        self.lua = pygame.transform.scale(self.lua, (1024/6,1024/6))
        self.image = self.lua
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)

    def update(self):
        if noite.y >= 230 and not self.amanheceu:
            self.velocidade = 0.05
        if self.y >= 450:
            self.amanheceu = True
            self.velocidade = 0
            self.y = -65  # Volta para o topo

        self.y += self.velocidade
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

#classes----------------------------
menu = Menu()
kangaruun = Kangaruun()
play = Play()
shop = Shop()
exit = Exit()
settings = Settings()
new_game = New_game()
continue_menu = Continue_menu()
lvl = Lvl()
tutorial = Tutorial()
back_play = Back_play()
tutorial_menu = Tutorial_Menu()
paginas_tutorial = Paginas_Tutorial()

cursor = Cursor()
efeitos_menu = Efeito_menu()

leveis = Leveis()
progresso = Progress()
progresso_marca = Progress_brand()
progresso_marca2 = Progress_brand2()

#-------------Peronsagens-----------------#
canguru = Canguru()
vidas_rosto = Vidas_rosto()
vidas_numeros = Vidas_numeros()
dano = Dano_canguru_Sprite()
bumerangue = Bumerangue(canguru)
colisao = Colisao()
canguru.bumerangue = bumerangue
#-----------------Itens-------------------#
mochila = Mochila()
item_vida = Item_vida()
#------------------Boss------------------#
tasmania = Miniboss()
machado = Machado()
machado2 = Machado2()
machado3 = Machado3()
machado4 = Machado4()
machado5 = Machado5()
machado6 = Machado6()
seta = Seta()
marcador_boss = Marcador_boss()
#----------------Inimigos----------------#
#ratos
rato = Rato()
rato2 = Rato2()
rato3 = Rato3()
rato4 = Rato4()
rato5 = Rato5()
rato6 = Rato6()
#--
osso = Osso(rato,canguru)
osso2 = Osso2(rato2,canguru)
osso3 = Osso3(rato3,canguru)
osso4 = Osso4(rato4,canguru)
osso5 = Osso5(rato5,canguru)
osso6 = Osso5(rato6,canguru)
#lagartos
lagarto = Lagarto(canguru,bumerangue)
lagarto2 = Lagarto2(canguru,bumerangue)
lagarto3 = Lagarto3(canguru,bumerangue)
lagarto4 = Lagarto4(canguru,bumerangue)
lagarto5 = Lagarto5(canguru,bumerangue)
#dingos
dingo = Dingo(bumerangue,canguru.bumerangue)
dingo2 = Dingo2(bumerangue,canguru.bumerangue)
dingo3 = Dingo3(bumerangue,canguru.bumerangue)
dingo4 = Dingo4(bumerangue,canguru.bumerangue)
dingo5 = Dingo5(bumerangue,canguru.bumerangue)
dingo6 = Dingo6(bumerangue,canguru.bumerangue)
#-----------------Menus-------------------------#
gameover = Gameover()
gameover_continue = Gameover_continue()
gameover_quit = Gameover_quit()
gameover_bumerangue = Gameover_bumerangue()
pause = Pause()
stage_clear = Stage_clear()
score = Score()
#----------------Cenario------------------------#
elementos = Elementos()
elementos2 = Elementos2()
elementos3 = Elementos3()
nuvem = Nuvem()
nuvem2 = Nuvem2()
nuvem3 = Nuvem3()
nuvem4 = Nuvem4()
nuvem5 = Nuvem5()
fase = Fases()
chao = Chao()
chao2 = Chao2()
chao3 = Chao3()
tufo = Tufo()
grama = Grama()
grama2 = Grama2()
grama3 = Grama3()
noite = Noite()
lua = Lua()
dia = Dia(noite,lua)
montanha = Montanha()
sol = Sol()
chaodia =Chaodia()
chaonoite = Chaonoite()
montanhas = Montanhas()
montanhas2=Montanhas2()
#-------------Gerenciador------------#
gerenciador = Gerenciador()
#---------junção classes--------------#
canguru.vidas_numeros = vidas_numeros
montanhas.montanha = montanha
montanhas2.montanhas = montanhas
montanhas2.montanha = montanha
dia.sol = sol
lua.sol = sol
sol.dia=dia
chaodia.dia = dia
noite.dia = dia

#grupo e camadas
game = pygame.sprite.LayeredUpdates()
game.add(noite,lua,dia,sol, layer=0)
game.add(nuvem, nuvem2, nuvem3, nuvem4, nuvem5,chaonoite,chaodia,layer=1)
game.add(montanha,montanhas,montanhas2, layer=2)
game.add(grama,grama2,grama3, layer=3)
game.add(elementos, elementos2, elementos3,chao,chao2,chao3,tufo,layer=4)
game.add(item_vida,bumerangue,layer = 5)
game.add(canguru,layer = 6.4) #5
game.add( dingo,dingo2,dingo3,dingo4,dingo5,dingo6,layer=6) #6 e 7 baixo
game.add(lagarto,lagarto2,lagarto3,lagarto4,lagarto5, layer=7) # 6 e 6.5 baixo
game.add(rato,rato2,rato3,rato4,rato5,rato6, layer=8)
game.add(osso,osso2,osso3,osso4,osso5,osso6,layer=9)
game.add(vidas_rosto,vidas_numeros,mochila,progresso_marca,progresso_marca2,layer=10)

game.add(layer=canguru.get_layer())
game.add(layer=dingo.get_layer())
game.add(layer=dingo2.get_layer())
game.add(layer=dingo3.get_layer())
game.add(layer=dingo4.get_layer())
game.add(layer=dingo5.get_layer())
game.add(layer=dingo6.get_layer())
game.add(layer=tufo.get_layer())
game.add(layer=chaodia.get_layer())
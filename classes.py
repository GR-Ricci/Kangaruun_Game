import os
from os import remove

import pygame
from pygame.locals import *
from pygame import sprite
from random import randint
from random import choice

#formação da tela
tela = pygame.display.set_mode((640,480))

# self nas classes -
# irão viver na cidade e usar de seus recursos
#tudo que for da cidade, é reutilizado, recebe self
# apenas variavel temporaria (visitantes) são livres do self, maldicao da cidade

#formação da cidade - os
cidade = os.path.dirname(__file__)
loja_sprites = os.path.join(cidade,'elementos/spritesheet')
loja_imagens = os.path.join(cidade, 'elementos/sprites')
loja_cenarios = os.path.join(cidade, 'elementos/cenario')
loja_som = os.path.join(cidade, 'elementos/som')
carroca_sprites = pygame.image.load(os.path.join(loja_imagens, 'dinoSpritesheet.png')).convert_alpha()
carroca_deserto = pygame.image.load(os.path.join(loja_cenarios, 'deserto.png')).convert_alpha()
carroca_chao = pygame.image.load(os.path.join(loja_cenarios,'chão.png')).convert_alpha()
carroca_canguru = pygame.image.load(os.path.join(loja_sprites,'canguru.png')).convert_alpha()
carroca_bumerangue = pygame.image.load(os.path.join(loja_sprites,'bumerangue.png')).convert_alpha()
carroca_lagarto = pygame.image.load(os.path.join(loja_sprites,'lagarto.png')).convert_alpha()
carroca_rato = pygame.image.load(os.path.join(loja_sprites,'rato.png')).convert_alpha()
carroca_dingo = pygame.image.load(os.path.join(loja_sprites,'dingo.png')).convert_alpha()
carroca_cenario1 = pygame.image.load(os.path.join(loja_cenarios,'fundo.png')).convert_alpha()
carroca_areia = pygame.image.load(os.path.join(loja_cenarios,'areias.png')).convert_alpha()
carroca_nuvem = pygame.image.load(os.path.join(loja_cenarios, 'nuvem.png')).convert_alpha()
carroca_cacto = pygame.image.load(os.path.join(loja_cenarios,'cactos.png')).convert_alpha()
carroca_osso = pygame.image.load(os.path.join(loja_cenarios,'osso.png')).convert_alpha()

class Leveis():

    def __init__(self):
        self.pontos = 0
        self.contador = 0
        self.fonte = pygame.font.SysFont('calibri', 20, False, False)
        self.lvl_0 = True
        self.lvl_1 = False
        self.lvl_2 = False
        self.lvl_3 = False
        self.lvl_4 = False
        self.lvl_5 = False

    def pontuacao(self):
        texto = self.fonte.render(f'PONTOS: {self.pontos}', True, (255, 0, 0))
        self.contador +=0.10
        self.pontos = int(self.contador)
        tela.blit(texto, (10, 450))

    def lvl(self):
        if self.pontos >= 10000:
            self.lvl_5 = True
            self.lvl_4 = False
        elif self.pontos >= 10000:
            self.lvl_4 = True
            self.lvl_3 = False
        elif self.pontos >= 10000:
            self.lvl_3 = True
            self.lvl_2 = False
        elif self.pontos >= 10000:
            self.lvl_2 = True
            self.lvl_1 = False
        elif self.pontos >= 10000:
            self.lvl_1 = True
            self.lvl_0 = False
        else:
            self.lvl_0 = True

    def update(self):
        self.pontuacao()
        self.lvl()

class Fases(pygame.sprite.Sprite):
    def __init__(self,pontos):
        pygame.sprite.Sprite.__init__(self)
        self.leveis = pontos
        self.fases=[]
        self.fases.append(carroca_deserto)
        self.fases_index = 0

        for i in range (len(self.fases)):
            self.image = self.fases[i]
            self.rect = self.image.get_rect()
            self.rect.center = 0,0

    def mostrar(self):
        if self.leveis.lvl_0:
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

class Canguru(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.bumerangue = None
        self.pulo_imagem = pygame.image.load('elementos/sprites/canguru/pulo.png')
        self.pulo_duplo_imagem = pygame.image.load('elementos/sprites/canguru/pulo_duplo.png')
        queda_imagem = pygame.image.load('elementos/sprites/canguru/deitado_1.png')
        self.queda_imagem = pygame.transform.scale(queda_imagem, (438, 315))

        self.canguru = []
        self.canguru_ataca = []
        self.canguru_agachado = []
        self.canguru_atacar = []

        self.atual = 0
        self.atual_ataca = 0
        self.atual_correndo = 0
        self.gravidade = 0
        self.bloquear_agachamento = False
        self.pulo = False
        self.pulo_duplo = False
        self.queda = False
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

#canguru com bumerangue

    def Sprites(self):
        self.canguru = []
        self.canguru.append(carroca_canguru.subsurface((0 * 287, 0), (287, 316))),
        self.canguru.append(carroca_canguru.subsurface((3 * 287, 0), (287, 316)))

        self.canguru_ataca = []
        self.canguru_ataca.append(carroca_canguru.subsurface((4 * 287, 0), (287, 316)))
        self.canguru_ataca.append(carroca_canguru.subsurface((1 * 287, 0), (287, 316)))

        self.canguru_agachado = [pygame.image.load('elementos/sprites/canguru/deitado_1.png'),
                                 pygame.image.load('elementos/sprites/canguru/deitado_2.png')]

        self.image = self.canguru[int(self.atual)]
        self.rect = self.image.get_rect()
        self.rect.center = (190, 490)

    def avancar(self):
        self.destino = 450  # Corre até x = 400
        self.origem = 190
        self.velocidade = 10
        self.volta = 5
        self.volta_mais = 10

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

        if self.volta_rapido:
            self.voltando = False
            if self.rect.centerx > self.origem:
                self.rect.centerx -= self.volta_mais
            else:
                self.rect.centerx = self.origem
                self.avanco = False  # Finaliza tudo
                self.volta_rapido = False

    def atacar(self):
        if self.bumerangue.ataca:
            self.atacando = True
            self.animar = False
        else:
            self.atacando = False
    def pular(self):
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

        if self.pulando and self.avanco and not self.voltando:
            self.image = self.queda_imagem

        if self.pulo and not self.pulando:
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

        if self.pulo_duplo and self.pulo and self.pulando :
            self.pulo = False
            self.pulo_duplo = False
            self.gravidade = -25
            self.image = self.pulo_duplo_imagem

        if self.pulando and self.queda:
            self.gravidade += 2
            self.image = self.queda_imagem

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

            if self.rect.centery >= 520:  # chão
                self.rect.centery = 520
                self.gravidade = 0
                self.pulando = False
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
                self.queda = False
                teclas = pygame.key.get_pressed()
                if teclas[pygame.K_DOWN] and not teclas[pygame.K_UP]:
                    canguru.agachado = True
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

        if not self.agachado and not self.pulando:
            self.pulo = False
            self.pulando = False
            self.agachado = False
            if not self.atacando:
                self.animar = True
            if not self.animar:
                self.atacando = True


    def update(self):
        self.avancar()
        self.pular()
        self.atacar()

        if pygame.key.get_pressed()[K_UP] and not self.pulando:
            self.buffer_pulo = True

        elif self.pulando:
            self.image = pygame.transform.scale(self.image, (315 / 4, 379 / 4))

        elif self.agachado:
            self.atual_correndo += 0.15
            if self.atual_correndo >= len(self.canguru_agachado):
                self.atual_correndo = 0
            self.image = self.canguru_agachado[int(self.atual_correndo)]
            self.image = pygame.transform.scale(self.image, (438 / 4, 315 / 4))
            self.rect.centery = 530

        elif self.atacando:
            self.atual_ataca += 0.10
            if self.atual_ataca >= len(self.canguru_ataca):
                self.atual_ataca = 0
            self.image = self.canguru_ataca[int(self.atual_ataca)]
            self.image = pygame.transform.scale(self.image, (315 / 4, 379 / 4))
            self.rect.centery = 485

        else:
            self.atual += 0.10
            if self.atual >= len(self.canguru):
                self.atual = 0
            self.image = self.canguru[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (315 / 4, 379 / 4))
            self.rect.centery = 485

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

            self.movimento_x += 8
            arco = ((self.movimento_x - 100) ** 2) / 1000 - 60
            self.rect.center = (self.x_inicial + self.movimento_x, self.y_fixo + arco)

            if self.rect.x >= 500:  # Distância fixa da tela
                self.indo = False
                self.voltando = True

        # Na volta, ajusta gradualmente para a posição atual do canguru
        elif self.voltando:
            self.movimento_x -= 10

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
            if percentual < 0.3:
                # Ajuste mais agressivo
                ajuste = 50
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

            canguru_hitbox_cabeca = pygame.Rect(self.canguru.rect.x + 0, self.canguru.rect.y - 10, 100, 150)
            canguru_hitbox_corpo = pygame.Rect(self.canguru.rect.x + 0, self.canguru.rect.y + 55, 100, 100)

            pygame.draw.rect(tela, (0, 0, 0), bumerangue_hitbox, 2)
            pygame.draw.rect(tela, (250, 0, 0), canguru_hitbox_cabeca, 2)
            pygame.draw.rect(tela, (250, 0, 0), canguru_hitbox_corpo, 2)

            if self.voltando:
                if bumerangue_hitbox.colliderect(canguru_hitbox_cabeca):
                    print('colisao')
                    self.ataca = False
                if bumerangue_hitbox.colliderect(canguru_hitbox_corpo):
                    print('colisao')
                    self.ataca = False

    def update(self):
        self.Colisao()
        if self.ataca:
            self.bumerangue_on()
        else:
            self.reset_bumerangue()

class Nuvem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.spawn = True
        self.x = randint(800,1200)
        self.y = randint(0,45)
        self.velocidade = -2
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
                self.x = randint(800, 1200)
                self.y = randint(0,45)
                self.movimento.append([self.x, self.y])

    def update(self):
        if self.spawn:
            self.Sprites()
        self.Animar()

        for i in self.movimento:
            self.rect = self.image.get_rect()
            self.rect.topright = i[0], i[1]
            tela.blit(self.image, self.rect)

class Nuvem2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.spawn = True
        self.x = randint(800,1200)
        self.y = randint(55,130)
        self.velocidade = -2
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
        if self.spawn:
            self.Sprites()
        self.Animar()

        for i in self.movimento:
            self.rect = self.image.get_rect()
            self.rect.topright = i[0], i[1]
            tela.blit(self.image, self.rect)

class Nuvem3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.spawn = True
        self.x = randint(800,1200)
        self.y = randint(150,250)
        self.velocidade = -2
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
        if self.spawn:
            self.Sprites()
        self.Animar()

        for i in self.movimento:
            self.rect = self.image.get_rect()
            self.rect.topright = i[0], i[1]
            tela.blit(self.image, self.rect)

class Nuvem4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.spawn = True
        self.x = randint(1400,1600 )
        self.y = randint(150, 250)
        self.velocidade = -2
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
        if self.spawn:
            self.Sprites()
        self.Animar()

        for i in self.movimento:
            self.rect = self.image.get_rect()
            self.rect.topright = i[0], i[1]
            tela.blit(self.image, self.rect)

class Nuvem5(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.spawn = True
        self.x = randint(1400,1600 )
        self.y = randint(150, 250)
        self.velocidade = -2
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
        if self.spawn:
            self.Sprites()
        self.Animar()

        for i in self.movimento:
            self.rect = self.image.get_rect()
            self.rect.topright = i[0], i[1]
            tela.blit(self.image, self.rect)

class Chao(pygame.sprite.Sprite):
    def __init__ (self, pontos):
        pygame.sprite.Sprite.__init__(self)
        self.leveis = pontos
        self.velocidade = 0
        self.chao = pygame.image.load('elementos/cenario/chão.png')
        self.chao = pygame.transform.scale(self.chao, (1469/5,1024/5))
        self.image = self.chao
        self.rect = self.image.get_rect()
        self.quantidade_chao=15
        self.rua = []
        self.x = 0
        self.y = 420
        colisao = False

        for i in range(self.quantidade_chao): #quantidade que preenche a tela
            self.rua.append([self.x, self.y])
            self.x += 40  #cada i soma

    def chao_movimento(self):

        if self.quantidade_chao < 15:
            self.x += 40
            self.rua.append([self.x,self.y])
            self.quantidade_chao += 1

        #Level
        if self.leveis.lvl_0:
            self.velocidade = 3
        if self.leveis.lvl_1:
            self.velocidade = 4
        if self.leveis.lvl_2:
            self.velocidade = 5
        if self.leveis.lvl_3:
            self.velocidade = 6
        if self.leveis.lvl_4:
            self.velocidade = 7
        if self.leveis.lvl_5:
            self.velocidade = 10

        for i in self.rua:
            i[0] -= self.velocidade
            self.quantidade_chao -= 1

            if i[0] < -10:
                self.rua.remove(i)


        for i in self.rua:

            self.rect = self.image.get_rect()  # Atualiza o rect da nuvem
            self.rect.center= i[0], i[1]  # Posiciona o rect conforme a posição da nuvem
            tela.blit(self.image, self.rect)

    def update(self):
        self.chao_movimento()

class Dingo (pygame.sprite.Sprite):
    def __init__(self,pontos,bumerangue,canguru):
        pygame.sprite.Sprite.__init__(self)
        self.leveis = pontos
        self.bumerangue = bumerangue
        self.canguru = canguru
        self.x = 1500
        self.y = 300
        self.andando = [] #para gerenciar x e y
        self.andando.append([self.x,self.y])
        self.correndo = True
        self.ataque = False
        self.contador_dingo = 0
        self.Sprites()

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


    def Animacao(self):

        if self.leveis.lvl_0:
            if self.correndo:
                self.velocidade_animacao = 0.10
            if self.ataque:
                self.velocidade_animacao = 0.05
            self.velocidade = 5

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

            if i [0] - self.canguru.rect.x <= 320:
               self.ataque = True
               self.correndo = True

            if i[0] - self.bumerangue.rect.x <= 200:
                self.ataque = True
                self.correndo = True

            i[0] -= self.velocidade
            if i[0] <= -1:
                self.andando.remove(i)
                self.andando.append([self.x, self.y])
                self.contador_dingo = 0  # RESET DO CONTADOR
                self.ataque = False  # VOLTA AO ESTADO INICIAL
                self.correndo = True

    def update(self):
        self.Animacao()

        for i in self.andando:
            self.image = pygame.transform.scale(self.image, (1200/8,1200/8))
            self.rect = self.image.get_rect()  #image ja foi deifinido pela lista de lagartos, ele ja existe independentre
            self.rect.topright = i[0], i[1]  # Posiciona o rect conforme a posição da nuvem
            tela.blit(self.image, self.rect)

class Lagarto(pygame.sprite.Sprite):
    def __init__(self,pontos,canguru):
        pygame.sprite.Sprite.__init__(self)
        self.leveis = pontos
        self.canguru = canguru
        self.x = 1000
        self.y = 240
        self.contador_lagarto = 0
        self.contado_ataque = 0
        self.ataque = False
        self.parado = True
        self.andando = [] #para gerenciar x e y
        self.andando.append([self.x, self.y])

    def Sprites(self):
        self.lagartos = []
        if self.parado:
            for i in (0,1):
                imagem_lagarto = carroca_lagarto.subsurface((i * 397, 0), (397, 362))
                imagem_lagarto = pygame.transform.scale(imagem_lagarto, (397 / 2, 362 /2))
                self.lagartos.append(imagem_lagarto)

        elif self.ataque:
            for i in [2,3,4]:
                ataque_lagarto = carroca_lagarto.subsurface((i*397,0), (397,362))
                ataque_lagarto = pygame.transform.scale(ataque_lagarto, (397 / 2, 362 /2))
                self.lagartos.append(ataque_lagarto)

        self.image = self.lagartos[0]
        self.rect = self.image.get_rect()
        self.rect.center = 200, 200

    def Animacao(self):

        if self.leveis.lvl_0:
            if self.ataque:
                self.velocidade_animacao = 0.07
            else:
                self.velocidade_animacao = 0.10
            self.velocidade = 5

        if self.contador_lagarto >= len(self.lagartos):
            self.contador_lagarto = 0

        self.image = self.lagartos[int(self.contador_lagarto)]
        self.contador_lagarto += self.velocidade_animacao

        for i in self.andando:

            i[0] -= self.velocidade
            if i[0] < -1:
                self.andando.remove(i)
                self.andando.append([self.x, self.y])
                self.contador_lagarto = 0  # RESET DO CONTADOR
                self.ataque = False  # VOLTA AO ESTADO INICIAL
                self.parado = True


            if i[0] - self.canguru.rect.x <= 320 and i[0] - self.canguru.rect.x >= 80:
                self.ataque = True
                self.parado = False
                if self.canguru.rect.y <=120:
                    self.contador_lagarto = 0
            else:
                self.ataque = False
                self.parado = True

    def update(self):
        self.Sprites()
        self.Animacao()

        for i in self.andando:
            self.rect = self.image.get_rect()  #image ja foi deifinido pela lista de lagartos, ele ja existe independentre
            self.rect.topright = i[0], i[1]  # Posiciona o rect conforme a posição da nuvem
            tela.blit(self.image, self.rect)

class Aereos (pygame.sprite.Sprite):
    def __init__(self,pontos):
        pygame.sprite.Sprite.__init__(self)

        self.leveis = pontos
        self.contador = 0
        self.contador_ataque = 0
        self.velocidade_voo = 0
        self.velocidade = 0.10
        self.altura = [10,69,200]
        self.ataques = [400,500,600]
        self.atacar = choice(self.ataques)
        self.x = 1000
        self.y = choice(self.altura)
        self.voando = [] #para gerenciar x e y
        self.voando.append([self.x, self.y])
        self.atacando = False
        self.atacou = False
        self.voar = True
        self.sprites()

    def sprites (self):
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
        self.rect = self.image.get_rect()
        self.rect.center = (190, 490)

    def ataque(self):
        if self.rect.x <= self.atacar + 5 and self.rect.x >= self.atacar - 5 and not self.atacando:
            self.voar = False
            self.atacando = True

    def animar(self):

        if self.leveis.lvl_0:
            self.velocidade = 0.05
            self.velocidade_voo = 4
        elif self.leveis.lvl_1:  # Só verifica se lvl_0 for False
            self.velocidade = 0.08
            self.velocidade_voo = 6
        elif self.leveis.lvl_2:  # Só verifica se os anteriores forem False
            self.velocidade = 0.10
            self.velocidade_voo = 9
        elif self.leveis.lvl_3:
            self.velocidade = 0.13
            self.velocidade_voo = 11
        elif self.leveis.lvl_4:
            self.velocidade = 0.15
            self.velocidade_voo = 13
        elif self.leveis.lvl_5:
            self.velocidade = 0.16
            self.velocidade_voo = 15

        if self.atacando:
            if self.contador >= len(self.lista_atacando):
                self.atacando = False
                self.atacou = True
                self.contador = 0
            self.image = self.lista_atacando[int(self.contador)]
            self.contador += self.velocidade

        elif self.voar:
            if self.contador >= len(self.lista_aereo):
                self.contador = 0
            self.image = self.lista_aereo[int(self.contador)]
            self.contador += self.velocidade

        elif self.atacou and not self.atacando:
            if self.contador >= len(self.lista_atacou):
                self.contador = 0
            self.image = self.lista_atacou[int(self.contador)]
            self.contador += self.velocidade

        for i in self.voando:
            i[0] -= self.velocidade_voo
            if i[0] < -1:
                self.atacou = False
                self.atacando = False
                self.voar = True
                self.voando.remove(i)
                self.contador = 0
                self.y = choice(self.altura)
                self.voando.append([self.x, self.y])

    def colisao(self):
        for i in self.voando:
            self.image = pygame.transform.scale(self.image, (500 // 4, 500 // 4))
            voando_rect = self.image.get_rect(topright=i)
            voando_hitbox = voando_rect.inflate(-50, -60)
            dino_hitbox_cabeca = pygame.Rect(canguru.rect.x + 25, canguru.rect.y + 10, 50, 35)
            dino_hitbox_corpo = pygame.Rect(canguru.rect.x + 25, canguru.rect.y + 55, 40, 40)

            pygame.draw.rect(tela, (0, 0, 250), dino_hitbox_cabeca, 2)
            pygame.draw.rect(tela, (0, 250, 250), dino_hitbox_corpo, 2)
            pygame.draw.rect(tela, (255, 0, 0), voando_hitbox, 2)

            if voando_hitbox.colliderect(dino_hitbox_corpo):
                print('colisao ')
            if voando_hitbox.colliderect(dino_hitbox_cabeca):
                print('colisao aerea')

    def update(self):
        self.animar()
        self.colisao()
        self.ataque()

        for i in self.voando:
            self.image = pygame.transform.scale(self.image, (500 // 4, 500 // 4))
            self.rect = self.image.get_rect()  # Atualiza o rect da nuvem
            self.rect.topright = i[0], i[1]  # Posiciona o rect conforme a posição da nuvem
            tela.blit(self.image, self.rect)

class Osso(pygame.sprite.Sprite):
    def __init__(self,pontos,aereo,canguru):
        pygame.sprite.Sprite.__init__(self)
        self.contador_osso = 0
        self.leveis = pontos
        self.aereo = aereo
        self.canguru = canguru

        self.atirar = False
        self.Sprites()
        self.x = 0
        self.y = 0
        self.velocidade = 8

    def Sprites(self):
        self.osso = []
        for i in range (6,13):
            imagem_osso = carroca_rato.subsurface((i * 500, 0), (500, 500))
            imagem_osso = pygame.transform.scale(imagem_osso, (500/3, 500/3))
            self.osso.append(imagem_osso)
        self.image = self.osso[0]
        self.rect = self.image.get_rect()
        self.rect.center = (-100, -100)

    def osso_on(self):
        self.contador_osso += 0.20
        if self.contador_osso > len(self.osso):
            self.contador_osso = 0
        self.image = self.osso[int(self.contador_osso)]

        if self.aereo.atacou and not self.atirar:
            self.atirar = True
            self.rect.center = self.aereo.rect.center
            self.x, self.y = self.rect.center

            # PEGA APENAS A POSIÇÃO X DO CANGURU (horizontal)
            self.alvo_x = self.canguru.rect.centerx

            # Configurações de movimento:
            self.velocidade_x = 9  # Velocidade horizontal (ajuste)
            self.velocidade_y = 5 # Velocidade vertical (queda)

            # Determina direção horizontal (esquerda/direita)
            self.direcao_x = 1 if self.alvo_x > self.x else -1

            # Movimento ATUAL (bem simples)
        if self.atirar:
            # Movimento horizontal SEMPRE na direção X original do canguru
            self.x += self.velocidade_x * self.direcao_x

            # Queda vertical (Y sempre aumenta)
            self.y += self.velocidade_y

            self.rect.center = (int(self.x), int(self.y))

        if self.aereo.rect.x <= -10:
            self.atirar = False
            self.contador_osso = 0
            self.rect.center = (-100, -100)


    def update(self):
        self.osso_on()

class Cenario(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.fase_1 = pygame.image.load('elementos/cenario/fundo.png')
        self.fase_1 = pygame.transform.scale(self.fase_1,(1536/2.2,1024/2.2))
        self.image = self.fase_1
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)

    def update(self):
        self.image = self.fase_1
        self.rect = self.image.get_rect()
        self.rect.center = (300, 230)

class Montanha(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 320
        self.y = 180
        self.velocidade = -0.01
        self.montanha = pygame.image.load('elementos/cenario/montanha2.png')
        self.montanha = pygame.transform.scale(self.montanha, (1000,500))
        self.image = self.montanha
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)
    def update(self):
        self.image = self.montanha
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.x += self.velocidade
        if self.x <= -250:
            self.x = 1500

class Elementos(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.numeros = [0,1,2]
        self.cenario = choice (self.numeros)
        self.spawn = True
        self.x = 900
        self.velocidade = -2


    def Sprites(self):
        if self.spawn and self.cenario == 0:
            self.y = randint(310, 364)
            self.sorteio = [0, 1, 2]
            self.sorteado = choice(self.sorteio)
            self.areias = []
            imagem_areia = carroca_areia.subsurface ((self.sorteado*800,0), (800,200))
            imagem_areia = pygame.transform.scale(imagem_areia, (800/4,200/4))
            self.areias.append(imagem_areia)
            self.image = self.areias[0]
            self.spawn = False
            self.movimento = []
            self.movimento.append([self.x, self.y])

        if self.spawn and self.cenario == 1:
            self.y = randint(216,270)
            self.sorteio = [0, 1, 2]
            self.sorteado = choice(self.sorteio)
            self.cactos = []
            imagem_cacto = carroca_cacto.subsurface ((self.sorteado*1536,0), (1536,1024))
            imagem_cacto = pygame.transform.scale(imagem_cacto, (1536/6,1024/6))
            self.cactos.append(imagem_cacto)
            self.image = self.cactos[0]
            self.spawn = False
            self.movimento = []
            self.movimento.append([self.x, self.y])

        if self.spawn and self.cenario == 2:

            self.sorteio = [0,1]
            self.sorteado = choice(self.sorteio)
            self.ossos = []
            imagem_osso = carroca_osso.subsurface((self.sorteado * 300, 0), (300, 300))

            if self.sorteado == 0:

                lugares_osso = [285,290,300]
                self.y = choice(lugares_osso)
                if self.y == 300:
                    imagem_osso = pygame.transform.scale(imagem_osso, (300/3 , 300/3 ))
                elif self.y == 290:
                    imagem_osso = pygame.transform.scale(imagem_osso, (300 / 2.2, 300 / 2.2))
                elif self.y == 285:
                    imagem_osso = pygame.transform.scale(imagem_osso, (300 / 2, 300 / 2))



                self.ossos.append(imagem_osso)

            elif self.sorteado == 1: #260,270 = /2
                lugares_osso =[265,270,275,280,290]
                self.y = choice(lugares_osso)
                if self.y in(265,270):
                    imagem_osso = pygame.transform.scale(imagem_osso, (300 /2, 300 /2))
                elif self.y in (275, 280):
                    imagem_osso = pygame.transform.scale(imagem_osso, (300 / 2.5, 300 / 2.5))
                elif self.y == 290:
                    imagem_osso = pygame.transform.scale(imagem_osso, (300 /3, 300 /3))

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
                self.y = randint (310,364)
                self.movimento.append([self.x, self.y])

    def update(self):
        if self.spawn:
            self.Sprites()
        self.Animar()

        for i in self.movimento:
            self.rect = self.image.get_rect()
            self.rect.topright = i[0], i[1]
            tela.blit(self.image, self.rect)

class Elementos2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.numeros = [0, 1]
        self.cenario = choice(self.numeros)
        self.spawn = True
        self.x = 1200
        self.velocidade = -2

    def Sprites(self):
        if self.spawn and self.cenario == 0:
            self.y = randint(310, 364)
            self.sorteio = [0, 1]
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
            self.sorteio = [0, 1, 2]
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
                self.y = randint(310, 364)
                self.movimento.append([self.x, self.y])

    def update(self):
        if self.spawn:
            self.Sprites()
        self.Animar()

        for i in self.movimento:
            self.rect = self.image.get_rect()
            self.rect.topright = i[0], i[1]
            tela.blit(self.image, self.rect)

class Elementos3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.numeros = [0, 1, 2]
        self.cenario = choice(self.numeros)
        self.spawn = True
        self.x = 1500
        self.velocidade = -2

    def Sprites(self):
        if self.spawn and self.cenario == 0:
            self.y = randint(310, 364)
            self.sorteio = [0, 1, 2]
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
            self.sorteio = [0, 1, 2]
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

            self.sorteio = [0, 1]
            self.sorteado = choice(self.sorteio)
            self.ossos = []
            imagem_osso = carroca_osso.subsurface((self.sorteado * 300, 0), (300, 300))

            if self.sorteado == 0:

                lugares_osso = [285, 290, 300]
                self.y = choice(lugares_osso)
                if self.y == 300:
                    imagem_osso = pygame.transform.scale(imagem_osso, (300 / 3, 300 / 3))
                elif self.y == 290:
                    imagem_osso = pygame.transform.scale(imagem_osso, (300 / 2.2, 300 / 2.2))
                elif self.y == 285:
                    imagem_osso = pygame.transform.scale(imagem_osso, (300 / 2, 300 / 2))

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
        if self.spawn:
            self.Sprites()
        self.Animar()

        for i in self.movimento:
            self.rect = self.image.get_rect()
            self.rect.topright = i[0], i[1]
            tela.blit(self.image, self.rect)


#personagens
pontos = Leveis()
elementos = Elementos()
elementos2 = Elementos2()
elementos3 = Elementos3()
nuvem = Nuvem()
nuvem2 = Nuvem2()
nuvem3 = Nuvem3()
nuvem4 = Nuvem4()
nuvem5 = Nuvem5()
canguru = Canguru()
fase = Fases(pontos)
chao = Chao(pontos)
lagarto = Lagarto(pontos,canguru)
aereo = Aereos(pontos)
bumerangue = Bumerangue(canguru)
dingo = Dingo(pontos,bumerangue,canguru)
osso = Osso(pontos,aereo,canguru)
canguru.bumerangue = bumerangue

cenario = Cenario()
montanha = Montanha()

#grupo de classes
game = pygame.sprite.Group()
game.add(cenario,nuvem,nuvem2,nuvem3,nuvem4,nuvem5,montanha,elementos,elementos2,elementos3,
              lagarto,aereo,canguru,bumerangue,chao,dingo,osso)
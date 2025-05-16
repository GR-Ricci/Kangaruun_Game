import os
import pygame
pygame.init()

tela = pygame.display.set_mode((640,480))
relogio = pygame.time.Clock()


#Cidade de recursos
cidade = os.path.dirname(__file__)
loja_sprites = os.path.join(cidade,'elementos/spritesheet')
loja_imagens = os.path.join(cidade, 'elementos/sprites')
loja_cenarios = os.path.join(cidade, 'elementos/cenario')
loja_som = os.path.join(cidade, 'elementos/som')

#carrocas
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
carroca_tufo = pygame.image.load(os.path.join(loja_cenarios,'tufo.png')).convert_alpha()
carroca_grama = pygame.image.load(os.path.join(loja_cenarios,'grama.png')).convert_alpha()
carroca_montanhas = pygame.image.load(os.path.join(loja_cenarios,'montanhas.png')).convert_alpha()


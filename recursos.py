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
loja_efeitos = os.path.join(cidade,'elementos/efeitos')
loja_menu = os.path.join(cidade,'elementos/menus')
loja_item = os.path.join(cidade,'elementos/itens')
loja_boss = os.path.join(cidade,'elementos/boss')
loja_tutorial = os.path.join(cidade,'elementos/tutorial')
#carrocas
carroca_deserto = pygame.image.load(os.path.join(loja_cenarios, 'deserto.png')).convert_alpha()

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
carroca_morte1 = pygame.image.load(os.path.join(loja_efeitos,'morte1.png')).convert_alpha()
carroca_morte2 = pygame.image.load(os.path.join(loja_efeitos,'morte2.png')).convert_alpha()
carroca_impacto = pygame.image.load(os.path.join(loja_efeitos,'impacto.png')).convert_alpha()
carroca_rosto_vida = pygame.image.load(os.path.join(loja_sprites,'rostos_canguru.png')).convert_alpha()
carroca_numero_vida = pygame.image.load(os.path.join(loja_sprites,'numeros_vida.png')).convert_alpha()
carroca_dano_canguru = pygame.image.load(os.path.join(loja_efeitos,'dano.png')).convert_alpha()
carroca_canguru_parado = pygame.image.load(os.path.join(loja_sprites,'canguru_parado.png')).convert_alpha()
carroca_canguru_morto = pygame.image.load(os.path.join(loja_sprites,'canguru_morto.png')).convert_alpha()
carroca_canguru_morto_sem_bumerangue = pygame.image.load(os.path.join(loja_sprites,'canguru_morto_sem_bumerangue.png')).convert_alpha()
carroca_gameover = pygame.image.load(os.path.join(loja_menu,'gameover.png')).convert_alpha()
carroca_gameover_continue = pygame.image.load(os.path.join(loja_menu,'continue.png')).convert_alpha()
carroca_gameover_quit = pygame.image.load(os.path.join(loja_menu,'quit.png')).convert_alpha()
carroca_gameover_quit_quebrado = pygame.image.load(os.path.join(loja_menu,'quit_quebrado.png')).convert_alpha()
carroca_gameover_continue_quebrado = pygame.image.load(os.path.join(loja_menu,'continue_quebrado.png')).convert_alpha()
carroca_vida = pygame.image.load(os.path.join(loja_item,'vida.png')).convert_alpha()
carroca_menu_efeitos = pygame.image.load(os.path.join(loja_menu,'efeitos.png')).convert_alpha()
carroca_mochila = pygame.image.load(os.path.join(loja_item,'bag6.png')).convert_alpha()

carroca_boss_base = pygame.image.load(os.path.join(loja_boss,'tasmania_base.png')).convert_alpha()
carroca_boss_base_inversa = pygame.image.load(os.path.join(loja_boss,'tasmania_base2.png')).convert_alpha()
carroca_boss_ataque = pygame.image.load(os.path.join(loja_boss,'tasmania_ataque.png')).convert_alpha()
carroca_boss_ataqueb = pygame.image.load(os.path.join(loja_boss,'tasmania_ataqueb.png')).convert_alpha()
carroca_boss_avanco = pygame.image.load(os.path.join(loja_boss,'tasmania_avanco.png')).convert_alpha()
carroca_boss_avanco2 = pygame.image.load(os.path.join(loja_boss,'tasmania_avancob.png')).convert_alpha()

carroca_boss_vulneravel = pygame.image.load(os.path.join(loja_boss,'tasmania_vulneravel.png')).convert_alpha()
carroca_boss_derrotado = pygame.image.load(os.path.join(loja_boss,'tasmania_derrotado.png')).convert_alpha()
carroca_machado = pygame.image.load(os.path.join(loja_boss,'machado.png')).convert_alpha()
carroca_machadob= pygame.image.load(os.path.join(loja_boss,'machadob.png')).convert_alpha()
carroca_boss_pulo = pygame.image.load(os.path.join(loja_boss,'tasmania_pulo.png')).convert_alpha()
carroca_animacao_dano_boss = pygame.image.load(os.path.join(loja_boss,'animacao_dano_tasmania.png')).convert_alpha()
carroca_animacao_escudo_boss = pygame.image.load(os.path.join(loja_boss,'animacao_escudo_boss.png')).convert_alpha()

carroca_pause = pygame.image.load(os.path.join(loja_menu,'pause.png')).convert_alpha()
carroca_stage_clear = pygame.image.load(os.path.join(loja_menu,'stage_clear.png')).convert_alpha()
carroca_score = pygame.image.load(os.path.join(loja_menu,'score.png')).convert_alpha()
carroca_seta = pygame.image.load(os.path.join(loja_boss,'seta.png')).convert_alpha()
carroca_marcador_boss = pygame.image.load(os.path.join(loja_boss,'marcador_boss.png')).convert_alpha()

carroca_menu_continue = pygame.image.load(os.path.join(loja_menu,'continue_menu.png')).convert_alpha()
carroca_menu_shop = pygame.image.load(os.path.join(loja_menu,'shop.png')).convert_alpha()
carroca_menu_lvl = pygame.image.load(os.path.join(loja_menu,'lvl.png')).convert_alpha()
carroca_menu_new_game = pygame.image.load(os.path.join(loja_menu,'new_game.png')).convert_alpha()
carroca_back = pygame.image.load(os.path.join(loja_menu,'back.png')).convert_alpha()

carroca_kangarunn = pygame.image.load(os.path.join(loja_menu,'kangaruun2.png')).convert_alpha()
carroca_menu_image = pygame.image.load(os.path.join(loja_menu,'menu2.png')).convert_alpha()
carroca_menu_play= pygame.image.load(os.path.join(loja_menu,'play.png')).convert_alpha()
carroca_menu_exit = pygame.image.load(os.path.join(loja_menu,'exit.png')).convert_alpha()
carroca_menu_tutorial = pygame.image.load(os.path.join(loja_menu,'tutorial.png')).convert_alpha()
carroca_menu_settings = pygame.image.load(os.path.join(loja_menu,'settings.png')).convert_alpha()



carroca_cursor_play = pygame.image.load(os.path.join(loja_menu,'cursor_play.png')).convert_alpha()
carroca_cursor_exit = pygame.image.load(os.path.join(loja_menu,'cursor_exit.png')).convert_alpha()
carroca_cursor_settings = pygame.image.load(os.path.join(loja_menu,'cursor_settings.png')).convert_alpha()
carroca_cursor_shop = pygame.image.load(os.path.join(loja_menu,'cursor_shop2.png')).convert_alpha()

carroca_cursor_new_game = pygame.image.load(os.path.join(loja_menu,'cursor_new_game2.png')).convert_alpha()
carroca_cursor_continue = pygame.image.load(os.path.join(loja_menu,'cursor_continue.png')).convert_alpha()
carroca_cursor_lvl = pygame.image.load(os.path.join(loja_menu,'cursor_lvl.png')).convert_alpha()
carroca_cursor_tutorial = pygame.image.load(os.path.join(loja_menu,'cursor_tutorial.png')).convert_alpha()
carroca_cursor_back= pygame.image.load(os.path.join(loja_menu,'cursor_back.png')).convert_alpha()

carroca_progresso = pygame.image.load(os.path.join(loja_menu,'progresso.png')).convert_alpha()
carroca_progresso_full = pygame.image.load(os.path.join(loja_menu,'progresso_full.png')).convert_alpha()
carroca_progresso_marca = pygame.image.load(os.path.join(loja_menu,'progresso_marca.png')).convert_alpha()

carroca_chao = pygame.image.load(os.path.join(loja_cenarios,'chao_dividido.png')).convert_alpha()

carroca_tutorial_paginas =pygame.image.load(os.path.join(loja_tutorial,'tutorial_paginas.png')).convert_alpha()

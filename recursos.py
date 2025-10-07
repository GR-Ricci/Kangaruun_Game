import os
import sys
import pygame

pygame.init()
tela = pygame.display.set_mode((640,480))
pygame.display.set_caption("Kangaruun")
relogio = pygame.time.Clock()

# [Base path] + OS >>>  para PyInstaller
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath("")

def resource_path(*paths):
    return os.path.join(base_path, *paths)

#region Pastas >> Path
loja_sprites = resource_path('elementos','spritesheet')
loja_imagens = resource_path('elementos','sprites')
loja_cenarios = resource_path('elementos','cenario')
loja_som = resource_path('elementos','som')
loja_efeitos = resource_path('elementos','efeitos')
loja_menu = resource_path('elementos','menus')
loja_item = resource_path('elementos','itens')
loja_boss = resource_path('elementos','boss')
loja_tutorial = resource_path('elementos','tutorial')
loja_fontes = resource_path('elementos','fontes')
#endregion

#region Imagens
# Carregamento de imagens
carroca_deserto = pygame.image.load(resource_path('elementos','cenario','deserto.png')).convert_alpha()
carroca_canguru = pygame.image.load(resource_path('elementos','spritesheet','canguru.png')).convert_alpha()
carroca_bumerangue = pygame.image.load(resource_path('elementos','spritesheet','bumerangue.png')).convert_alpha()
carroca_lagarto = pygame.image.load(resource_path('elementos','spritesheet','lagarto.png')).convert_alpha()
carroca_rato = pygame.image.load(resource_path('elementos','spritesheet','rato.png')).convert_alpha()
carroca_dingo = pygame.image.load(resource_path('elementos','spritesheet','dingo.png')).convert_alpha()
carroca_cenario1 = pygame.image.load(resource_path('elementos','cenario','fundo.png')).convert_alpha()
carroca_areia = pygame.image.load(resource_path('elementos','cenario','areias.png')).convert_alpha()
carroca_nuvem = pygame.image.load(resource_path('elementos','cenario','nuvem.png')).convert_alpha()
carroca_cacto = pygame.image.load(resource_path('elementos','cenario','cactos.png')).convert_alpha()
carroca_osso = pygame.image.load(resource_path('elementos','cenario','osso.png')).convert_alpha()
carroca_tufo = pygame.image.load(resource_path('elementos','cenario','tufo.png')).convert_alpha()
carroca_grama = pygame.image.load(resource_path('elementos','cenario','grama.png')).convert_alpha()
carroca_montanhas = pygame.image.load(resource_path('elementos','cenario','montanhas.png')).convert_alpha()
carroca_montanha1 = pygame.image.load(resource_path('elementos','cenario','montanha.png')).convert_alpha()
carroca_montanha2 = pygame.image.load(resource_path('elementos','cenario','montanha2.png')).convert_alpha()
carroca_dia = pygame.image.load(resource_path('elementos','cenario','dia.png')).convert_alpha()
carroca_noite = pygame.image.load(resource_path('elementos','cenario','noite.png')).convert_alpha()
carroca_chao_dia = pygame.image.load(resource_path('elementos','cenario','chao_dia.png')).convert_alpha()
carroca_chao_noite = pygame.image.load(resource_path('elementos','cenario','chao_noite.png')).convert_alpha()
carroca_sol = pygame.image.load(resource_path('elementos','cenario','sol.png')).convert_alpha()
carroca_lua = pygame.image.load(resource_path('elementos','cenario','Lua.png')).convert_alpha()



carroca_morte1 = pygame.image.load(resource_path('elementos','efeitos','morte1.png')).convert_alpha()
carroca_morte2 = pygame.image.load(resource_path('elementos','efeitos','morte2.png')).convert_alpha()
carroca_impacto = pygame.image.load(resource_path('elementos','efeitos','impacto.png')).convert_alpha()
carroca_rosto_vida = pygame.image.load(resource_path('elementos','spritesheet','rostos_canguru.png')).convert_alpha()
carroca_numero_vida = pygame.image.load(resource_path('elementos','spritesheet','numeros_vida.png')).convert_alpha()
carroca_dano_canguru = pygame.image.load(resource_path('elementos','efeitos','dano.png')).convert_alpha()
carroca_canguru_parado = pygame.image.load(resource_path('elementos','spritesheet','canguru_parado.png')).convert_alpha()
carroca_canguru_morto = pygame.image.load(resource_path('elementos','spritesheet','canguru_morto.png')).convert_alpha()
carroca_canguru_morto_sem_bumerangue = pygame.image.load(resource_path('elementos','spritesheet','canguru_morto_sem_bumerangue.png')).convert_alpha()
carroca_gameover = pygame.image.load(resource_path('elementos','menus','gameover.png')).convert_alpha()
carroca_gameover_continue = pygame.image.load(resource_path('elementos','menus','continue.png')).convert_alpha()
carroca_gameover_quit = pygame.image.load(resource_path('elementos','menus','quit.png')).convert_alpha()
carroca_gameover_quit_quebrado = pygame.image.load(resource_path('elementos','menus','quit_quebrado.png')).convert_alpha()
carroca_gameover_continue_quebrado = pygame.image.load(resource_path('elementos','menus','continue_quebrado.png')).convert_alpha()
carroca_vida = pygame.image.load(resource_path('elementos','itens','vida.png')).convert_alpha()
carroca_menu_efeitos = pygame.image.load(resource_path('elementos','menus','efeitos.png')).convert_alpha()
carroca_mochila = pygame.image.load(resource_path('elementos','itens','bag6.png')).convert_alpha()




carroca_boss_base = pygame.image.load(resource_path('elementos','boss','tasmania_base.png')).convert_alpha()
carroca_boss_base_inversa = pygame.image.load(resource_path('elementos','boss','tasmania_base2.png')).convert_alpha()
carroca_boss_ataque = pygame.image.load(resource_path('elementos','boss','tasmania_ataque.png')).convert_alpha()
carroca_boss_ataqueb = pygame.image.load(resource_path('elementos','boss','tasmania_ataqueb.png')).convert_alpha()
carroca_boss_avanco = pygame.image.load(resource_path('elementos','boss','tasmania_avanco.png')).convert_alpha()
carroca_boss_avanco2 = pygame.image.load(resource_path('elementos','boss','tasmania_avancob.png')).convert_alpha()
carroca_boss_vulneravel = pygame.image.load(resource_path('elementos','boss','tasmania_vulneravel.png')).convert_alpha()
carroca_boss_derrotado = pygame.image.load(resource_path('elementos','boss','tasmania_derrotado.png')).convert_alpha()
carroca_machado = pygame.image.load(resource_path('elementos','boss','machado.png')).convert_alpha()
carroca_machadob = pygame.image.load(resource_path('elementos','boss','machadob.png')).convert_alpha()
carroca_boss_pulo = pygame.image.load(resource_path('elementos','boss','tasmania_pulo.png')).convert_alpha()
carroca_animacao_dano_boss = pygame.image.load(resource_path('elementos','boss','animacao_dano_tasmania.png')).convert_alpha()
carroca_animacao_escudo_boss = pygame.image.load(resource_path('elementos','boss','animacao_escudo_boss.png')).convert_alpha()

carroca_pause = pygame.image.load(resource_path('elementos','menus','pause.png')).convert_alpha()
carroca_stage_clear = pygame.image.load(resource_path('elementos','menus','stage_clear.png')).convert_alpha()
carroca_score = pygame.image.load(resource_path('elementos','menus','score.png')).convert_alpha()
carroca_seta = pygame.image.load(resource_path('elementos','boss','seta.png')).convert_alpha()
carroca_marcador_boss = pygame.image.load(resource_path('elementos','boss','marcador_boss.png')).convert_alpha()

carroca_menu_continue = pygame.image.load(resource_path('elementos','menus','continue_menu.png')).convert_alpha()
carroca_menu_shop = pygame.image.load(resource_path('elementos','menus','shop.png')).convert_alpha()
carroca_menu_lvl = pygame.image.load(resource_path('elementos','menus','lvl.png')).convert_alpha()
carroca_menu_new_game = pygame.image.load(resource_path('elementos','menus','new_game.png')).convert_alpha()
carroca_back = pygame.image.load(resource_path('elementos','menus','back.png')).convert_alpha()

carroca_kangarunn = pygame.image.load(resource_path('elementos','menus','kangaruun2.png')).convert_alpha()
carroca_menu_image = pygame.image.load(resource_path('elementos','menus','menu2.png')).convert_alpha()
carroca_menu_play = pygame.image.load(resource_path('elementos','menus','play.png')).convert_alpha()
carroca_menu_exit = pygame.image.load(resource_path('elementos','menus','exit.png')).convert_alpha()
carroca_menu_tutorial = pygame.image.load(resource_path('elementos','menus','tutorial.png')).convert_alpha()
carroca_menu_settings = pygame.image.load(resource_path('elementos','menus','settings.png')).convert_alpha()

carroca_cursor_play = pygame.image.load(resource_path('elementos','menus','cursor_play.png')).convert_alpha()
carroca_cursor_exit = pygame.image.load(resource_path('elementos','menus','cursor_exit.png')).convert_alpha()
carroca_cursor_settings = pygame.image.load(resource_path('elementos','menus','cursor_settings.png')).convert_alpha()
carroca_cursor_shop = pygame.image.load(resource_path('elementos','menus','cursor_shop2.png')).convert_alpha()
carroca_cursor_new_game = pygame.image.load(resource_path('elementos','menus','cursor_new_game2.png')).convert_alpha()
carroca_cursor_continue = pygame.image.load(resource_path('elementos','menus','cursor_continue.png')).convert_alpha()
carroca_cursor_lvl = pygame.image.load(resource_path('elementos','menus','cursor_lvl.png')).convert_alpha()
carroca_cursor_tutorial = pygame.image.load(resource_path('elementos','menus','cursor_tutorial.png')).convert_alpha()
carroca_cursor_back = pygame.image.load(resource_path('elementos','menus','cursor_back.png')).convert_alpha()

carroca_progresso = pygame.image.load(resource_path('elementos','menus','progresso.png')).convert_alpha()
carroca_progresso_full = pygame.image.load(resource_path('elementos','menus','progresso_full.png')).convert_alpha()
carroca_progresso_marca = pygame.image.load(resource_path('elementos','menus','progresso_marca.png')).convert_alpha()

carroca_chao = pygame.image.load(resource_path('elementos','cenario','chao_dividido.png')).convert_alpha()
carroca_tutorial_paginas = pygame.image.load(resource_path('elementos','tutorial','tutorial_paginas.png')).convert_alpha()

carroca_canguru_deitado1 = pygame.image.load(resource_path('elementos','sprites','canguru','deitado_1.png')).convert_alpha()
carroca_canguru_deitado2 = pygame.image.load(resource_path('elementos','sprites','canguru','deitado_2.png')).convert_alpha()
carroca_canguru_pulo = pygame.image.load(resource_path('elementos','sprites','canguru','pulo.png')).convert_alpha()
carroca_canguru_pulo_duplo = pygame.image.load(resource_path('elementos','sprites','canguru','pulo_duplo.png')).convert_alpha()
#endregion

#region Fonte
# Fonte
carroca_fonte_pixel = resource_path('elementos','fontes','Pixeled.ttf')
#endregion
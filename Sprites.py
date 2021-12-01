import pygame
import Mapa
import Telas

# Tempo dos sprites
sprites_tempo = [0]
# Qual sprite está ativo
sprites_ativos = {"Abelha": 0, "Aranha": 0}

# Sprites
# Inimigo Vertical
IV = pygame.sprite.Sprite()
IV.image = pygame.image.load("Recursos/NADA.jpg").subsurface((0, 0), (64, 64))
IV.rect = pygame.Rect(0, 0, 0, 0)
# Inimigo Horizontal
IH = pygame.sprite.Sprite()
IH.image = pygame.image.load("Recursos/NADA.jpg").subsurface((0, 0), (64, 64))
IH.rect = pygame.Rect(0, 0, 0, 0)
# Parede
Pa = pygame.sprite.Sprite()
Pa.rect = pygame.Rect(0, 0, 0, 0)
# Baú
Bau = pygame.sprite.Sprite()
Bau.image = pygame.image.load("Recursos/Bau.png")
Bau.image = pygame.transform.scale(Bau.image, (75, 75))
Bau.rect = pygame.Rect(0, 0, 0, 0)
# Chave
Ch = pygame.sprite.Sprite()
Ch.image = pygame.image.load("Recursos/Chave.png")
Ch.image = pygame.transform.scale(Ch.image, (71, 25))
Ch.rect = pygame.Rect(0, 0, 0, 0)
# Coração
Co = pygame.sprite.Sprite()
Co.image = pygame.image.load("Recursos/Coracao_3-1.png").subsurface((0, 0), (59, 64))
Co.image = pygame.transform.scale(Co.image, (37, 40))
Co.rect = pygame.Rect(0, 0, 0, 0)
# Porta
Por = pygame.sprite.Sprite()
Por.image = pygame.image.load("Recursos/Porta.png")
Por.image = pygame.transform.scale(Por.image, (200, 200))
Por.rect = pygame.Rect(0, 0, 0, 0)
# Espinhos
Es = pygame.sprite.Sprite()
Es.image = pygame.image.load("Recursos/NADA.jpg").subsurface((0, 0), (64, 64))
Es.rect = pygame.Rect(0, 0, 0, 0)

# Grupo de todos os sprites
# Inimigo Vertical
Grupo_sprites_IV = pygame.sprite.Group()
Grupo_sprites_IV.add(IV)
# Inimigo Horizontal
Grupo_sprites_IH = pygame.sprite.Group()
Grupo_sprites_IH.add(IH)
# Parede
Grupo_sprites_Pa = pygame.sprite.Group()
Grupo_sprites_Pa.add(Pa)
#Baú
Grupo_sprites_Bau = pygame.sprite.Group()
Grupo_sprites_Bau.add(Bau)
# Chave
Grupo_sprites_Ch = pygame.sprite.Group()
Grupo_sprites_Ch.add(Ch)
# Coração
Grupo_sprites_Co = pygame.sprite.Group()
Grupo_sprites_Co.add(Co)
# Porta
Grupo_sprites_Por = pygame.sprite.Group()
Grupo_sprites_Por.add(Por)
# Espinhos
Grupo_sprites_Es = pygame.sprite.Group()
Grupo_sprites_Es.add(Es)

def TemposDosSprites():
    # Abelha
    sprites_tempo[0] += 1
    if sprites_tempo[0] > 2:
        sprites_tempo[0] = 1

# Atualiza sprites
def Atualiza_sprites():
    # Abelha
    if sprites_tempo[0] == 2:
        sprites_ativos["Abelha"] += 1
        if sprites_ativos["Abelha"] > 1:
            sprites_ativos["Abelha"] = 0
    # Aranha
    if sprites_tempo[0] == 2:
        if sprites_ativos["Aranha"] == 0:
            sprites_ativos["Aranha"] = 4
        elif sprites_ativos["Aranha"] == 4:
            sprites_ativos["Aranha"] = 0

# Desenha todos os sprites
def Desenha_sprites(screen):
    # Inimigo Vertical
    for i in range(len(Mapa.InimigosV)):
        IV.rect = Mapa.InimigosV[i]
        # Abelha
        if Telas.fase[0] == -4:
            if Mapa.Inimigos_direcaoV[i] > 0:
                IV.image = pygame.image.load("Recursos/Abelha_Baixo_4-1.png").subsurface((sprites_ativos["Abelha"] * 64, 0), (64, 64))
            else:
                IV.image = pygame.image.load("Recursos/Abelha_Cima_4-1.png").subsurface((sprites_ativos["Abelha"] * 64, 0), (64, 64))
        '''# Aranha
        elif Telas.fase[0] == -?:
            if Mapa.Inimigos_direcaoV[i] > 0:
                IV.image = pygame.image.load("Recursos/Aranha_Baixo_9-1.png").subsurface((sprites_ativos["Aranha"] * 64, 0), (64, 64))
            else:
                IV.image = pygame.image.load("Recursos/Aranha_Cima_9-1.png").subsurface((sprites_ativos["Aranha"] * 64, 0), (64, 64))'''
        IV.image = pygame.transform.scale(IV.image, (200, 200))
        if IV.rect.left > -200 and IV.rect.right < 1416 and IV.rect.top > -200 and IV.rect.bottom < 904:
            Grupo_sprites_IV.draw(screen)

    # Inimigo Horizontal
    for i in range(len(Mapa.InimigosH)):
        IH.rect = Mapa.InimigosH[i]
        # Abelha
        if Telas.fase[0] == -4:
            if Mapa.Inimigos_direcaoH[i] > 0:
                IH.image = pygame.image.load("Recursos/Abelha_Direita_4-1.png").subsurface((sprites_ativos["Abelha"] * 64, 0), (64, 64))
            else:
                IH.image = pygame.image.load("Recursos/Abelha_Esquerda_4-1.png").subsurface((sprites_ativos["Abelha"] *64, 0), (64, 64))
        '''
        # Aranha
        elif Telas.fase[0] == -?:
            if Mapa.Inimigos_direcaoH[i] > 0:
                IH.image = pygame.image.load("Recursos/Aranha_Direita_9-1.png").subsurface((sprites_ativos["Aranha"] * 64, 0), (64, 64))
            else:
                IH.image = pygame.image.load("Recursos/Aranha_Esquerda_9-1.png").subsurface((sprites_ativos["Aranha"] * 64, 0), (64, 64))'''
        IH.image = pygame.transform.scale(IH.image, (200, 200))
        if IH.rect.left > -200 and IH.rect.right < 1416 and IH.rect.top > -200 and IH.rect.bottom < 904:
            Grupo_sprites_IH.draw(screen)

    # Parede
    for i in range(len(Mapa.Paredes)):
        Pa.rect = Mapa.Paredes[i]
        # Arvore
        if Telas.fase[0] == -4:
            Pa.image = pygame.image.load("Recursos/Arvores.png")
        '''# Pedras
        elif Telas.fase[0] == -?:
            Pa.image = pygame.image.load("Recursos/Pedras.png")'''
        Pa.image = pygame.transform.scale(Pa.image, (200, 200))
        if Pa.rect.left > -200 and Pa.rect.right < 1416 and Pa.rect.top > -200 and Pa.rect.bottom < 904:
            Grupo_sprites_Pa.draw(screen)

    # Chave
    for i in range(len(Mapa.Chaves)):
        Ch.rect = Mapa.Chaves[i]
        if Ch.rect.left > -200 and Ch.rect.right < 1416 and Ch.rect.top > -200 and Ch.rect.bottom < 904:
            Grupo_sprites_Ch.draw(screen)

    # Baú
    for i in range(len(Mapa.Baus)):
        Bau.rect = Mapa.Baus[i]
        if Bau.rect.left > -200 and Bau.rect.right < 1416 and Bau.rect.top > -200 and Bau.rect.bottom < 904:
            Grupo_sprites_Bau.draw(screen)

    # Coração
    for i in range(len(Mapa.coracao)):
        Co.rect = Mapa.coracao[i]
        if Co.rect.left > -200 and Co.rect.right < 1416 and Co.rect.top > -200 and Co.rect.bottom < 904:
            Grupo_sprites_Co.draw(screen)

    # Porta
    for i in range(len(Mapa.Portas)):
        Por.rect = Mapa.Portas[i]
        if Por.rect.left > -200 and Por.rect.right < 1416 and Por.rect.top > -200 and Por.rect.bottom < 904:
            Grupo_sprites_Por.draw(screen)

    # Espinho
    for i in range(len(Mapa.Espinhos)):
        Es.rect = Mapa.Espinhos[i]
        if Mapa.Espinhos_estado[i] == "ativo":
            Es.image = pygame.image.load("Recursos/spikes.png").subsurface((0, 0), (64, 64))
        elif Mapa.Espinhos_estado[i] == "desativado":
            Es.image = pygame.image.load("Recursos/spikes.png").subsurface((64, 0), (64, 64))
        Es.image = pygame.transform.scale(Es.image, (200, 200))
        if Es.rect.left > -200 and Es.rect.right < 1416 and Es.rect.top > -200 and Es.rect.bottom < 904:
            Grupo_sprites_Es.draw(screen)
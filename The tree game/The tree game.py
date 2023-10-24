import pygame
import math
from game import Game

pygame.init()


# génération de la fenêtre de jeu
pygame.display.set_caption("Comet fall game")
screen = pygame.display.set_mode((1080, 720))

# génération de l'arrière plan
background = pygame.image.load('assets/bg.jpg')

#importation de l'ecran d'accueil
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

game = Game()

running = True

while running:

    # positionnement de l'arrière plan
    screen.blit(background, (0, -200))

    #verification si jeu commencé
    if game.is_playing:
        #declencher le jeu
        game.update(screen)

    else:
        screen.blit(banner, banner_rect)




    # boucle de MAJ de l'écran
    pygame.display.flip()

    # pour quitter le jeu
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("A la prochaine")

        # boucle de déplacement et le reste
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #detection de la touche espace
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

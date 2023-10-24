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

play_button = pygame.image.load(('assets/button.png'))
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)


game = Game()

running = True

while running:

    # positionnement de l'arrière plan
    screen.blit(background, (0, -200))


    #verification si jeu commencé
    if game.is_playing:
        #declencher le jeu
        game.update(screen)
        game.player.update_health_bar(screen)

    else:
        screen.blit(banner, banner_rect)
        screen.blit(play_button, play_button_rect)




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


        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()

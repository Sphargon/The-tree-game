import pygame
import random

# création d'une classe pour gérer les monstres (momie)
class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.velocity = random.randint(1, 3)
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1080 + random.randint(0, 600)
        self.rect.y = 540

    def take_damage(self, amount):
        self.health -= amount

        if self.health <= 0:
            self.rect.x = 1000 + random.randint(0, 600)
            self.velocity = random.randint(1, 3)
            self.health = self.max_health

    def update_health_bar(self, surface):

        #définir la couleur de la barre de vie
        bar_color_health = (111, 210, 46)
        initial_max_health = (60, 63, 60)

        #définir sa position, sa longueur et sa largeur
        bar_position = [self.rect.x + 10, self.rect.y - 20, self.health, 5]
        initial_max_health_position = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]

        # dessiner cette barre sur le jeu
        pygame.draw.rect(surface, initial_max_health, initial_max_health_position)
        pygame.draw.rect(surface, bar_color_health, bar_position)




    def move_forward(self):
        #faire avancer le monstre + commande de collision
        if not self.game.check_collision(self, self.game.all_player):
           self.rect.x -= self.velocity

        else:
            self.game.player.damage(self.attack)

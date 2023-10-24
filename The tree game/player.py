import pygame
from projectile import Projectile


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 30
        self.velocity = 2
        self.all_projectile = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 500

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            self.game.game_over()


    def update_health_bar(self, surface):

        #définir la couleur de la barre de vie
        bar_color_health = (111, 210, 46)
        initial_max_health = (60, 63, 60)

        #définir sa position, sa longueur et sa largeur
        bar_position = [self.rect.x + 50, self.rect.y + 20, self.health, 5]
        initial_max_health_position = [self.rect.x + 50, self.rect.y + 20, self.max_health, 5]

        # dessiner cette barre sur le jeu
        pygame.draw.rect(surface, initial_max_health, initial_max_health_position)
        pygame.draw.rect(surface, bar_color_health, bar_position)


    def launch_projectile(self):
        self.all_projectile.add(Projectile(self))


    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monster):
            self.rect.x += self.velocity


    def move_left(self):
        self.rect.x -= self.velocity



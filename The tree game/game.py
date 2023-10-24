import pygame
from player import Player
from momie import Monster

class Game:

    def __init__(self):
        self.is_playing = False
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)
        self.all_monster = pygame.sprite.Group()
        self.pressed = {}
        


    def start(self):
        self.player.rect.x = 100
        self.is_playing = True

        self.spawning_monsters()
        self.spawning_monsters()
        self.spawning_monsters()
        self.spawning_monsters()

    def game_over(self):
        self.all_monster = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False


    def update(self, screen):
        # afffichage joueur
        screen.blit(self.player.image, self.player.rect)

        for projectile in self.player.all_projectile:
            projectile.move()

        for monster in self.all_monster:
            monster.move_forward()
            monster.update_health_bar(screen)

        # affichage projectiles
        self.player.all_projectile.draw(screen)

        # affichage momie
        self.all_monster.draw(screen)

        # direction
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()


    def check_collision(self, sprite, group):
        #vérfication des collisions
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


    def spawning_monsters(self):
        #pour faire apparaitre un monstre
        monster = Monster(self)
        self.all_monster.add(monster)
import pygame

# définir le projectile
class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.velocity = 4
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 130
        self.rect.y = player.rect.y + 100
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        # faire tourner la boule
        self.angle += 10
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)


    def remove(self):
        #faire disparaitre les projectiles quand cette commande est sollicitée
        self.player.all_projectile.remove(self)

    def move(self):
        #la faire aller a droite
        self.rect.x += self.velocity
        self.rotate()

        #vérification de collision avec les monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monster):
           self.remove()

           monster.take_damage(self.player.attack)



        # supression des projectiles inutiles
        if self.rect.x > 1080:
            self.player.all_projectile.remove(self)

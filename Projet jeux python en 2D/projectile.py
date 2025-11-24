import pygame

# Definir la classe pour configurer le projectile du personnage
class Projectile(pygame.sprite.Sprite):

     def __init__(self, player):
          super().__init__()
          self.velocity = 1
          self.player = player
          self.image = pygame.image.load("Projet jeux python en 2D/assets/projectile.png")
          self.image = pygame.transform.scale(self.image, (50, 50))
          self.rect = self.image.get_rect()
          self.rect.x = player.rect.x + 230
          self.rect.y = player.rect.y
          self.origin_image = self.image
          self.angle = 0

     def rotate(self):
          # Ca va permettre de faire tourner le projectile
          self.angle += 1
          self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
          self.rect = self.image.get_rect(center=self.rect.center)
        
     def remove(self):
          self.player.all_projectiles.remove(self)

     def move(self):
          self.rect.x += self.velocity
          self.rotate()

          # Ensuite je vais creer une condition pour retirer le tir si il n'est plus dans la fenetre
          if self.rect.x > 1080:
              self.remove()
     

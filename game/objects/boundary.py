import pygame
from game.constants import CHUNK

class Boundary(pygame.sprite.Sprite):
  def __init__(self, pos, groups, surface = pygame.Surface((CHUNK, CHUNK))):
    super().__init__(groups)
    self.image = surface
    self.rect = self.image.get_rect(topleft = pos)
    self.hitbox = self.rect.inflate((0, 0))

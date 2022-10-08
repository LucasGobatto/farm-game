import pygame
from game.constants import CHUNK

class Boundary(pygame.sprite.Sprite):
  def __init__(self, pos: tuple[int, int], groups):
    super().__init__(groups)
    self.image = pygame.Surface((CHUNK, CHUNK))
    self.rect = self.image.get_rect(topleft = pos)
    self.hitbox = self.rect.inflate((0, CHUNK / 2))

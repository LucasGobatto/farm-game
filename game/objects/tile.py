import pygame
from game.get_assets import GetAssets

class Tile(pygame.sprite.Sprite):

  def __init__(self, pos: tuple[int, int], groups, type: str, shrink: tuple[int, int] = (0,0)):
    super().__init__(groups)
    getAssets = GetAssets()

    self.image = getAssets.get(type)
    self.rect = self.image.get_rect(topleft = pos)
    self.hitbox = self.rect.inflate(shrink)

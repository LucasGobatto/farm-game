from random import choice
import pygame
from game.utils import import_folder
from game.constants import CHUNK

class Trees(pygame.sprite.Sprite):
  def __init__(self, pos, groups):
    super().__init__(groups)
    self.image = choice(import_folder("./assets/map/objects/trees"))
    self.rect = self.image.get_rect(topleft = pos)
    shrink_x =  -(CHUNK - 10) / 2
    shrink_y = -(3* CHUNK - 22)
    self.hitbox = self.rect.inflate((shrink_x, shrink_y))

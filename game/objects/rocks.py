from random import choice
import pygame
from game.utils import import_folder
from game.constants import CHUNK

class Rocks(pygame.sprite.Sprite):

  def __init__(self, pos, groups, type):
    super().__init__(groups)
    self.image = choice(import_folder(f"./assets/map/objects/{type}"))
    self.rect = self.image.get_rect(topleft = pos)
    self.hitbox = self.rect.inflate((-CHUNK / 2, -CHUNK / 2))

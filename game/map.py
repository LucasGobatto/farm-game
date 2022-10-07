import pygame
from game.camera import Camera
from game.constants import *
from game.objects import Player

class Map:
  def __init__(self):
    self.surface = pygame.display.get_surface()

    self.visible_sprites = Camera()
    self.obstacle_sprites = pygame.sprite.Group() 

    self.__create_map__()

  def __create_map__(self):
    self.player = Player((800,600), [self.visible_sprites], self.obstacle_sprites)

  def run(self):
    self.visible_sprites.custom_draw(self.player)
    self.visible_sprites.update()
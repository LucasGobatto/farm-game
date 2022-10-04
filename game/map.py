import pygame
from game.constants import *
from game.objects import Water, Player

class Map:
  def __init__(self):
    self.surface = pygame.display.get_surface()

    self.visible_sprites = pygame.sprite.Group()
    self.obstacle_sprites = pygame.sprite.Group()

    self.__create_map__()

  def __create_map__(self):
    for y, line in enumerate(MAP):
      for x, square in enumerate(line):
        position = (x * CHUNK, y * CHUNK)
        size = ((x + 1) * CHUNK, (y+1) * CHUNK)

        if (square == MapIcons.land):
          self.surface.fill(Color.green, (position, size))
        if (square == MapIcons.player):
          Player(position, [self.visible_sprites], self.obstacle_sprites)
        if (square == MapIcons.water):
          Water(position, [self.obstacle_sprites, self.visible_sprites])

  def run(self):
    self.visible_sprites.draw(self.surface)
    self.visible_sprites.update()
import pygame
from game.camera import Camera
from game.constants import *
from game.objects import Player, Boundary
from game.utils import import_csv_file

class Map:
  def __init__(self):
    self.surface = pygame.display.get_surface()

    self.visible_sprites = Camera()
    self.obstacle_sprites = pygame.sprite.Group() 

    self.__create_map__()

  def __create_map__(self):
    layout = {
      "boundary": import_csv_file("./assets/csv/boundary.csv")
    }

    for styles in layout.keys():
      for y, row in enumerate(layout[styles]):
        for x, space in enumerate(row):
          pos = (x * CHUNK, y * CHUNK)

          if (styles == "boundary" and space == "0"):
            Boundary(pos, [self.obstacle_sprites])

    self.player = Player((700,600), [self.visible_sprites], self.obstacle_sprites)

  def run(self):
    self.visible_sprites.custom_draw(self.player)
    self.visible_sprites.update()
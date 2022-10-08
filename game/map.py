import pygame
from game.camera import Camera
from game.constants import *
from game.objects import Player, Boundary, Tile, Rocks
from game.utils import import_csv_file

class Map:
  def __init__(self):
    self.surface = pygame.display.get_surface()

    self.visible_sprites = Camera()
    self.obstacle_sprites = pygame.sprite.Group() 

    self.__create_map__()

  def __create_map__(self):
    layout = {
      "boundary": import_csv_file("boundary.csv"),
      "grass": import_csv_file("grass.csv"),
      "rocks": import_csv_file("rocks.csv"),
      "trees": import_csv_file("trees.csv"),
      "flowers": import_csv_file("flowers.csv"),
      "arbory": import_csv_file("arbory.csv"),
      "water-grass": import_csv_file("water-grass.csv"),
      "water-rocks": import_csv_file("water-rocks.csv"),
      "hero": import_csv_file("hero.csv")
    }
    obstacle_sprites = ["rocks"]

    for styles in layout.keys():
      for y, row in enumerate(layout[styles]):
        for x, space in enumerate(row):
          pos = (x * CHUNK, y * CHUNK)

          if (styles == "trees"):
            if (space == "0"):
              Tile(pos, [self.visible_sprites], styles)

          elif (styles == "hero"):
            if (space == "13"):
              self.player = Player(pos, [self.visible_sprites], self.obstacle_sprites)


          elif (space != "-1"):
            if (styles == "boundary"):
              Boundary(pos, [self.obstacle_sprites])


            elif (styles in obstacle_sprites):
              Rocks(pos, [self.visible_sprites, self.obstacle_sprites], styles)
            else:
              Tile(pos, [self.visible_sprites], styles)


  def run(self):
    self.visible_sprites.custom_draw(self.player)
    self.visible_sprites.update()
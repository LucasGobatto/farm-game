import pygame
from game.camera import Camera
from game.constants import *
from game.objects import Player, Boundary, Tile
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

    for styles in layout.keys():
      for y, row in enumerate(layout[styles]):
        for x, space in enumerate(row):
          pos = (x * CHUNK, y * CHUNK)

          if (styles == "trees"):
            if (space == "0"):
                shrink_x =  -(CHUNK - 10) / 2
                shrink_y = -(3* CHUNK - 22)
                shrink = (int(shrink_x), int(shrink_y))
                Tile(pos, [self.visible_sprites, self.obstacle_sprites], styles, shrink)

          elif (styles == "hero"):
            if (space == "13"):
              self.player = Player(pos, [self.visible_sprites], self.obstacle_sprites)

          elif (space != "-1"):
            if (styles == "boundary"):
              Boundary(pos, [self.obstacle_sprites])
              continue

            if (styles == "rocks"):
              shrink = (int(-CHUNK / 2), int(-CHUNK / 2))
              sprites = [self.visible_sprites, self.obstacle_sprites]
            else:
              sprites = [self.visible_sprites]
              shrink = (0,0)

            Tile(pos, sprites, styles, shrink)

  def run(self):
    self.visible_sprites.custom_draw(self.player)
    self.visible_sprites.update()
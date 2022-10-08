from os import walk
import pygame

def import_folder(path: str) -> list[pygame.surface.Surface]:
  images: list[pygame.surfice.Surface] = []
  for (_, __, files) in walk(path):
    for file in files:
      fullpath = f'{path}/{file}'
      image = pygame.image.load(fullpath).convert_alpha()
      images.append(image)
    pass
  
  return images

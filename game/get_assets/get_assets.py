from random import choice
import pygame
from .singleton import Singleton
from game.utils import import_folder

class GetAssets(metaclass=Singleton):
  _base_root = "./game/assets/map/objects"
  _objects: dict[str, list] = {}

  def get(self, asset: str) -> pygame.surface.Surface:
    if (asset not in self._objects.keys()):
      self.__set__(asset)

    return choice(self._objects[asset])
  
  def __set__(self, asset: str): 
    self._objects[asset] = import_folder(f"{self._base_root}/{asset}")


import time
import pygame
from game.constants import *

class GameStatsBuilder:
  _wood = 0
  _money = 0
  _meat = 0
  _seconds = time.time()
  _day = 1

  def __init__(self, content: str, pos: tuple[int, int]):
    self.font = GameStatsDisplayProperties.getFont()
    self.display_surface = pygame.display.get_surface()
    
    self.game_stats_surface = self.font.render(content, True, Color.invisible)
    self.rect = self.game_stats_surface.get_rect(topleft= pos)
    self.display_days()

    pygame.draw.rect(self.display_surface, Color.invisible, self.rect)

  def display_days(self):
    content = 'Dia: '+ str(self._day)
    self.day_surface = self.font.render(content, True, Color.invisible)
    sizes = self.display_surface.get_size()
    self.day_rect = self.day_surface.get_rect(topright=(sizes[0] - 10, 10))
    self.display_surface.blit(self.day_surface, self.day_rect)

  def increase_day(self):
    self._day += 1

  def update(self):
    self.display_days()
    self.display_surface.blit(self.game_stats_surface, self.rect)

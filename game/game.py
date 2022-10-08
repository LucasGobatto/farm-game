import pygame, os
from game.constants import *
from game.game_stats import GameStatsBuilder
from game.map import Map

class Game():
  def __init__(self):
    pygame.display.init()
    self.surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  
    pygame.display.set_caption("MiniFarm")
    pygame.font.init()

    self.game_stats = GameStatsBuilder()
    pygame.time.set_timer(pygame.USEREVENT + 1, FIVE_MINUTES)
    self.clock = pygame.time.Clock()
  
    self.map = Map()

  def stop(self):
    pygame.quit()
    os._exit(0)

  def run(self):
    while True:
      pressed_keys = pygame.key.get_pressed()
        
      for event in pygame.event.get():
        if pressed_keys[pygame.K_ESCAPE] or event.type == pygame.QUIT:
          self.stop()
        if event.type == pygame.USEREVENT + 1:
          self.game_stats.increase_day()

      self.surface.fill(0)
      self.map.run()

      self.game_stats.update()
      pygame.display.update()
      self.clock.tick(GAME_FPS)
  
if __name__ == "__main__":
  game = Game()
  game.run()

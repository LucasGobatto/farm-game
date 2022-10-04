import pygame, os
from game.constants import *
from game.map import Map

class Game():
  def __init__(self):
    pygame.display.init()
    pygame.display.set_mode(size=(WIDTH, HEIGHT))
    pygame.display.set_caption("MiniFarm")

    self.clock = pygame.time.Clock()
  
    self.map = Map()

  def stop(self):
    pygame.quit()
    os._exit(0)

  def run(self):
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.stop()

      self.map.run()
      pygame.display.update()
      self.clock.tick(GAME_FPS)
  
if __name__ == "__main__":
  game = Game()
  game.run()

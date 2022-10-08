from pygame.font import Font

GAME_FPS = 60
WIDTH = 912
HEIGHT = 728
CHUNK = 48
FIVE_MINUTES = 5 * 60 * 1000

class Color:
  blue_dark = (0, 0, 255)
  green = (0, 255, 0)
  blue_light = (0, 55, 234)
  green_light = (0, 188, 66)
  black = (0, 0, 0)
  white = (255, 255, 255)
  invisible = (255, 255, 255)

class GameStatsDisplayProperties:
  @staticmethod
  def getFont():
    return Font(None, 48)
  
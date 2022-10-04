import pygame

class Player(pygame.sprite.Sprite):

  def __init__(self, pos, groups):
    super().__init__(groups)
    self.image = pygame.image.load('./assets/player.png').convert_alpha()
    self.rect = self.image.get_rect(topleft = pos)

    self.direction = pygame.math.Vector2()
    self.speed = 5

  def update(self):
    self.__keyboard_input__()
    self.move(self.speed)

  def move(self, speed):
    if self.direction.magnitude() != 0:
      self.direction = self.direction.normalize()

    self.rect.center += self.direction * speed

  def __keyboard_input__(self):
    movements = {
      "increase": 1,
      "decrease": -1,
    }

    events = pygame.key.get_pressed()
    direction = { "x": 0, "y": 0}
   
    if events[pygame.K_UP]:
      direction["y"] = movements["decrease"]
    
    if events[pygame.K_DOWN]:
      direction["y"] = movements["increase"]
    
    if events[pygame.K_LEFT]:
      direction["x"] = movements["decrease"]

    if events[pygame.K_RIGHT]:
      direction["x"] = movements["increase"]

    self.direction.x = direction["x"]
    self.direction.y = direction["y"]

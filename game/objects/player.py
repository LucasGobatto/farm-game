import pygame, math
from game.utils import import_folder

class Player(pygame.sprite.Sprite):
  def __init__(self, pos, groups, obstacle_sprites):
    super().__init__(groups)
    self.import_image()
    self.frame_index = 0
    self.animation_time = 0.1
    self.is_running = False
    self.animation_direction = "front"
    self.image = self.animation["stop"][self.animation_direction][self.frame_index]
    self.rect = self.image.get_rect(topleft = pos)
    self.hitbox = self.rect.inflate(0, 0)

    self.direction = pygame.math.Vector2()
    self.speed = 3

    self.obstacle_sprites = obstacle_sprites

  def import_image(self):
    path = "./assets/player"
    self.animation = {
      "stop": { "left": [], "right": [], "front": [], "back": []}, 
      "running": { "left": [], "right": [], "front": [], "back": []},
    }
    
    for state in self.animation.keys():
      for direction in self.animation[state].keys():
        fullpath = f"{path}/{state}/{direction}"
        self.animation[state][direction] = import_folder(fullpath)
  
  def animate(self):
    if (self.is_running):
      state = "running"
      self.frame_index += self.animation_time
    else:
      self.frame_index += self.animation_time / 2 
      state = "stop"

    animation = self.animation[state][self.animation_direction]

    if (self.frame_index >= len(animation)):
      self.frame_index = 0
    
    self.image = animation[int(math.floor(self.frame_index))]

  def update(self):
    self.keyboard_input()
    self.move()
    self.animate()

  def move(self):
    if (self.direction.x == 0 and self.direction.y == 0):
      self.is_running = False
    else:
      self.is_running = True

    if self.direction.magnitude() != 0:
      self.direction = self.direction.normalize()

    self.hitbox.x += self.direction.x * self.speed
    self.collision("horizontal")
    self.hitbox.y += self.direction.y * self.speed
    self.collision("vertical")
    self.rect.center = self.hitbox.center

  def keyboard_input(self):
    movements = {
      "increase": 1,
      "decrease": -1,
    }

    events = pygame.key.get_pressed()
    direction = { "x": 0, "y": 0 }
   
    if events[pygame.K_UP] or events[pygame.K_w]:
      direction["y"] = movements["decrease"]
      self.animation_direction = "back"
    
    if events[pygame.K_DOWN] or events[pygame.K_s]:
      direction["y"] = movements["increase"]
      self.animation_direction = "front"

    if events[pygame.K_LEFT] or events[pygame.K_a]:
      direction["x"] = movements["decrease"]
      self.animation_direction = "left"

    if events[pygame.K_RIGHT] or events[pygame.K_d]:
      direction["x"] = movements["increase"]
      self.animation_direction = "right"

    self.direction.x = direction["x"]
    self.direction.y = direction["y"]

  def collision(self, direction):
    if direction == "horizontal":
      for sprite in self.obstacle_sprites:
        if sprite.hitbox.colliderect(self.hitbox):
          if self.direction.x > 0:
            self.hitbox.right = sprite.hitbox.left
          elif self.direction.x < 0:
            self.hitbox.left = sprite.hitbox.right

    if direction == "vertical":
      for sprite in self.obstacle_sprites:
        if sprite.hitbox.colliderect(self.hitbox):
          if self.direction.y > 0:
            self.hitbox.bottom = sprite.hitbox.top
          elif self.direction.y < 0:
            self.hitbox.top = sprite.hitbox.bottom

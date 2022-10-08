from typing import Literal
import pygame, math
from pygame.surface import Surface
from game.utils import import_folder
from game.constants import CHUNK

DirectionType = Literal["horizontal","vertical"]
AnimationDirections = Literal["left","right","back","front"]

class Player(pygame.sprite.Sprite):
  _is_running = False
  _frame_index = 0
  _animation_direction: AnimationDirections = "front"
  _animation_time = 0.1
  _speed = 3
  _direction = pygame.math.Vector2()
  
  def __init__(self, pos, groups, obstacle_sprites):
    super().__init__(groups)
    self.import_image()
    self.image = self.animation["stop"][self._animation_direction][self._frame_index]
    self.rect = self.image.get_rect(topleft = pos)
    self.hitbox = self.rect.inflate((1 - (CHUNK / 2), 2 - CHUNK * 2))
    self.obstacle_sprites = obstacle_sprites

  def import_image(self):
    path = "./assets/player"
    self.animation: dict[str, dict[str, list[Surface]]] = {
      "stop": { "left": [], "right": [], "front": [], "back": []}, 
      "running": { "left": [], "right": [], "front": [], "back": []},
    }
    
    for state in self.animation.keys():
      for direction in self.animation[state].keys():
        fullpath = f"{path}/{state}/{direction}"
        self.animation[state][direction] = import_folder(fullpath)
  
  def animate(self):
    if (self._is_running):
      state = "running"
      self._frame_index += self._animation_time
    else:
      self._frame_index += self._animation_time / 2 
      state = "stop"

    animation = self.animation[state][self._animation_direction]

    if (self._frame_index >= len(animation)):
      self._frame_index = 0
    
    self.image = animation[int(math.floor(self._frame_index))]

  def update(self):
    self.keyboard_input()
    self.move()
    self.animate()

  def move(self):
    if (self._direction.x == 0 and self._direction.y == 0):
      self._is_running = False
    else:
      self._is_running = True

    if self._direction.magnitude() != 0:
      self._direction = self._direction.normalize()

    self.hitbox.x += int(self._direction.x * self._speed)
    self.collision("horizontal")
    self.hitbox.y += int(self._direction.y * self._speed)
    self.collision("vertical")
    
    if (self.rect):
      self.rect.center = self.hitbox.center

  def keyboard_input(self):
    movements = {
      "increase": 1,
      "decrease": -1,
    }

    events = pygame.key.get_pressed()
    direction: dict[str, int] = { "x": 0, "y": 0 }
   
    if events[pygame.K_UP] or events[pygame.K_w]:
      direction["y"] = movements["decrease"]
      self._animation_direction = "back"
    
    if events[pygame.K_DOWN] or events[pygame.K_s]:
      direction["y"] = movements["increase"]
      self._animation_direction = "front"

    if events[pygame.K_LEFT] or events[pygame.K_a]:
      direction["x"] = movements["decrease"]
      self._animation_direction = "left"

    if events[pygame.K_RIGHT] or events[pygame.K_d]:
      direction["x"] = movements["increase"]
      self._animation_direction = "right"

    self._direction.x = direction["x"]
    self._direction.y = direction["y"]

  def collision(self, direction: DirectionType):
    if direction == "horizontal":
      for sprite in self.obstacle_sprites:
        if sprite.hitbox.colliderect(self.hitbox):
          if self._direction.x > 0:
            self.hitbox.right = sprite.hitbox.left
          elif self._direction.x < 0:
            self.hitbox.left = sprite.hitbox.right

    if direction == "vertical":
      for sprite in self.obstacle_sprites:
        if sprite.hitbox.colliderect(self.hitbox):
          if self._direction.y > 0:
            self.hitbox.bottom = sprite.hitbox.top
          elif self._direction.y < 0:
            self.hitbox.top = sprite.hitbox.bottom

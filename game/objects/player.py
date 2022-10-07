import pygame

class Player(pygame.sprite.Sprite):
  def __init__(self, pos, groups, obstacle_sprites):
    super().__init__(groups)
    self.image = pygame.image.load('./assets/player/stop/front_stop_1.png').convert_alpha()
    self.rect = self.image.get_rect(topleft = pos)
    self.hitbox = self.rect.inflate(0, -5)

    self.direction = pygame.math.Vector2()
    self.speed = 3

    self.obstacle_sprites = obstacle_sprites

  def update(self):
    self.keyboard_input()
    self.move(self.speed)

  def move(self, speed):
    if self.direction.magnitude() != 0:
      self.direction = self.direction.normalize()

    self.hitbox.x += self.direction.x * speed
    self.collision("horizontal")
    self.hitbox.y += self.direction.y * speed
    self.collision("vertical")
    self.rect.center = self.hitbox.center

  def keyboard_input(self):
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

import pygame 

class Camera(pygame.sprite.Group):
  def __init__(self) -> None:
    super().__init__()

    self.surface = pygame.display.get_surface()
    self.half_width = self.surface.get_size()[0] // 2
    self.half_height = self.surface.get_size()[1] // 2
    self.offset = pygame.math.Vector2()
  
  def custom_draw(self, player):
    self.offset.x = player.rect.centerx - self.half_width 
    self.offset.y = player.rect.centery - self.half_height 

    for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
      offset_position = sprite.rect.topleft - self.offset 
      self.surface.blit(sprite.image, offset_position)

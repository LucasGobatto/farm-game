import pygame 

class Camera(pygame.sprite.Group):
  def __init__(self) -> None:
    super().__init__()

    self.surface = pygame.display.get_surface()
    self.half_width = self.surface.get_size()[0] // 2
    self.half_height = self.surface.get_size()[1] // 2
    self.offset = pygame.math.Vector2()

    self.floor_surf = pygame.image.load("./game/assets/map/ground.png").convert()
    self.floor_rect = self.floor_surf.get_rect(topleft=(0,0))
  
  def custom_draw(self, player):
    self.offset.x = player.rect.centerx - self.half_width 
    self.offset.y = player.rect.centery - self.half_height 

    floor_offeset_pos = self.floor_rect.topleft - self.offset
    self.surface.blit(self.floor_surf, floor_offeset_pos)

    for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
      offset_position = sprite.rect.topleft - self.offset 
      self.surface.blit(sprite.image, offset_position)

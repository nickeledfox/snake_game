import pygame
from pygame.locals import *


if __name__ == '__main__':
  pygame.init()

  def draw_block():
    surface.fill((0, 102, 51))
    surface.blit(block,(block_x, block_y))
    pygame.display.flip()

  # GFX
  surface = pygame.display.set_mode((800, 500))
  surface.fill((0, 102, 51))

  block = pygame.image.load('src/block.jpg').convert()
  block_x = 100
  block_y = 100
  surface.blit(block,(block_x, block_y))

  pygame.display.flip()

  running = True

  while running:
    for event in pygame.event.get():
      if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            running = False
        if event.key == K_LEFT:
            block_x -= 10
            draw_block()
        if event.key == K_RIGHT:
            block_x += 10
            draw_block()
        if event.key == K_UP:
            block_y -= 10
            draw_block()
        if event.key == K_DOWN:
            block_y += 10
            draw_block()

      elif event.type == QUIT:
          running = False
    
import pygame
import sys

from isometric_map import screen_to_tile, draw_map
from player import Player

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_WIDTH = 64
TILE_HEIGHT = 32

# Colors 2
WHITE = (255, 255, 255)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Staggered Isometric Map')

# Load tile
tile_image = pygame.image.load('tile.png')

# Load player image
player_image = pygame.image.load('player.png')

player = Player(5, 5, screen, player_image, TILE_WIDTH, TILE_HEIGHT)


def is_direct_diagonal(start, end):
    dx = abs(start.x - end.x)
    dy = abs(start.y - end.y)
    return dx == 1 and dy == 1


def main():
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                tile_x, tile_y = screen_to_tile(*event.pos)

                player.move_to(tile_x, tile_y)

        screen.fill(WHITE)
        draw_map(screen, tile_image)
        player.update()
        player.draw()
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()

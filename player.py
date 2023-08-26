import pygame

from isometric_map import world_to_screen
from pathfinding import Node, a_star
class Player:
    def __init__(self, x, y, screen, player_image, TILE_WIDTH, TILE_HEIGHT, scale_factor=0.2):
        self.x = x
        self.y = y
        self.path = []
        self.move_counter = 0
        self.MOVE_DELAY = 1
        self.screen = screen
        self.player_image = player_image
        self.TILE_WIDTH = TILE_WIDTH
        self.TILE_HEIGHT = TILE_HEIGHT
        self.player_image = pygame.transform.scale(player_image, (
        int(player_image.get_width() * scale_factor), int(player_image.get_height() * scale_factor)))

    def move_to(self, x, y):
        # Here x and y are already tile coordinates, no need to convert them using screen_to_world.
        start = Node(self.x, self.y)
        end = Node(x, y)

        self.path = a_star(start, end)
        if self.path:
            # The path returned by a_star is already in tile coordinates, so you don't need to convert them again.
            self.path.pop(0)
            print(f"Moving from ({start.x}, {start.y}) to ({end.x}, {end.y}) through path: {self.path}")

    def update(self):
        self.move_counter += 1
        if self.path and self.move_counter >= self.MOVE_DELAY:
            self.x, self.y = self.path.pop(0)
            self.move_counter = 0

    def draw(self):
        screen_x, screen_y = world_to_screen(self.x, self.y)
        x_offset = (self.TILE_WIDTH - self.player_image.get_width()) // 2
        y_offset = self.TILE_HEIGHT - self.player_image.get_height()  # This should place the bottom of the sprite at the tile's "point"
        self.screen.blit(self.player_image, (screen_x + x_offset, screen_y + y_offset))

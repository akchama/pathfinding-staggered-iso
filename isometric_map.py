import pygame
from constants import TILE_WIDTH, TILE_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT

def draw_tile(screen, tile_image, x, y, col, row):
    screen.blit(tile_image, (x, y))

    # Set the font, color and render the text
    font = pygame.font.SysFont(None, 24)  # Use any available system font with size 24
    label = font.render(f"{col},{row}", True, (255, 0, 0))  # Render in red color
    screen.blit(label, (x + TILE_WIDTH // 4, y + TILE_HEIGHT // 4))  # Adjust this position if needed


def draw_map(screen, tile_image):
    cols = (SCREEN_WIDTH // (TILE_WIDTH // 2)) + 1
    rows = (SCREEN_HEIGHT // (TILE_HEIGHT // 2)) + 1

    for row in range(rows):
        for col in range(cols):
            x = col * TILE_WIDTH - (row % 2) * (TILE_WIDTH // 2)
            y = row * (TILE_HEIGHT // 2)
            draw_tile(screen, tile_image, x, y, col, row)

def screen_to_world(x, y):
    world_x = x + y
    world_y = y - x
    return world_x, world_y

def world_to_screen(x, y):
    if y % 2 == 0:  # even row
        screen_x = x * TILE_WIDTH
        screen_y = y * TILE_HEIGHT // 2
    else:  # odd row
        screen_x = x * TILE_WIDTH + TILE_WIDTH // 2
        screen_y = y * TILE_HEIGHT // 2
    return screen_x, screen_y


def screen_to_tile(x, y):
    print(f"Clicked at: {x}, {y}")

    col = x // TILE_WIDTH
    row = 2 * (y // TILE_HEIGHT)

    print(f"Initial col, row: {col}, {row}")

    x_offset = x % TILE_WIDTH
    y_offset = y % TILE_HEIGHT

    print(f"x_offset, y_offset: {x_offset}, {y_offset}")

    if col % 2 == 0:  # Even column
        if y_offset < (TILE_HEIGHT / 2) - x_offset * (TILE_HEIGHT / TILE_WIDTH):
            col -= 1
            row -= 1
    else:  # Odd column
        if y_offset < x_offset * (TILE_HEIGHT / TILE_WIDTH):
            col -= 1
        else:
            row += 1

    print(f"Adjusted col, row: {col}, {row}")

    return col, row


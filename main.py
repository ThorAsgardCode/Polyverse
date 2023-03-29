import pygame
import math

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Player settings
player_pos = [width // 2, height // 2]
player_angle = 0
player_speed = 5

# Other geometric forms
circle_radius = 25
square_size = 50
circle_pos = [100, 100]
square_pos = [300, 300]

# Chat settings
chat_font = pygame.font.Font(None, 36)
chat_text = ""
chat_timeout = 0


def draw_triangle(pos, angle):
    size = 20
    points = [
        (pos[0] + size * math.cos(angle), pos[1] + size * math.sin(angle)),
        (pos[0] + size * math.cos(angle + 4 * math.pi / 3), pos[1] + size * math.sin(angle + 4 * math.pi / 3)),
        (pos[0] + size * math.cos(angle + 2 * math.pi / 3), pos[1] + size * math.sin(angle + 2 * math.pi / 3)),
        ]
    pygame.draw.polygon(screen, GREEN, points)

def draw_chat(text):
    chat_surface = chat_font.render(text, True, WHITE)
    screen.blit(chat_surface, (20, height - 40))
def check_interaction(player_pos, obj_pos, threshold):
    distance = math.sqrt((player_pos[0] - obj_pos[0])**2 + (player_pos[1] - obj_pos[1])**2)
    return distance < threshold

def draw_button(screen, position, size, color, text):
    # Set font and text
    font = pygame.font.Font(None, 36)
    text = font.render(text, True, (0, 0, 0))
    text_rect = text.get_rect(center=(position[0] + size[0] / 2, position[1] + size[1] / 2))

    # Draw button
    pygame.draw.rect(screen, color, (*position, *size))
    screen.blit(text, text_rect)
running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_angle += 0.1
    if keys[pygame.K_RIGHT]:
        player_angle -= 0.1
    if keys[pygame.K_UP]:
        player_pos[0] += player_speed * math.cos(player_angle)
        player_pos[1] += player_speed * math.sin(player_angle)
    if keys[pygame.K_DOWN]:
        player_pos[0] -= player_speed * math.cos(player_angle)
        player_pos[1] -= player_speed * math.sin(player_angle)

    draw_triangle(player_pos, player_angle)
    pygame.draw.circle(screen, RED, circle_pos, circle_radius)
    pygame.draw.rect(screen, BLUE, (square_pos[0], square_pos[1], square_size, square_size))

    if check_interaction(player_pos, circle_pos, circle_radius + 20):
        chat_text = "Interacting with the circle!"
        chat_timeout = 60
    elif check_interaction(player_pos, square_pos, square_size / 2 + 20):
        chat_text = "Interacting with the square!"
        chat_timeout = 60

    if chat_timeout > 0:
        draw_chat(chat_text)
        chat_timeout -= 1

    # Draw button
    draw_button(screen, (100, 100), (200, 50), (255, 0, 0), "Click me!")

    pygame.display.flip()
    pygame.time.delay(33)

pygame.quit()
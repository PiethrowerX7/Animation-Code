import pygame
import sys

# Constants
ANIMATION_SPEED = 0.25

# Player Class Creation
class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.animation = False
        self.sprites = [pygame.image.load(f'frame_{i}.png') for i in range(1, 21)]
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def start_animation(self):
        self.animation = True

    def stop_animation(self):
        self.animation = False

    def update(self, speed):
        if self.animation:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]

# General Setup
pygame.init()
clock = pygame.time.Clock()
fps = 60

# Game Screen
WIDTH = 1100
HEIGHT = 920
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animation Test Code")
BLACK = (0, 0, 0)

# Creating Sprites and Groups
moving_sprites = pygame.sprite.Group()
player = Player(500, 500)
moving_sprites.add(player)

# Main Game Loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_SPACE]:
        player.start_animation()
    else:
        player.stop_animation()

    pygame.time.delay(30)
    screen.fill(BLACK)
    moving_sprites.draw(screen)
    moving_sprites.update(ANIMATION_SPEED)
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
sys.exit()
import pygame
import os
import random

# window setup
WIDTH, HEIGHT = 700, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FLAPPY BIRD")
FPS = 60

# images
BACKGROUND_IMAGE = pygame.image.load(os.path.join('images', 'background.png'))
BIRD_IMAGE = pygame.image.load(os.path.join('images', 'bird.png'))
PILLAR_IMAGE_1 = pygame.image.load(os.path.join('images', 'pillar_1.png'))
PILLAR_IMAGE_2 = pygame.image.load(os.path.join('images', 'pillar_2.png'))
PILLAR_IMAGE_3 = pygame.image.load(os.path.join('images', 'pillar_3.png'))

# bird
BIRD_WIDTH, BIRD_HEIGHT = 87, 89
VEL = 7

# pillar
PILLAR_VELOCITY = 5


def draw(bird, pillars):
    WIN.blit(BACKGROUND_IMAGE, (0, 0))
    WIN.blit(BIRD_IMAGE, (bird.x, bird.y))
    for pillar, random_pillar_image in pillars:
        WIN.blit(random_pillar_image, (pillar.x, pillar.y))


def create_pillar():
    pillar_images = [PILLAR_IMAGE_1, PILLAR_IMAGE_2, PILLAR_IMAGE_3]
    random_pillar = random.choice(pillar_images)
    pillar_width, pillar_height = random_pillar.get_rect().size
    random_y = random.randint(0, HEIGHT - pillar_height)

    new_pillar = pygame.Rect(WIDTH, random_y, pillar_width, pillar_height)

    return new_pillar, random_pillar


def move_pillar(pillars):
    for pillar, random_pillar in pillars:
        pillar.x -= PILLAR_VELOCITY

    pillars = [(pillar, random_pillar) for pillar, random_pillar in pillars if pillar.x + pillar.width > 0]
    return pillars


def bird_movement(bird, keys_pressed):
    if keys_pressed[pygame.K_SPACE] and bird.y - VEL > 0:
        bird.y -= VEL
    elif bird.y + VEL < HEIGHT - BIRD_HEIGHT:
        bird.y += VEL


def collision(bird, pillars):
    for pillar, random_pillar in pillars:
        if bird.colliderect(pillar):
            return True
    return False


def main():
    bird = pygame.Rect(50, HEIGHT // 2 - BIRD_HEIGHT, BIRD_WIDTH, BIRD_HEIGHT)

    pillar_timer = 0
    pillars = []

    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if pillar_timer == 0:
            new_pillar, random_pillar_image = create_pillar()
            pillars.append((new_pillar, random_pillar_image))
            pillar_timer = 50
        else:
            pillar_timer -= 1

        keys_pressed = pygame.key.get_pressed()

        bird_movement(bird, keys_pressed)
        move_pillar(pillars)
        draw(bird, pillars)

        if collision(bird, pillars):
            break

        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()

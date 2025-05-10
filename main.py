import pygame
import sys

from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()

    Shot.containers = (shots_group, updatable, drawable, all_sprites)
    Player.containers = (updatable, drawable, all_sprites)
    Asteroid.containers = (asteroids, updatable, drawable, all_sprites)
    AsteroidField.containers = (updatable,)
    #comma important as it tells python it's a tuple  with a single element
    asteroid_field = AsteroidField()

    player = Player(x, y)
    all_sprites.add(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

            for shot in shots_group:
                if asteroid.collides_with(shot):
                    new_asteroids = asteroid.split()
                    if new_asteroids:
                        for new_asteroid in new_asteroids:
                            all_sprites.add(new_asteroid)
                            asteroids.add(new_asteroid)
                    shot.kill()
        screen.fill("black")

        for item in updatable:
            if item == player:
                item.update(dt, shots_group)
            else:
                item.update(dt)

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__== "__main__":
    main()
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


"""this line ensures the main() fucntion is only called when this file is run directly; it won't
run if it's imported as a module. it's considered the "pythonic" way to structure an
executable program in python. Technically you could just call main()"""


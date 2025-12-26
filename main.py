import pygame, player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from asteroidfield import AsteroidField
from asteroid import Asteroid
import sys
import shot

def main():
    print("Starting Asteroids with pygame version:",  pygame.version.ver)
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    clock = pygame.time.Clock()
    dt = 0

    updatable= pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids= pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids,updatable, drawable)
    player.Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable,)
    shot.Shot.containers = (shots,updatable,drawable)

    asteroid_field = AsteroidField()
    player1 =  player.Player(x=SCREEN_WIDTH//2, y=SCREEN_HEIGHT//2)
    

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  
        dt = clock.tick(60) / 1000.0
        for asteroid in asteroids:
            if asteroid.collides_with(player1):
                    log_event("player_hit")
                    print("Game over!")
                    sys.exit()
            for s in shots:
                if asteroid.collides_with(s):
                    log_event("asteroid_shot")
                    asteroid.split()
                    s.kill()
        screen.fill("black")
        updatable.update(dt)
        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()
        
        




if __name__ == "__main__":
    main()
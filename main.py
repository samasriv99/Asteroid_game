import pygame
import constants
import logger
from logger import log_state
import circleshape
from circleshape import CircleShape
import player
from player import Player

def main():
    pygame.init()
    clk = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version : {pygame.version.ver}")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    user = Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
    dt=0

    while True:
        logger.log_state()
        user.update(dt)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        user.draw(screen)
        pygame.display.flip()
        dt = clk.tick(60)/1000
        
        


if __name__ == "__main__":
    main()

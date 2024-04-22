import time
import pygame
from pygame.locals import *
import timestep

pgvec2 = pygame.math.Vector2

pygame.init()

RESOLUTION = pygame.math.Vector2(1000, 600)
screen = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("Timestep Test")
SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()

font = pygame.font.SysFont("Calibri", 40)
start = False
start_time = 0


class Player(timestep.Character):
    def __init__(self, x: int, y: int) -> None:
        self.image = pygame.Surface((100, 100))
        self.image.fill("red")
        super().__init__(x, y, self.image)
        self.gravity = pgvec2(0, 0.1)

    def update(self) -> None:
        super().update()

        self.vel.y += self.gravity.y
        self.rect.y += round(self.vel.y)


player = Player(500, 0)


class game_loop(timestep.Timestep):
    def update(self):
        global game_running, start_time, start
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                game_running = False
            if event.type == KEYDOWN:
                if event.key == K_SPACE and not start:
                    start = True
                    start_time = time.time()

        if start:
            player.update()

    def render(self, alpha):
        global game_running

        screen.fill((0, 0, 0))

        player.draw(screen, alpha)

        if player.rect.y >= SCREEN_HEIGHT:
            finish = time.time() - start_time
            print(finish)
            game_running = False

        pygame.display.flip()


game = game_loop(1/60)

game_running = True
while game_running:
    game.run_game()
pygame.quit()

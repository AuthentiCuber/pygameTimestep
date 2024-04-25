import pygame
from pygame.locals import *
import timestep

pygame.init()

RESOLUTION = pygame.math.Vector2(1000, 600)
screen = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("Timestep Test")
SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()


class Player(timestep.Character):
    def __init__(self, x_pos: float, y_pos: float) -> None:
        self.image = pygame.Surface((100, 100))
        self.image.fill("red")
        self.rect = self.image.get_frect()
        super().__init__(x_pos, y_pos, self.image, self.rect)
        self.gravity = pygame.math.Vector2(0, 1)
        self.vel = pygame.math.Vector2(0, 0)
        self.friction = 0.8
        self.jumped = False

    def update(self) -> None:
        super().update()

        self.vel.y += self.gravity.y
        self.vel.x *= self.friction

        keys = pygame.key.get_pressed()
        if keys[K_RIGHT]:
            self.vel.x = 10
        if keys[K_LEFT]:
            self.vel.x = -10
        if keys[K_UP] and not self.jumped:
            self.vel.y = -15
            self.jumped = True

        self.rect.x += self.vel.x
        self.rect.y += self.vel.y

        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.vel.y = 0
            self.jumped = False
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.vel.x = 0
        elif self.rect.left < 0:
            self.rect.left = 0
            self.vel.x = 0


player = Player(500, 0)


class game_loop(timestep.Timestep):
    def update(self):
        global game_running
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                game_running = False

        player.update()

    def render(self, alpha):

        screen.fill((0, 0, 0))

        player.draw(screen, alpha)

        pygame.display.flip()


game = game_loop(1/60)

game_running = True
while game_running:
    game.run_game()
pygame.quit()

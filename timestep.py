"""Timestep is a module based on Pygame that implements a decoupled update and rendering to make any code framerate independant. Based on https://gafferongames.com/post/fix_your_timestep/#the-final-touch. Created so you never have to worry about multiplying by deltatime again."""

import pygame
import time


class Character:
    """Base class for any sprites or objects"""

    def __init__(self,
                 x_pos: float,
                 y_pos: float,
                 image: pygame.Surface,
                 rect: pygame.FRect) -> None:
        self.image = image
        self.rect = rect
        self.rect.topleft = x_pos, y_pos
        self.__pos = pygame.math.Vector2(self.rect.topleft)
        self.__prev_pos = self.__pos

    def update(self) -> None:
        """Override this method with movement, input, collisions etc."""
        self.__prev_pos = self.__get_rect_pos()

    def draw(self, surface: pygame.Surface, alpha: float) -> None:
        """Draw the Character to the screen."""
        self.__pos = self.__prev_pos.lerp(self.__get_rect_pos(), alpha)
        surface.blit(self.image, self.__pos)

    def __get_rect_pos(self) -> pygame.math.Vector2:
        """Return the position of the Charater's rect as a Vec2."""
        return pygame.math.Vector2(self.rect.topleft)


class Timestep:
    """Class that does all the calculations to make the game framerate independent"""

    def __init__(self, step: float) -> None:
        self.__step = step
        self.__accumulator = 0
        self.__last_time = time.time()

    def __calc_dt(self) -> float:
        now = time.time()
        self.dt = now - self.__last_time
        self.__last_time = now
        return self.dt

    def update(self) -> None:
        """Override this function with event loop and movement"""
        pass

    def render(self, alpha: float) -> None:
        """Override this function with blits and drawing of Characters"""
        pass

    def run_game(self) -> None:
        """Updates and renders the game framerate independantly. Should only be called within a while loop."""
        dt = self.__calc_dt()
        self.__accumulator += dt

        while self.__accumulator >= self.__step:
            self.update()

            self.__accumulator -= self.__step

        alpha = self.__accumulator / self.__step

        self.render(alpha)

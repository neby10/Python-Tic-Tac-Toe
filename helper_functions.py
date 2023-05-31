# Author: Nick Eby
# 5.26.2023
# Tic Tac Toe: Helper Functions

import pygame
from constants import GameColors, GameMeasurements as GM

def render_text(screen, text_content, x, y, font_type=None, font_size=36, font_color=GameColors.BLUEISH):
    font = pygame.font.Font(font_type, font_size)
    text_surface = font.render(text_content, True, font_color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)
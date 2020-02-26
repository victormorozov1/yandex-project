import io
import pygame


def convert_image(response_content):
    return pygame.image.load(io.BytesIO(response_content))
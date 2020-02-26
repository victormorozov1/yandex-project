import requests
import sys
import pygame
import os
from convert_image import convert_image


class Map:
    def __init__(self, coords, z, z_change=1):
        self.coords = coords
        self.z = z
        self.z_change = z_change
        self.screen = pygame.display.set_mode((600, 450))

    def get_coords(self, address):
        api_address = 'https://geocode-maps.yandex.ru/1.x'
        api_key = '40d1649f-0493-4b70-98ba-98533de7710b'
        response = requests.get(f'{api_address}/?apikey={api_key}&' +
                                f'geocode={address}, 1&format=json')
        if response:
            response_data = response.json()
            geo_obj = response_data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
            return ','.join(geo_obj["Point"]["pos"].split())
        else:
            print("Ошибка выполнения запроса")
            print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    def get_map(self):
        api_address = "https://static-maps.yandex.ru/1.x/?"
        response = requests.get(f'{api_address}l=map&ll={self.coords}&z={self.z}')
        return convert_image(response.content)

    def move_map(self):
        pass

    def scale_up(self):
        self.z = str(min(13, int(self.z) + self.z_change))

    def scale_down(self):
        self.z = str(max(0, int(self.z) - self.z_change))

    def draw(self):
        self.screen.blit(map.get_map(), (0, 0))
        pygame.display.update()


map = Map('54.689,55.879', '10')
pygame.init()

is_running = True
while is_running:
    map.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        map.scale_up()
    if pressed[pygame.K_DOWN]:
        map.scale_down()


pygame.quit()


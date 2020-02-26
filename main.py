import requests
import sys
import pygame
import os


class Map:
    def __init__(self, coords, scale):
        self.coords = coords
        self.scale = scale

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
        response = requests.get(f'{api_address}l=map&ll={self.coords}&spn={self.scale}')
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
        return map_file

    def move_map(self):
        pass


map = Map('54.689,55.879', '0.1,0.1')
pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map.get_map()), (0, 0))
pygame.display.flip()
is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.MOUSEBUTTONUP:
            if event.key == pygame.K_UP:
                pass
pygame.quit()

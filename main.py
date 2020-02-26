import requests
import sys
import pygame
import os
from convert_image import convert_image


def get_coords(address):
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


def get_map(coords, scale='0.1,0.1'):
    api_address = "https://static-maps.yandex.ru/1.x/?"
    response = requests.get(f'{api_address}l=map&ll={coords}&spn={scale}')
    return convert_image(response.content)


moscow_coords = get_coords('Москва')
pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(get_map(moscow_coords), (0, 0))
pygame.display.flip()
is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
pygame.quit()
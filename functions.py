import requests


def get_request(text):
    api_address = 'https://static-maps.yandex.ru/1.x/'
    api_key = '40d1649f-0493-4b70-98ba-98533de7710b'
    response_text = f'{api_address}/?apikey={api_key}&' + text + "&l=map"
    response_text = 'https://static-maps.yandex.ru/1.x/?l=map&pt=37.6,55.6~37.601,55.6,78~37.602,55.6,pmgrs~37.603,55.6,pm2rdm~37.604,55.6,pmntl100~37.605,55.6,pmors23~37.606,55.6,flag~37.607,55.6,pm2ywl99~37.608,55.6,ya_ru'
    response = requests.get(response_text)
    print(response_text)
    if response:
        #response_data = response.json()
        return response

    print("Ошибка выполнения запроса")


def get_coords(name):
    response = requests.get(
        "http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=" +
        name + "&format=json").json()
    objects = response['response']['GeoObjectCollection']['featureMember']
    for i in objects:
        print('return', i['GeoObject']['Point']['pos'].split(' '))
        return i['GeoObject']['Point']['pos'].split(' ')

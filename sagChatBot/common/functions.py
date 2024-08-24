import requests


def get_random_picture(a):
    endPoint = f'https://{a}.ceo/api/breeds/image/random'
    response = requests.get(endPoint)
    data = response.json()
    return data['message']
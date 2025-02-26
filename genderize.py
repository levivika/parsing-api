import requests



def get_data(name):
    url = f'https://api.genderize.io/?name={name}'
    response = requests.get(url)
    data = response.json()
    return data


def parce_data(data: str):
    name = data.get('name')
    gender = data.get('gender')
    probability = data.get('probability')
    print(name, gender, probability)


name = input('Name: ')
data = get_data(name)
parce_data(data)
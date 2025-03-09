import requests
'''
Дописать программу таким образом, чтобы в случае корректного имени выводилось сообщение
в формате: Имя Elena относится к женскому полу с вероятностью 99%
В случае некорректного имени выводилось сообщение Имя введено не корректно.
'''




def get_data(name):
    url = f'https://api.genderize.io/?name={name}'
    response = requests.get(url)
    data = response.json()
    return data


def parce_data(data: str):
    name = data.get('name')
    gender = data.get('gender')
    probability = data.get('probability')
    inf = (name, gender, probability)
    return inf

def data_to_format(inf):
    name, gender, probability = inf
    if name:
        if gender == 'female':
            gender = 'к женскому полу'
        else:
            gender = 'к мужскому полу'
        if probability:
            probability=int(probability*100)
        text = f'Имя {name} относится {gender} с вероятностью {probability}%'
    else:
        text = 'Имя введено не корректно.'
    return text







name = input('Name: ')
data = get_data(name)
inf = parce_data(data)
print(data_to_format(inf))

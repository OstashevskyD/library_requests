import requests


def superhero_requests():
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url=url)
    return response.json()

if __name__ == '__main__':
    superhero_requests()

super_hero_list = superhero_requests()

for hero in super_hero_list:
    if hero["name"] == "Hulk":
        hulk_param = hero['powerstats']
    if hero["name"] == "Captain America":
        captain_america_param = hero['powerstats']
    if hero["name"] == "Thanos":
        thanos_param = hero['powerstats']


def smartest_superhero():
    if hulk_param['intelligence'] > captain_america_param['intelligence'] \
            and hulk_param['intelligence'] > thanos_param['intelligence']:
        most_smart = 'Hulk'
    if captain_america_param['intelligence'] > hulk_param['intelligence'] \
            and captain_america_param['intelligence'] > thanos_param['intelligence']:
        most_smart = 'Captain America'
    if thanos_param['intelligence'] > hulk_param['intelligence'] \
            and thanos_param['intelligence'] > captain_america_param['intelligence']:
        most_smart = 'Thanos'
    return most_smart

print(f'Самый умный супергерой: {smartest_superhero()}')
import requests
import json

def get_millennium_falcon_pilots():
    url = "https://swapi.dev/api/starships/?search=Millennium%20Falcon"
    response = requests.get(url)
    data = response.json()

    if data['results']:
        falcon_info = data['results'][0]

        pilots_info = []
        for pilot_url in falcon_info['pilots']:
            pilot_response = requests.get(pilot_url)
            pilot_data = pilot_response.json()
            homeworld_response = requests.get(pilot_data['homeworld'])
            homeworld_data = homeworld_response.json()

            pilot_info = {
                "name": pilot_data['name'],
                "height": pilot_data['height'],
                "mass": pilot_data['mass'],
                "homeworld": homeworld_data['name'],
                "homeworld_url": pilot_data['homeworld']
            }
            pilots_info.append(pilot_info)

        falcon_info = {
            "ship-name": falcon_info['name'],
            "starship-class": falcon_info['starship_class'],
            "max_atmosphering_speed": falcon_info['max_atmosphering_speed'],
            "pilots": pilots_info
        }

        print(json.dumps(falcon_info, indent=4))

        with open('millennium_falcon_info.json', 'w') as file:
            json.dump(falcon_info, file, indent=4)

    else:
        print("Корабль Millennium Falcon не найден")


get_millennium_falcon_pilots()

import requests

def get_pokemon(url = 'https://pokeapi.co/api/v2/pokemon-form/', offset=0):
    # Parameters
    args = {'offset': offset} if offset else {}

    # Request
    response = requests.get(url, params=args)
    if response.status_code == 200:
        payload = response.json()
        results = payload.get('results', [])

        if results:
            for pokemon in results:
                name = pokemon['name']
                print(name)

        next = input("¿Continuar listando? [Y/N]? \n").lower()
        if next == 'y':
            get_pokemon(offset=offset+20)

if __name__ == '__main__':
    # URL
    url = 'https://pokeapi.co/api/v2/pokemon-form/'

    # Send GET
    get_pokemon(url)
    

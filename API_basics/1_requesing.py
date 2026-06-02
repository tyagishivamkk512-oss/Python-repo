import requests

base_url = "https://pokeapi.co/api/v2/"

def pokemon_info(name):
    our_url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    our_response = requests.get(our_url)

    if our_response.status_code == 200:
        pokemon_data = our_response.json()
        return pokemon_data

    else:
        print(f"request not found ERROR:{our_response.status_code}")

pokemon_name = "Charizard"
get_pokemon_info = pokemon_info(pokemon_name)

if get_pokemon_info:
    print(f"Name: {get_pokemon_info["name"]}")
    print(f"ID: {get_pokemon_info["id"]}")
    print(f"Height: {get_pokemon_info["height"]}")
    print(f"Weight: {get_pokemon_info["weight"]}")
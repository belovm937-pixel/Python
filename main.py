import requests

token = 'c3f66cc4023579a6dae5ef3e146df0c8'
host = 'https://api.pokemonbattle.ru/v2'

response_post = requests.post(f'{host}/pokemons', json = {
    "name": "Maksim",
    "photo_id": 1
}, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})

print(response_post.json())

response_put = requests.put(f'{host}/pokemons', json = {
    "pokemon_id": "6216",
    "name": "NewName",
    "photo_id": 2
}, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})

print(response_put.json())

response_post_in = requests.post(f'{host}/trainers/add_pokeball', json = {
    "pokemon_id": "6214"
}, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})

print(response_post_in.json())
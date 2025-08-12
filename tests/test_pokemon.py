import requests
import pytest

token = 'c3f66cc4023579a6dae5ef3e146df0c8'
host = 'https://api.pokemonbattle.ru/v2'

def test_status_code():
    response = requests.get(f'{host}/trainers', params= {'trainer_id' : 8279})
    assert response.status_code == 200
    
def test_have_name():
    response = requests.get(f'{host}/trainers', params= {'trainer_id' : 8279})
    assert response.json()['trainer_name'] == 'Максим'
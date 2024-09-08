import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '756ab8a8a2fefceb6bc26e85a2a41bc8'
HEADER = {'Content-Type' : 'application/json',
          'trainer_token' : TOKEN}
body_reg = {
    "trainer_token": TOKEN,
    "email": "lizaburnina@mail.ru",
    "password": "Ezivom10"
}
body_confirm = {
   "trainer_token": TOKEN 
}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 222
}

body_name = {
    "pokemon_id": "69389",
    "name": "New Name",
    "photo_id": 222
}
body_pokeball = {
    "pokemon_id": "69389"
}
'''resonse = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_reg)
print(resonse.text)'''

'''resonse_confirm = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirm )
print(resonse_confirm.text)'''

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create )
print(response_create.text)

message = response_create.json()['message']
print(message)

response_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_name)
print(response_name.text)

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball )
print(response_pokeball.text)
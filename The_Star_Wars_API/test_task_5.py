import requests

base_url = "https://swapi.dev/api/"

"""Getting information about character"""


def get_character(num):
    # Getting url

    url = f'{base_url}people/{num}'

    # Getting json response

    get_result = requests.get(url)
    json_info = get_result.json()

    return json_info


""" Getting information about film """


def get_film(num):
    # Getting url

    url = f'{base_url}films/{num}'

    # Getting json response

    get_result = requests.get(url)
    json_info = get_result.json()

    return json_info


# Getting all films of a character

num_character = 4
films = get_character(num_character)["films"]

# Getting all characters

all_characters = set()

for film in films:
    num_film = film.strip('/').split('/')[-1]
    characters = get_film(num_film)["characters"]
    all_characters.update(characters)

# Getting names of all characters

characters_names = set()

for character in all_characters:
    num_char = character.strip('/').split('/')[-1]
    character_name = get_character(num_char)["name"]
    characters_names.add(character_name)
print(characters_names)

# Writing characters names to a file

with open('characters_names.txt', 'w', encoding='utf-8') as names_file:
    for name in characters_names:
        names_file.write(name + '\n')


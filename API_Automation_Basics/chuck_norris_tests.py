import requests
import json


# GET RANDOM REQUEST

url = 'https://api.chucknorris.io/jokes/random'
print(url)
result = requests.get(url)
print(f'Status code {result.status_code}')
if result.status_code == 200:
    print('Success')
else:
    print('Not valid status code')
print(result.text)
assert (200 == result.status_code)

# GET CATEGORY

category_param = 'food'
url = f'https://api.chucknorris.io/jokes/random?category={category_param}'
result = requests.get(url)

print(f'Status code {result.status_code}')
if result.status_code == 200:
    print('Success')
else:
    print('Not valid code')

result_json_str = result.text
result_json_dict = json.loads(result_json_str)
category_response = result_json_dict['categories']

if ''.join(category_response) == category_param:
    print('Correct category')
else:
    print('Incorrect category')


# GET QUERY

query_request = 'Earth'
url = f'https://api.chucknorris.io/jokes/search?query={query_request}'
result = requests.get(url)

print(f'Status code {result.status_code}')
if result.status_code == 200:
    print('Success')
else:
    print('Not valid code')

print(result.text)

# GET CATEGORIES

url = 'https://api.chucknorris.io/jokes/categories'
result = requests.get(url)

print(f'Status code {result.status_code}')
if result.status_code == 200:
    print('Success')
else:
    print('Not valid code')

print(result.text)


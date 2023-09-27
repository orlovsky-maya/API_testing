import requests


class RandomJoke:

    def __int__(self):
        pass


    def test_new_random_joke(self):
        url = 'https://api.chucknorris.io/jokes/random'
        result = requests.get(url)
        result.encoding = 'utf-8'
        assert (200 == result.status_code), 'Not valid status code'
        print(f'Status code {result.status_code}')

        info_json = result.json()
        category_response = info_json.get('categories')
        assert category_response == [], 'Incorrect category'
        print(f'Correct category: {category_response}')

        value_response = info_json.get('value')
        assert "Chuck" in value_response, '"Chuck" is not in the joke'
        print(f'Random Joke: "{value_response}" contains "Chuck"')

    def test_new_random_category_joke(self):
        category_request = 'food'
        url = f'https://api.chucknorris.io/jokes/random?category={category_request}'
        result = requests.get(url)
        result.encoding = 'utf-8'

        assert result.status_code == 200, 'Not valid status code'
        print(f'Status code  {result.status_code}')

        info_json = result.json()
        category_response = info_json.get('categories')
        assert category_response == category_request.split(), 'Incorrect category'
        print(f'Correct category: {category_response}')

random_joke = RandomJoke()
random_joke.test_new_random_joke()
random_joke.test_new_random_category_joke()

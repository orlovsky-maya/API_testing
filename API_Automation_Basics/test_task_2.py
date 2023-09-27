import requests


class RandomJoke:
    """Creating a new joke """

    def __int__(self):
        pass

    def test_new_random_category_joke(self, category_request):
        url = f'https://api.chucknorris.io/jokes/random?category={category_request}'
        result = requests.get(url)
        result.encoding = 'utf-8'
        print(url)

        # Checking Status code

        assert result.status_code == 200, 'Incorrect status code'
        print(f'Correct status code:  {result.status_code}')

        # Checking category

        info_json = result.json()
        category_response = info_json.get('categories')
        assert category_response == category_request.split(), 'Incorrect category'
        print(f'Correct category: {category_response}')

        # Getting a joke

        joke = info_json.get('value')
        print(f'Joke: {joke}')
        print('----------------------------------------------------------------------------')


"""Getting a list of categories"""

url = 'https://api.chucknorris.io/jokes/categories'
categories = requests.get(url).json()
print(f'All categories: {categories}')

"""Creating a joke for user's category """

category = input().strip()
while True:
    if category in categories:
        random_joke = RandomJoke()
        random_joke.test_new_random_category_joke(category)
        break
    else:
        print(f"{category} category doesn't exist")
        print('Try again')
        category = input().strip()

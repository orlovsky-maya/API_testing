import requests
import json
import os


class TestNewLocation:
    base_url = 'https://rahulshettyacademy.com'
    key = '?key=qaclick123'

    """Creating new location"""

    def test_create_location(self):
        # Getting post url

        post_resource = '/maps/api/place/add/json'
        post_url = self.base_url + post_resource + self.key
        print(post_url)

        # Open json file

        with open('new_location_body.json', 'r', encoding='utf-8') as body_json:
            body_json = json.load(body_json)

        # POST request

        post_result = requests.post(post_url, json=body_json)
        post_result.encoding = 'utf-8'
        print(post_result.text)

        # Checking status_code

        status_code = post_result.status_code
        assert status_code == 200, 'Incorrect status code, status code should be 200'
        print(f'Correct status code: {status_code}')

        # Checking status

        info_json = post_result.json()
        status = info_json.get('status')
        assert status == 'OK', 'Incorrect status, status should be OK'
        print(f'Correct status: {status} ')

        # Getting place_id

        local_place_id = info_json.get('place_id')
        print(f'Place_id: {local_place_id}')

        return local_place_id

    def test_check_location(self, local_place_id):
        """Checking new location """

        # Getting get_url

        get_resource = '/maps/api/place/get/json'
        get_url = self.base_url + get_resource + self.key + '&place_id=' + local_place_id
        print(get_url)

        # GET request

        get_result = requests.get(get_url)
        get_result.encoding = 'utf-8'
        print(get_result.text)

        # Checking status_code

        status_code = get_result.status_code
        assert status_code == 200, 'Incorrect status code, status code should be 200'
        print(f'Correct status code: {status_code}')

        print('New location is created successfully')


location = TestNewLocation()

# Writing place_id to the 'place_id' file
with open('place_id.txt', 'w', encoding='utf-8') as place_id_file:
    for _ in range(5):
        place_id = location.test_create_location()
        location.test_check_location(place_id)

        place_id_file.write(place_id + '\n')

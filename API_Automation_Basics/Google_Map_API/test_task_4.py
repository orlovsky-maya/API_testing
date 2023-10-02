import requests
import json


class TestDeleteLocation:
    base_url = 'https://rahulshettyacademy.com'
    key = '?key=qaclick123'

    def test_delete_location(self, local_place_id):
        """Deleting location"""

        print('_____________________________________________________________________________________')
        print(f'Delete location: {local_place_id}')

        # Getting delete url

        delete_resource = '/maps/api/place/delete/json'
        delete_url = self.base_url + delete_resource + self.key
        print(delete_url)

        # Open json file

        with open('deleting_location_body.json', 'r', encoding='utf-8') as body_json:
            body_json = json.load(body_json)
            body_json['place_id'] = local_place_id

        # DELETE request

        delete_result = requests.get(delete_url, json=body_json)

        # Checking status_code

        status_code = delete_result.status_code
        print(status_code)
        assert status_code == 200, 'Incorrect status code, status code should be 200'
        print(f'Correct status code: {status_code}')

        # Checking message

        info_json = delete_result.json()
        status = info_json.get('status')
        assert status == "OK", 'Incorrect message'
        print(f'Correct success message: {status}')

        return local_place_id

    def test_check_exists_location(self, local_place_id):
        """Checking location """

        print('_________________________________________________________________________________')
        print(f'Check location: {local_place_id}')

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
        assert status_code == 200 or status_code == 404, f'Incorrect status code: {status_code}'
        return True if status_code == 200 else False


location = TestDeleteLocation()

# Open place_id file

with open('place_id.txt', 'r', encoding='utf-8') as place_id_file:
    id_list = [place_id.strip() for place_id in place_id_file.readlines()]
    print(id_list)

# Delete 2 and 4 place_id

for i in range(1, 4, 2):
    place_id = id_list[i]
    assert location.test_check_exists_location(place_id), f"The location with {place_id} doesn't exist"
    print(f"The location with {place_id} exists")
    location.test_delete_location(place_id)
    assert not location.test_check_exists_location(place_id), f"The location with {place_id} isn't deleted"
    print(f"The location with {place_id} is deleted")

# Create new file with existing locations

with open('place_id.txt', 'r', encoding='utf-8') as place_id_file, open('existing_locations.txt', 'w', encoding='utf-8') as existing_locations_file:
    for _ in range(5):
        place_id = place_id_file.readline().strip()
        if location.test_check_exists_location(place_id):
            print(place_id, file=existing_locations_file)
            print(f"The location with {place_id} exists")
        else:
            print(f"The location with {place_id} doesn't exist")
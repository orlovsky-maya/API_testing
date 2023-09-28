import json
import requests

""" CRUD operations for new location"""


class TestNewLocation:
    """Creating new location"""

    def test_create_location(self):
        base_url = 'https://rahulshettyacademy.com'
        key = '?key=qaclick123'

        # Getting post url

        post_resource = '/maps/api/place/add/json'
        post_url = base_url + post_resource + key
        print(post_url)

        """ POST Request - creating new location"""

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

        place_id = info_json.get('place_id')
        print(f'Place_id: {place_id}')

        """GET Request - Checking new location """

        # Getting get_url

        get_resource = '/maps/api/place/get/json'
        get_url = base_url + get_resource + key + '&place_id=' + place_id
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

        """Updating new location"""

        """PUT Request - updating location"""

        # Getting put url

        put_resource = '/maps/api/place/update/json'
        put_url = base_url + put_resource + key
        print(put_url)

        # Open json file

        with open('update_location_body.json', 'r', encoding='utf-8') as body_json:
            body_json = json.load(body_json)
            body_json['place_id'] = place_id

        # PUT Request

        put_result = requests.put(put_url, json=body_json)

        # Checking status_code

        status_code = put_result.status_code
        assert status_code == 200, 'Incorrect status code, status code should be 200'
        print(f'Correct status code: {status_code}')

        # Checking message

        info_json = put_result.json()
        message_success = info_json.get('msg')
        assert message_success == 'Address successfully updated', 'Incorrect message'
        print(f'Correct success message: {message_success}')

        """GET Request - Checking updated location """

        # GET request

        print(get_url)
        get_result = requests.get(get_url)
        get_result.encoding = 'utf-8'
        print(get_result.text)

        # Checking status_code

        status_code = get_result.status_code
        assert status_code == 200, 'Incorrect status code, status code should be 200'
        print(f'Correct status code: {status_code}')

        # Checking new address

        info_json = get_result.json()
        address = info_json.get('address')
        assert address == '100 Lenina street, RU', 'Incorrect new address'
        print(f'New address of location: {address}')
        print('The location is updated successfully')

        """Deleting new location"""

        """DELETE Request - deleting location"""

        # Getting delete url

        delete_resource = '/maps/api/place/delete/json'
        delete_url = base_url + delete_resource + key
        print(delete_url)

        # Open json file

        with open('deleting_location_body.json', 'r', encoding='utf-8') as body_json:
            body_json = json.load(body_json)
            body_json['place_id'] = place_id

        # DELETE request

        delete_result = requests.get(delete_url, json=body_json)

        # Checking status_code

        status_code = delete_result.status_code
        assert status_code == 200, 'Incorrect status code, status code should be 200'
        print(f'Correct status code: {status_code}')

        # Checking message

        info_json = delete_result.json()
        status = info_json.get('status')
        assert status == "OK", 'Incorrect message'
        print(f'Correct success message: {status}')
        print('Location is deleted successfully')

        """GET Request - Checking deleted location """

        # Getting get url

        get_url = base_url + get_resource + key + '&place_id=' + place_id
        print(get_url)

        # GET request

        get_result = requests.get(get_url)
        get_result.encoding = 'utf-8'
        print(get_result.text)

        # Checking status_code

        status_code = get_result.status_code
        assert status_code == 404, 'Incorrect status code, status code should be 404'
        print(f'Correct status code: {status_code}')

        # Checking message

        info_json = get_result.json()
        message_success = info_json.get('msg')
        assert message_success == "Get operation failed, looks like place_id  doesn't exists", 'Incorrect message'
        print(f'Correct success message: {message_success}')

        """Updating non-existent location"""

        """PUT Request - updating non-existent location"""

        # Getting put url

        put_resource = '/maps/api/place/update/json'
        put_url = base_url + put_resource + key
        print(put_url)

        # Open json file

        with open('update_location_body.json', 'r', encoding='utf-8') as body_json:
            body_json = json.load(body_json)
            body_json['place_id'] = place_id

        # PUT Request

        put_result = requests.put(put_url, json=body_json)

        # Checking status_code

        status_code = put_result.status_code
        assert status_code == 404, 'Incorrect status code, status code should be 404'
        print(f'Correct status code: {status_code}')

        # Checking message

        info_json = put_result.json()
        message_success = info_json.get('msg')
        assert message_success == "Update address operation failed, looks like the data doesn't exists", \
            'Incorrect message'
        print(f'Correct success message: {message_success}')


location = TestNewLocation()
location.test_create_location()

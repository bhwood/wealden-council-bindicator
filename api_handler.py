import requests
import json

def get_collection_data(uprn):
    url = "https://www.wealden.gov.uk/wp-admin/admin-ajax.php"

    headers = {
    }

    data = {
        'action': 'wealden_get_collections_for_uprn',
        'uprn': uprn
    }


    response = requests.post(url, headers=headers, data=data)
    try:
        json_data = response.json()
        return json_data

    except json.JSONDecodeError:
        print("Response is not in JSON format")

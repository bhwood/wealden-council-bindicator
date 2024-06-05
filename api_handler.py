import requests

def get_collection_data(uprn):
    url = "https://www.wealden.gov.uk/wp-admin/admin-ajax.php"

    headers = {
    }

    data = {
        'action': 'wealden_get_collections_for_uprn',
        'uprn': uprn
    }


    response = requests.post(url, headers=headers, data=data)
    return response
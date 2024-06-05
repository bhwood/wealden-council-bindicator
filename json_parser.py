from api_handler import get_collection_data
import json


def json_parser(uprn):
    try:
        json_data = get_collection_data(uprn).json()
        return json_data

    except json.JSONDecodeError:
        print("Response is not in JSON format")

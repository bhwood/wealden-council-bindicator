import requests
import json
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

uprn = os.getenv('UPRN')


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

def days_until(date):
    today = datetime.now().date()
    return (date - today).days

def which_is_next(bin_day, recycling_day):
    days_until_bin = days_until(bin_day)
    days_until_recycling = days_until(recycling_day)
    if days_until_bin < days_until_recycling:
        next_collection = "Black Bin"
        next_date = bin_day
    else:
        next_collection = "Green Bin"
        next_date = recycling_day
    return {'nextCollection': next_collection, 'nextDate': next_date.strftime("%d/%m/%Y")}

    
def date_formatter(date_to_format):
    return date_to_format.strftime("%d/%m/%Y")
    

def next_bin_date(json_data):
    next_bin_date = json_data['collection']['refuseCollectionDate']
    bin_date_obj = datetime.fromisoformat(next_bin_date)
    bin_date = bin_date_obj.date()
    return bin_date

def next_recycling_date(json_data):
    next_recycling_date = json_data['collection']['recyclingCollectionDate']
    recycling_date_obj = datetime.fromisoformat(next_recycling_date)
    recycling_date = recycling_date_obj.date()
    return recycling_date

def json_result(json_data):
    result = which_is_next(next_bin_date(json_data), next_recycling_date(json_data))
    return json.dumps(result, indent=4)

def next_collection(json_data):
    result = which_is_next(next_bin_date(json_data), next_recycling_date(json_data))
    return f"Your next collection is for the {result['nextCollection']} on the {result['nextDate']}"


try:
    json_data = get_collection_data(uprn).json()
    print(f'Your next bin collection date is {date_formatter(next_bin_date(json_data))}')
    print(f'Your next recycling collection date is {date_formatter(next_recycling_date(json_data))}')
    print(next_collection(json_data))
    print(json_result(json_data))
    
        
except json.JSONDecodeError:
    print("Response is not in JSON format")
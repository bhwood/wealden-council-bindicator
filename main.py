from utils import *
from api_handler import get_collection_data
import os
from dotenv import load_dotenv

load_dotenv()

uprn = os.getenv('UPRN')


print(f'Your next bin collection date is {date_formatter(next_bin_date(get_collection_data(uprn)))}')
print(f'Your next recycling collection date is {date_formatter(next_recycling_date(get_collection_data(uprn)))}')
print(next_collection(get_collection_data(uprn)))
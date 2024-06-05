from utils import *
from json_parser import json_parser
import os
from dotenv import load_dotenv

load_dotenv()

uprn = os.getenv('UPRN')


print(f'Your next bin collection date is {date_formatter(next_bin_date(json_parser(uprn)))}')
print(f'Your next recycling collection date is {date_formatter(next_recycling_date(json_parser(uprn)))}')
print(next_collection(json_parser(uprn)))
print(json_result(json_parser(uprn)))
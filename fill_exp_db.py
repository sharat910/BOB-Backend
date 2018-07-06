import requests
from pprint import pprint
import datetime
import random

ROOT_URL = 'http://localhost:8000/'

def random_date(start, end):
    """Generate a random datetime between `start` and `end`"""
    return start + datetime.timedelta(
        # Get a random amount of seconds between `start` and `end`
        seconds=random.randint(0, int((end - start).total_seconds())),
    )

def fetch_and_print(url):
    text = requests.get(url).text
    try:
        pprint(eval(text))
    except:
        print(text)

def insert_dummy_expenditures():
    url = ROOT_URL + 'api/expenditure/'
    desc_choices = ["Petrol","Electricity","Stationary",
    "Cleaning","Loan payback"]
    for i in range(100):

        data = {'voucher_id': i,
                'description': random.choice(desc_choices),
                'date': random_date(datetime.date(2018,5,1),
                datetime.date.today()).strftime("%Y-%m-%d"),
                'amount':random.choice(range(0,5000,100))}

        pprint(data)
        r = requests.post(url, json=data)

    # print("Fetching Fee rate from db...")
    # fetch_and_print(url)


if __name__ == '__main__':
    insert_dummy_expenditures()

import requests
from pprint import pprint
from main.choices import *
import ast

ROOT_URL = 'http://localhost:8000/'

def fetch_and_print(url):
    text = requests.get(url).text
    try:
        pprint(eval(text))
    except:
        print(text)

def load_months():
    print("\n\nLoading months into db...")
    url = ROOT_URL + 'api/month/'
    for month in MONTHS:
        data = {"month": month[0]}
        r = requests.post(url, json=data)

    print("Fetching months from db...")
    fetch_and_print(url)

def load_levels():
    print("\n\nLoading levels into db...")
    url = ROOT_URL + 'api/level/'
    for level in LEVEL_CHOICES:
        data = {"level": level[0]}
        r = requests.post(url, json=data)

    print("Fetching levels from db...")
    fetch_and_print(url)

def load_rates():
    print("\n\nLoading Salary rate into db...")
    url = ROOT_URL + 'api/salaryrate/'
    data = {'salary_rate': 125}
    r = requests.post(url, json=data)
    print("Fetching Salary rate from db...")
    fetch_and_print(url)

    print("\n\nLoading Fee rate into db...")
    url = ROOT_URL + 'api/feerate/'
    data = {'month_fee': 900,
            'level_fee': 2700,
            'exam_fee': 200,
            'registration_fee':950}
    r = requests.post(url, json=data)
    print("Fetching Fee rate from db...")
    fetch_and_print(url)

    print("\n\nLoading Royalty rate into db...")
    url = ROOT_URL + 'api/royaltyrate/'
    data = {'month_royalty': 270,
            'level_royalty': 810,
            'exam_royalty': 200,
            'registration_royalty':860}
    r = requests.post(url, json=data)
    print("Fetching Royalty rate from db...")
    fetch_and_print(url)

def load_teacher():
    print("\n\nLoading teacher into db...")
    url = ROOT_URL + 'api/teacher/'
    data = {
    "name": "Renuka",
    "phone": "9440751422",
    "email": "renuka@gmail.com",
    "trained_max_level": 10
    }
    r = requests.post(url, json=data)
    print("Fetching teachers from db...")
    fetch_and_print(url)

def load_batch():
    print("\n\nLoading batch into db...")
    url = ROOT_URL + 'api/batch/'
    data = {
        "timing": "9AM-11AM",
        "day": "Saturday",
        "level_start_date": "2018-05-12",
        "level": 1,
        "teacher": 1,
    }
    r = requests.post(url, json=data)
    print(r.text,"\n")
    print("Fetching batches from db...")
    fetch_and_print(url)

def load_parent():
    print("\n\nLoading parent into db...")
    url = ROOT_URL + 'api/parent/'
    data = {
    "name": "Chandra Shekhar",
    "phone": "9494410800",
    "email": "cs_aai@yahoo.co.in",
    "parent_type": "Father"
    }
    r = requests.post(url, json=data)
    print("Fetching parents from db...")
    fetch_and_print(url)

def load_student():
    print("\n\nLoading student into db...")
    url = ROOT_URL + 'api/student/'
    data = {
    "name": "Nikhil",
    "date_of_birth": "2000-11-28",
    "date_of_joining": "2018-05-12",
    "performance_rating": "High",
    "dropped": False,
    "date_dropped": None,
    "t_shirt_size": "XL",
    "photo": None,
    "batch": 1,
    "father_name": "M Chandra Shekhar",
    "mother_name": "M Renuka",
    "phone": "+919440751422",
    "alt_phone": "+919494410800",
    "email": "nkhl2811@gmail.com",
    }
    r = requests.post(url, json=data)
    print(r.text,"\n")
    print("Fetching students from db...")
    fetch_and_print(url)

def load_exam_result():
    print("\n\nLoading examresult into db...")
    url = ROOT_URL + 'api/examresult/'
    data = {
    "score": 480,
    "max_score": 500,
    "student": 1,
    "level": 1,
    "date_of_exam":"2018-08-11"
    }
    r = requests.post(url, json=data)
    print("Fetching examresult from db...")
    fetch_and_print(url)

def load_feerecord():
    print("\n\nLoading feerecord into db...")
    url = ROOT_URL + 'api/feerecord/'
    data = {
    "fee_type": "Level",
    "fee_amount": 2150,
    "fee_receipt_no": 123,
    "student": 1,
    "level": 1,
    "months": [5,6,7],
    "date_of_payment": "2018-06-15"
    }
    r = requests.post(url, json=data)
    print("Fetching feerecord from db...")
    fetch_and_print(url)

def load_salaryrecord():
    print("\n\nLoading salaryrecord into db...")
    url = ROOT_URL + 'api/salaryrecord/'
    data = {
    "salary_type": "Level",
    "salary_amount": 375,
    "teacher": 1,
    "level": 1,
    "batch":1,
    "months": [5,6,7],
    "date_of_payment": "2018-06-15"
    }
    r = requests.post(url, json=data)
    print(r.text,"\n")
    print("Fetching salaryrecord from db...")
    fetch_and_print(url)

def load_all():
    load_months()
    load_levels()
    load_rates()
    load_teacher()
    load_batch()
    #load_parent()
    load_student()
    load_exam_result()
    load_feerecord()
    load_salaryrecord()

if __name__ == '__main__':
    load_all()
    # load_student()
    # load_exam_result()
    # load_feerecord()

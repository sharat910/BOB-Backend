import sys
import requests

main_url = 'http://localhost:8000/api/'

def fetch_and_print(url):
    text = requests.get(url).text    
    try:
        pprint(eval(text))
    except:
        print(text)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        if sys.argv[1] == 'get':
            url = "%s%s/" % (main_url, sys.argv[2])
            fetch_and_print(url)
        else:
            print("Invalid Command")
    else:
        print("Require 2 Args")
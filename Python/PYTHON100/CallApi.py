import requests

url= "https://official-joke-api.appspot.com/random_joke"

def get_data_api():

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print("Error calling API ", response.status_code)

get_data_api()
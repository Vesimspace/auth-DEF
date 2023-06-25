import requests
from pprint import pprint

def costumer():
    credentials = {
        'username': 'Test_rest',
        'email': 'test@gmail.com',
        'password1': '123vesim123',
        'password2': '123vesim123'
    }

    response = requests.post(
        url = 'http://127.0.0.1:8000/api/rest-auth/registration/',
        data = credentials,
    )

    print('Status Code:', response.status_code)

    response_data = response.json()
    pprint(response_data)

if __name__ == '__main__':
    costumer()
import requests
from pprint import pprint

def costumer():
    token = 'Token ba978fae4990d989493f9949a762f9e84287d221'

    headers = {
        'Authorization': token,
    }

    response = requests.get(
        url = 'http://127.0.0.1:8000/api/user-accounts/',
        headers = headers,
    )

    print('Status Code:', response.status_code)

    response_data = response.json()
    pprint(response_data)

if __name__ == '__main__':
    costumer()
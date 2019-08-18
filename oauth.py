import requests

# Github Oauth https://github.com/settings/applications/
client_id = 'yout_client_id'
client_secret = 'your_secret_id'
url = 'https://github.com/login/oauth/authorize?client_id={}&scope=repo'.format(client_id)
code = 'your_code_generete'
access_token = 'yout_access_token'

def generate_access_token():
    # UR
    url = 'https://github.com/login/oauth/access_token'

    # Header Send
    headers = { 'Accept': 'application/json' }

    # Data Send
    payload = {'client_id': client_id, 'client_secret': client_secret, 'code': code }

    # Request
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        response_json = response.json()
        access_token = response_json['access_token']
        print(access_token)

def get_info_user_repo():
    # URL
    url = 'https://api.github.com/user/repos'
    
    # Headers Send
    headers = { 'Authorization': 'token {}'.format(access_token) }

    # Send Request
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        payload = response.json()

        for project in payload:
            name = project['name']
            print(name)
    else:
        print(response.content)

def user_create_repo():
    # URL
    url = 'https://api.github.com/user/repos'

    # Headers Send
    headers = { 'Accept': 'application/json', 'Authorization': 'token {}'.format(access_token) }

    # Data Send
    payload = { 'name': 'consumo-api-python' }
    # Send Request
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        print(response.json())
    else:
        print(response.content)
    
if __name__ == '__main__':

    # Generate URL with Client ID, Get CODE
    print(url)
    
    # Get Access Token
    # generate_access_token()

    # Get Info User Repo
    # get_info_user_repo()

    # Create Repository
    # user_create_repo()

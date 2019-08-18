import requests

def get_cookies():
    # URL
    url = 'http://httpbin.org/cookies'

    # Cookies Send
    cookies = { 'my-cookie': 'true' }

    # Request
    response = requests.get(url, cookies=cookies)
    
    if response.ok: # OR response.status_code == 200
        cookies = response.cookies
        print(cookies)

        print('El contenido es => ')
        print(response.content)

if __name__ == '__main__':

    # Send Request
    get_cookies()
        
        

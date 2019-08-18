import requests

def session_init():
    # URL
    url = 'https://api.github.com/user'

    session = requests.session()
    session.auth = ( 'your_email_account', 'your_password' )

    response = session.get(url)
    if response.ok:
        response = session.get('https://github.com/your_user')
        if response.ok:
            # Get Cookies
            print(response.cookies) # cookies['_gh_sess'] 
    else:
        print(response.content)

if __name__ == '__main__':
    session_init()
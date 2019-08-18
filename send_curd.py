import requests
import json

if __name__ == "__main__":
    def send_get():
        print('Request GET =>>>>>>>>========>>>>>>>>>')
        # URL
        url = 'http://httpbin.org/get'

        # Data
        args = {'Nombre': 'Jose Romero', 'Curso': 'Python', 'Nivel': 'Intermedio'}
        response = requests.get(url, params=args)
        print('URL ==>> {}'.format(response.url))

        if response.status_code == 200:
            # content = response.content
            """ response_json = response.json()
            origin = response_json['origin']
            print(origin) """

            # Serializado
            response_json = json.loads(response.text)
            origin = response_json['origin']
            print(origin)
    
    def send_post():
        print('Request POST =>>>>>>>>========>>>>>>>>>')
        # URL
        url = 'http://httpbin.org/post'
        
        # Headers
        headers = {'Content-type': 'aplication/json', 'Access-Token': 'lkasjdlkajsdlasuo234234kasdasd3q234asdw324wf'}

        # Data
        payload = {'Nombre': 'Jose Romero', 'Curso': 'Python', 'Nivel': 'Intermedio'}
                
        # Send Type Paramas => json=payload , data=payload, json.dumps(payload)
        response = requests.post(url, json=payload, headers=headers)
        print('URL ==>> {}'.format(response.url))

        if response.status_code == 200:
            response_josn = json.loads(response.text)
            # Get Headers
            # response_headers = response.headers
            # server = response_headers['Server']
            print(response_josn)
    
    def send_put():
        print('Request PUT =>>>>>>>>========>>>>>>>>>')
        # URL
        url = 'http://httpbin.org/put'
        
        # Headers
        headers = {'Content-type': 'aplication/json', 'Access-Token': 'lkasjdlkajsdlasuo234234kasdasd3q234asdw324wf'}

        # Data
        payload = {'Nombre': 'Jose Romero', 'Curso': 'Python', 'Nivel': 'Intermedio'}
                
        # Send Type Paramas => json=payload , data=payload, json.dumps(payload)
        response = requests.put(url, json=payload, headers=headers)
        print('URL ==>> {}'.format(response.url))

        if response.status_code == 200:
            response_josn = json.loads(response.text)
            # Get Headers
            # response_headers = response.headers
            # server = response_headers['Server']
            print(response_josn)

    def send_delete():
        print('Request DELETE =>>>>>>>>========>>>>>>>>>')
        # URL
        url = 'http://httpbin.org/delete'
        
        # Headers
        headers = {'Content-type': 'aplication/json', 'Access-Token': 'lkasjdlkajsdlasuo234234kasdasd3q234asdw324wf'}
        args = {'id': 345}       
        # Send Type Paramas => json=payload , data=payload, json.dumps(payload)
        response = requests.put(url, params=args, headers=headers)
        print('URL ==>> {}'.format(response.url))

        if response.status_code == 200:
            response_josn = json.loads(response.text)
            # Get Headers
            # response_headers = response.headers
            # server = response_headers['Server']
            print(response_josn)

    # Send Data GET
    send_get()

    # Send Data POST
    send_post()

    # Send Data PUT
    send_put()

    # Send Data DELETE
    send_delete()
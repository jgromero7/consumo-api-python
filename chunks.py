import requests
import json
import sys
import time

if __name__ == "__main__":
    def donwload_img():
        print('Request GET =>>>>>>>>========>>>>>>>>>')
        # URL
        url = 'https://images.pexels.com/photos/45246/green-tree-python-python-tree-python-green-45246.jpeg?crop=entropy&cs=srgb&dl=animal-close-up-green-45246.jpg&fit=crop&fm=jpg&h=1400&w=2100'

        # Request ==> stream=True - Realiza la petición sin descargar
        response = requests.get(url, stream=True)
        print('URL ==>> {}'.format(response.url))

        count = 1
        block_size = 512
        total_size = int(response.headers.get('content-length'))
        with open('img_name.jpg', 'wb') as file:
            for chunk in response.iter_content(chunk_size=block_size): # Descarga el Contentido poco a poco
                file.write(chunk)
                percentage_progress(count, block_size, total_size)
                count += 1
        print('')
        print('Donwload Complete!')
        response.close()

    def percentage_progress(count, block_size, total_size):
        total = 100
        percent = int(count * block_size * total / total_size)
        text = '\rDownload Progress: [{0}] {1}% - {2}%'.format( '#' * percent + ' '*(total-percent), percent, total)
        sys.stdout.write(text) 
        sys.stdout.flush()


    # Donwload img
    donwload_img()
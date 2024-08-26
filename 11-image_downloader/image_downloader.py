import os
import requests


def get_extension(image_url: str) -> str | None:
    extension: list[str] = ['.png', '.jpg', '.jpeg', '.gif', '.svg']

    for ext in extension:
        if ext in image_url:
            return ext


def download_image(image_url: str, name: str, folder: str = None):
    if ext := get_extension(image_url):
        if folder:
            image_name: str = f'{folder}/{name}{ext}'  # images/app.jpg
        else:
            image_name: str = f'{name}{ext}'  # app.jpg
    else:
        raise Exception('Image extension not found')

    if os.path.isfile(image_name):
        raise Exception('File name already exists')

    try:
        image_content: bytes = requests.get(image_url).content
        with open(image_name, 'wb') as handler:
            handler.write(image_content)
            print(f'Downloaded "{image_name}" successfully')
    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    input_url: str = input('Input image url: ')
    input_name: str = input('Input image name: ')

    print('Downloading...')
    download_image(input_url, name=input_name, folder='images')

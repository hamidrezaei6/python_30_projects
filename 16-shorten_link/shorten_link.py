from typing import Final
import requests

API_KEY: Final[str] = "e78fcbcd8457cd705f0c075633fd3908"
BASE_URL: Final[str] = "https://cutt.ly/api/api.php"


def shorten_link(full_link: str):
    payload: dict = {'key': API_KEY, 'short': full_link, }
    request = requests.get(BASE_URL, params=payload)
    data: dict = request.json()

    if url_data := data.get('url'):
        if url_data['status'] == 7:
            short_link: str = url_data['shortLink']
            print('Link:', short_link)
        else:
            print('Error Status:', url_data['status'])


def main():
    link: str = input('Enter link: ')

    shorten_link(link)


if __name__ == '__main__':
    main()

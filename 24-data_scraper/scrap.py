import requests
import bs4


def get_html(course_id: int) -> str:
    url = f'https://toplearn.com/c/{course_id}'
    response = requests.get(url)
    return response.text


def get_title_from_toplearn(html: str) -> str:
    soup = bs4.BeautifulSoup(html, 'html.parser')
    header = soup.select_one('.right-side h1')
    if not header:
        return 'There is no course'
    return header.text.strip()


for course_id in range(6110, 6159):
    html = get_html(course_id)
    title = get_title_from_toplearn(html)
    print(title)

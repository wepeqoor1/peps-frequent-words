import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    url = 'https://quotes.toscrape.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('span', class_='text')

    print(quotes)
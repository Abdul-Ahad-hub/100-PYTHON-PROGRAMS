import requests
from bs4 import BeautifulSoup

response = requests.get("https://quotes.toscrape.com/")

soup = BeautifulSoup(response.text, 'html.parser')

def print_webpage():
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')

    for quote, author in zip(quotes, authors):
        print(f"{quote.text} - {author.text}")

print_webpage()
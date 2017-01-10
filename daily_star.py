import requests
from bs4 import BeautifulSoup
daily_star =  requests.get('http://www.thedailystar.net')
parsed_html = BeautifulSoup(daily_star.text, 'lxml')
headlines = parsed_html.find_all('h5')

for headline in headlines:
    if len(headline.text.strip()) > 0:
        print(headline.text.strip())

import requests
from bs4 import BeautifulSoup


def index_url(max_pages):
	page = 1
	while page <= max_pages:
		url = 'http://krunal-panchal.one/' + str(page)
		source_code = requests.get(url)
		plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
		for link in soup.findAll('a'):
			href = "http://krunal-panchal.one/" + link.get('href')
            title = link.string
			print(href)
            print(title)
            level_down_url(href)
		page += 1
# Above Function grabe the link which is under the anchor tag, and it also grabe the description.         
        
def level_down_url(item_url):
	source_code = requests.get(item_url)
	plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.findAll('a'):
        href = "http://krunal-panchal.one/" + link.get('href')
        print(href)
# Above Function grabe the link which is under the anchor tag level under the links which is grabed from above function, and it also grabe the description. 
    
trade_spider(1)

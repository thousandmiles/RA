from bs4 import BeautifulSoup
import requests

url = 'https://www.rockwellautomation.com/en-us/products.html'

response = requests.get(url)

res = BeautifulSoup(response.text, 'lxml')

class_list = res.find_all(attrs={'class': 'ff-primary-bold-rte subheading-3 color-factory-talk-blue'})

teaser__text_content = res.find_all(attrs={'class': 'teaser__text-content'})


length = len(teaser__text_content)

for i in range(length):
    _content = teaser__text_content[i]
    if _content.find(attrs = {'class': 'teaser__text'}):
        text = _content.find(attrs = {'class': 'teaser__text'}).get_text().strip()
        title = _content.find(attrs = {'class': 'teaser__title'}).get_text().strip()
        print( title, "-----", text)



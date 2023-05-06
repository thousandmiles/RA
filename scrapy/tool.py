from bs4 import BeautifulSoup
import requests


def GetBannerInfo(url):
    print('--------------------')
    print('URL = ',url)

    s_response = requests.get(url)
    s_res = BeautifulSoup(s_response.text, 'lxml')
    
    info = s_res.find(attrs = {'class': 'hero-banner__content'})
    if info is None:
        return

    banner__header = info.find(attrs = {'class': 'hero-banner__header'}).get_text().strip()
    if banner__header is None:
        return
    print('Header = ', banner__header)

    banner__description = info.find(attrs = {'class': 'hero-banner__description subheading-1'}).get_text().strip()
    if banner__description is None:
        return
    print('Description = ', banner__description)

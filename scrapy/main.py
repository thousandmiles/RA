from bs4 import BeautifulSoup
import requests
import tool

all_products_url = 'https://www.rockwellautomation.com/en-us/products.html'

response = requests.get(all_products_url)

res = BeautifulSoup(response.text, 'lxml')

# All Software

all_soft = []

class_list = res.find_all(
    attrs={'class': 'generic-container push-top-full push-bottom-full aem-GridColumn aem-GridColumn--default--12'})

for child in class_list:
    text = child.find_all(attrs={'class': 'teaser__text'})
    title = child.find_all(attrs={'class': 'teaser__title'})
    ref = child.find_all('a')
    class_ = child.find(attrs={
                        'class': 'ff-primary-bold-rte subheading-3 color-factory-talk-blue'}).get_text().strip()

    for i in range(len(text)):
        text_ = text[i].get_text().strip()
        title_ = title[i].get_text().strip()
        ref_ = ref[i]['href'].strip()

        soft_info = tool.Software(class_, title_, text_, ref_)
        soft_info.CompleteURL()
        soft_info.GetBannerInfo()
        all_soft.append(soft_info)

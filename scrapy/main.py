from bs4 import BeautifulSoup
import requests

all_products_url = 'https://www.rockwellautomation.com/en-us/products.html'

response = requests.get(all_products_url)

res = BeautifulSoup(response.text, 'lxml')

# All Software 

all_soft = [] 

class_list = res.find_all(attrs={'class': 'generic-container push-top-full push-bottom-full aem-GridColumn aem-GridColumn--default--12'})

for child in class_list:
    text = child.find_all(attrs = {'class': 'teaser__text'})
    title = child.find_all(attrs = {'class': 'teaser__title'})
    ref = child.find_all('a')
    class_ = child.find(attrs={'class': 'ff-primary-bold-rte subheading-3 color-factory-talk-blue'}).get_text().strip()
    
    for i in range(len(text)):
        text_ = text[i].get_text().strip()
        title_ = title[i].get_text().strip()
        ref_ = ref[i]['href'].strip()

        # if ref_.startswith("/en"):
        #     ref_ = "https://www.rockwellautomation.com" + ref_

        soft_info = [class_, title_, text_, ref_]
        all_soft.append(soft_info)

for item in all_soft:
    for i in item:
        print(i)
    print("----------------")

# Single software

# banner__header & banner__description
single_software_url = 'https://www.rockwellautomation.com/en-us/products/software/factorytalk/operationsuite/metrics.html'
s_response = requests.get(single_software_url)
s_res = BeautifulSoup(s_response.text, 'lxml')
info = s_res.find(attrs = {'class': 'hero-banner__content'})

banner__header = info.find(attrs = {'class': 'hero-banner__header'}).get_text().strip()
banner__description = info.find(attrs = {'class': 'hero-banner__description subheading-1'}).get_text().strip()

print(banner__header)
print(banner__description)
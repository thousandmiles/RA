from bs4 import BeautifulSoup
import requests

# url = 'https://www.rockwellautomation.com/en-us/products.html'

# response = requests.get(url)

# res = BeautifulSoup(response.text, 'lxml')

# class_list = res.find_all(attrs={'class': 'ff-primary-bold-rte subheading-3 color-factory-talk-blue'})

# teaser__text_content = res.find_all(attrs={'class': 'teaser__text-content'})


# length = len(teaser__text_content)

# for i in range(length):
#     _content = teaser__text_content[i]
#     if _content.find(attrs = {'class': 'teaser__text'}):
#         text = _content.find(attrs = {'class': 'teaser__text'}).get_text().strip()
#         title = _content.find(attrs = {'class': 'teaser__title'}).get_text().strip()
#         print( title, "-----", text)


# single_software_url = 'https://www.rockwellautomation.com/en-us/products/software/factorytalk/operationsuite/metrics.html'

# s_response = requests.get(single_software_url)

# s_res = BeautifulSoup(s_response.text, 'lxml')

# info = s_res.find(attrs={'class': 'hero-banner__content'})

# banner__header = info.find(
#     attrs={'class': 'hero-banner__header'}).get_text().strip()

# banner__description = info.find(
#     attrs={'class': 'hero-banner__description subheading-1'}).get_text().strip()

# print(banner__header)
# print(banner__description)

ref_ = 'https://www.plex.com/products/production-monitoring'
print('URL = ', ref_)
response = requests.get(ref_)
res = BeautifulSoup(response.text, 'lxml')

content_bg = res.find(
    attrs={'class': 'innerHeroSection absolute-image-right'})
print(content_bg)
x = content_bg.find(attrs={
                    'class': 'media media--blazy media--fx media--fx-lg media--image media--responsive is-b-loaded is-b-animated'})

print(x)
if content_bg is not None:
    bg_url = x['src'].strip()

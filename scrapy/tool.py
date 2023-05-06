from bs4 import BeautifulSoup
import requests


class Software(object):

    def __init__(self, class_, title_, text_, ref_):
        self.class_ = class_
        self.title_ = title_
        self.text_ = text_
        self.ref_ = ref_

    def CompleteURL(self):
        if self.ref_.startswith("/en"):
            self.ref_ = "https://www.rockwellautomation.com" + self.ref_

    def GetBannerInfo(self):
        print('--------------------')
        print('URL = ', self.ref_)

        s_response = requests.get(self.ref_)
        s_res = BeautifulSoup(s_response.text, 'lxml')

        info = s_res.find(attrs={'class': 'hero-banner__content'})
        if info is None:
            return

        self.banner__header = info.find(
            attrs={'class': 'hero-banner__header'}).get_text().strip()
        if self.banner__header is None:
            return
        print('Header = ', self.banner__header)

        self.banner__description = info.find(
            attrs={'class': 'hero-banner__description subheading-1'}).get_text().strip()
        if self.banner__description is None:
            return
        print('Description = ', self.banner__description)

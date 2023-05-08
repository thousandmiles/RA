from bs4 import BeautifulSoup
import requests


class Software(object):

    def __init__(self, class_, title_, text_, ref_):
        self.class_ = class_
        self.title_ = title_
        self.text_ = text_
        self.ref_ = ref_
        self.banner__header = title_
        self.banner__description = text_

    def CompleteURL(self):
        if self.ref_.startswith("/en"):
            self.ref_ = "https://www.rockwellautomation.com" + self.ref_

    def GetBannerInfo(self):

        s_response = requests.get(self.ref_)
        s_res = BeautifulSoup(s_response.text, 'lxml')

        info = s_res.find(attrs={'class': 'hero-banner__content'})
        if info is None:
            return

        self.banner__header = info.find(
            attrs={'class': 'hero-banner__header'}).get_text().strip()
        if self.banner__header is None:
            return

        self.banner__description = info.find(
            attrs={'class': 'hero-banner__description subheading-1'}).get_text().strip()
        if self.banner__description is None:
            return

    def GetBackgroundImage(self):
        print('URL = ', self.ref_)
        self.bg_url = ''
        response = requests.get(self.ref_)
        res = BeautifulSoup(response.text, 'lxml')
        content_bg = res.find(attrs={'class': 'main-image'})
        if content_bg is not None:
            self.bg_url = content_bg['src'].strip()
            if (self.bg_url.endswith('.jpg') or self.bg_url.endswith('.jpeg') or self.bg_url.endswith('.png')):
                pass
            else:
                self.bg_url = ''

        print(self.bg_url)

    def PrintInfo(self):
        print('--------------------')
        print('Class = ', self.class_)
        print('Title = ', self.title_)
        print('Text = ', self.text_)
        print('URL = ', self.ref_)
        print('Header = ', self.banner__header)
        print('Description = ', self.banner__description)

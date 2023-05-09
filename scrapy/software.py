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
        self.CompleteURL()
        self.response = requests.get(self.ref_)
        self.res = BeautifulSoup(self.response.text, 'lxml')

    def CompleteURL(self):
        if self.ref_.startswith("/en"):
            self.ref_ = "https://www.rockwellautomation.com" + self.ref_

    def GetBannerInfo(self):
        info = self.res.find(attrs={'class': 'hero-banner__content'})
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
        self.bg_url = ''
        self.bg_info = ''
        content_bg = self.res.find(attrs={'class': 'main-image'})
        if content_bg is not None:
            self.bg_url = content_bg['src'].strip()
            self.bg_info = content_bg['alt'].strip()
            if (self.bg_url.endswith('.jpg') or self.bg_url.endswith('.jpeg') or self.bg_url.endswith('.png')):
                pass
            else:
                self.bg_url = ''

    def GetPublication(self):
        self.publication = ''
        content_pub = self.res.find(
            attrs={'class': 'generic-container__inner'})
        if content_pub is not None:
            pub = content_pub.find(
                attrs={'class': 'publication'})
            if pub is not None:
                self.publication = pub.get_text().strip()

    def PrintInfo(self):
        print('--------------------')
        print('Class = ', self.class_)
        print('Title = ', self.title_)
        print('Text = ', self.text_)
        print('URL = ', self.ref_)
        print('Header = ', self.banner__header)
        print('Description = ', self.banner__description)
        print('Bg URL = ', self.bg_url)
        print('Bg Info = ', self.bg_info)
        print('Publication = ', self.publication)


# class Product(object):
#     def __init__(self,)

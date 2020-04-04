from bs4 import BeautifulSoup
import urllib.request as requests


class DownloadFetcher:

    def __init__(self, book_data: dict, base_url='http://93.174.95.29/main/'):
        self.book_data = book_data
        self.base_url = base_url

    # extracts the md5 from the book dictionary and add it to the base_url
    def get_book_link(self):
        try:
            link = self.book_data['Book']['link']
            md5 = link.split('=')[1]
            book_link = f'{self.base_url}{md5}'
            return book_link
        except Exception as e:
            print(e)

    # gets the link for direct download
    def get_direct_download(self):
        try:
            link = self.get_book_link()
            page = requests.urlopen(link)
            soup = BeautifulSoup(page, 'html.parser')
            direct_link = soup.h2.a.get('href')
            return direct_link
        except Exception as e:
            print(e)

import urllib.request as requests
from bs4 import BeautifulSoup
import re
import json


class Scrapper:

    def __init__(self, search_data, results=25,  base_url='http://libgen.is/',):
        self.search = search_data.replace(" ", "+")
        self.results = results
        self.base_url = base_url
        self.url = f'{self.base_url}search.php?req={self.search}&open=0&res={self.results}&view=simple&phrase=1&column=def'

    def page_data(self):
        try:
            page = requests.urlopen(self.url)
            soup = BeautifulSoup(page, 'html.parser')
            title_row = soup.find(attrs={'bgcolor': '#C0C0C0'})
            keys = ['Author(s)', 'Book', 'Publisher', 'Year', 'Pages', 'Language', 'Size',  'Extension' ]
            book_data_rows = title_row.find_next_siblings('tr')
            return (keys, book_data_rows)
        except Exception as e:
            print(e)

    def parse_data(self):
        print('\nGetting results from libgen.....')
        keys, dataRows = self.page_data()
        final_data = []
        for row in dataRows:
            book_data = []
            for td in row.find_all('td'):
                # get all non link values
                if td.string is not None and td.a is None:
                    book_data.append(td.string)
                # get the 'a' tags which are either authors or booknames
                elif td.a is not None:
                    if td.find(href=re.compile('^book')) is not None:
                        book_a = td.find(href=re.compile('^book'))
                        href = f"{self.base_url}{book_a.get('href')}"
                        name = [str(string)
                                for string in book_a.stripped_strings][0]
                        book_data.append(dict(title=name, link=href))
                    else:
                        book_data.append(
                            [str(string) for string in td.stripped_strings if str(string) != ','])
                # empty 'td'
                elif td.string is None:
                    book_data.append("")
            # print(book_data[1:-6])

            row_data = dict(zip(keys, book_data[1:-6]))
            final_data.append(row_data)
        return final_data


# data = Scrapper('three body problem').parse_data()
# print(data)

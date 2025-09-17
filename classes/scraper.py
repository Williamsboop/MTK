from typing import Optional
from json import load
from requests import get, Response
from bs4 import BeautifulSoup
from os import path

class SCRAPER:
    def __init__(self, url:str) -> None:
        with open('data/status_codes.json', 'r') as file:
            self.__statuses = load(file)

        # Local HTML File
        if path.exists(url):
            with open(url, 'rb') as local_html:
                self.__target_content = local_html.read()
            self.__status_code = 000
        else:
            # URL to Webpage
            self.__target_data:Response = get(url)
            self.__target_content:bytes = self.__target_data.content
            self.__status_code:int = self.__target_data.status_code

    @property
    def get_status(self) -> str:
        try:
            status:str = self.__statuses[str(self.__status_code)]
            return f"'{status}' | Code: {self.__status_code}"
        except KeyError:
            return f"'UNKNOWN_STATUS' | Code: {self.__status_code}"
        
    @property
    def get_html(self) -> str:
        html = BeautifulSoup(self.__target_content, 'lxml')
        return html.prettify()
    
    # Optional parameters usage: https://onlinegdb.com/vNvgGJZzo #
    def parse(self, element_type:str, class_name:Optional[str] = None, id_name:Optional[str] = None) -> list:
        
        
        return []
    
scraper = SCRAPER("data/tester.html")
print(scraper.get_html)
print(scraper.get_status)
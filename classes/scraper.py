from typing import Optional, Any
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
            self.__status_code = 0
            self.__html = BeautifulSoup(self.__target_content, 'lxml')
        else:
            # URL to Webpage
            self.__target_data:Response = get(url)
            self.__target_content:bytes = self.__target_data.content
            self.__status_code:int = self.__target_data.status_code
            self.__html = BeautifulSoup(self.__target_content, 'lxml')

    @property
    def get_status(self) -> str:
        try:
            status:str = self.__statuses[str(self.__status_code)]
            return f"'{status}' | Code: {self.__status_code}"
        except KeyError:
            return f"'UNKNOWN_STATUS' | Code: {self.__status_code}"
    
    # Interesting dynamic parameter parsing thingy: https://onlinegdb.com/nHC8JONE8 #
    def find(self, element_type:Any, class_name:Optional[Any] = None, id_name:Optional[Any] = None, txt:Optional[str]=None) -> list:
        
        # Defines keyword arguments dictionary.
        kwargs: dict = {}
        if class_name is not None:
            kwargs["class_"] = class_name
        if id_name is not None:
            kwargs["id"] = id_name

        elements: list[Any] = self.__html.find_all(element_type, **kwargs)

        # Parsing for specific text in element.
        if txt is not None:
            return [elm for elm in elements if txt in elm.get_text()]
        
        return elements

scraper = SCRAPER("https://www.hometowndma.com/")
print(scraper.get_status)
print(scraper.find('p'))
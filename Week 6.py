import requests
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import multiprocessing

class NotFoundException(Exception):
    """Base class for other exceptions"""
    pass

class TextComparer(): 
      
    def __init__(self, url_list):
        self.url_list = url_list
        self.index = 0
        
        
    def __download__(self, url, filename):
        
        res = requests.get(url)
        if res.status_code == 404:
            raise NotFoundException
                
        with open(filename + ".txt", 'wb') as fd:
            for chunk in res.iter_content(chunk_size=1024):
                fd.write(chunk)

    
    def __iter__(self):
        return iter
    
    def __next__(self):
        if self.index == len(self.url_list) -1:
            raise StopIteration
        print(len(self.url_list))
        index_to_fetch = self.index
        self.index = self.index + 1
        return list(self.url_list.values())[index_to_fetch]



    def __multi_download__(self, threads=5):
        
        with ThreadPoolExecutor(threads) as ex:
            for i in self.url_list:
                ex.submit(self.__download__, i, self.url_list[i])

            
    def __urllist_generator__(self):
        for url in self.url_list:
            yield url            
            
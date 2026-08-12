from infrastructure.inpi.inpi_search import INPISearch

class PatentFetcher:
    def __init__(self, inpi_search:INPISearch):
        self.inpi_search = inpi_search

    def fetch_by_app_code(self, app_code:str) -> str:
        
        return self.inpi_search.search_detail(app_code)
    
    def fetch_by_number(self, number:str) -> str:
        return self.inpi_search.basic_search(number)

    def fetch_by_keyword(self, title:str="", abstract:str="") -> str:
        return self.inpi_search.advanced_search(title=title, abstract=abstract)

    def fetch_by_page(self, page:str="1", title:str="", abstract:str="") -> str:
        return self.inpi_search.search_page(page, title, abstract)

    def base_get(self):
        return self.inpi_search.search_by_get("")


    # def fetch_by_number(self, number:str):
    #     html = self.inpi_search.basic_search(number)
    #     app_code = self.parser.parser_app_code(html)
    #     return self.fetch_by_app_code(app_code)
    
    # def fetch_by_keyword(self, title:str="", abstract:str=""):
    #     html = self.inpi_search.advanced_search(title=title, abstract=abstract)
    #     app_code = self.parser.parser_app_code(html)
    #     return self.fetch_by_app_code(app_code)
    
    
 
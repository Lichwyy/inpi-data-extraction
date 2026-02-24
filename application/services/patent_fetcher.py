from infrastructure.parsers.inpi_parser import INPIParser
from infrastructure.inpi.inpi_search import INPISearch

class PatentFetcher:
    def __init__(self, parser:INPIParser, inpi_search:INPISearch):
        self.parser = parser
        self.inpi_search = inpi_search

    def fetch_by_app_code(self, app_code:str):
        html = self.inpi_search.search_detail(app_code)
        return self.parser.parser_detail(html)
    
    def fetch_by_number(self, number:str):
        html = self.inpi_search.basic_search(number)
        app_code = self.parser.parser_app_code(html)
        return self.fetch_by_app_code(app_code)
    
    def fetch_by_keyword(self, title:str="", abstract:str=""):
        html = self.inpi_search.advanced_search(title=title, abstract=abstract)
        app_code = self.parser.parser_app_code(html)
        return self.fetch_by_app_code(app_code)
        
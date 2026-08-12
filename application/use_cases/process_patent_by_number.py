from application.services.search_fetcher import PatentFetcher
from application.services.patent_parser import PatentParser
class ProcessPatentByNumber:
    def __init__(self, fetcher:PatentFetcher, parser:PatentParser):
        self.fetcher = fetcher
        self.parser = parser
    def execute(self, number:str):
        try:
            page_finded = self.fetcher.fetch_by_number(number)
            app_code = self.parser.parse_app_code(page_finded)
            patent_page = self.fetcher.fetch_by_app_code(app_code[0])
            return self.parser.parse_detail(patent_page) 
        except Exception as e:
            return e
from application.services.search_fetcher import PatentFetcher
from application.services.patent_parser import PatentParser

class ProcessPatentByKeyword:
    def __init__(self, fetcher:PatentFetcher, parser:PatentParser):
        self.fetcher = fetcher
        self.parser = parser
        self.counter = 1
    def execute(self, title:str = "", abstract:str = ""):
        try:
            page = self.fetcher.fetch_by_keyword(title, abstract)
            app_codes = self.parser.parse_app_code(page)
            last_app_codes = list()
            app_codes_total = list()

            while True:
                if last_app_codes == app_codes:
                    break
                self.counter += 1
                last_app_codes = app_codes
                app_codes_total.extend(app_codes)
                next_page = self.fetcher.fetch_by_page(str(self.counter), title, abstract)
                app_codes = self.parser.parse_app_code(next_page)
            
            for app_code in app_codes_total:
                
                patent_page = self.fetcher.fetch_by_app_code(app_code)
                print("App Code: ", app_code, "pagina: "," ".join(patent_page.split())[0:2500])
                patent = self.parser.parse_detail(patent_page)
                yield patent

        except Exception as e:
            return e
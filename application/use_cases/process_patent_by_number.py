from application.services.patent_fetcher import PatentFetcher

class ProcessPatentByNumber:
    def __init__(self, fetcher:PatentFetcher):
        self.fetcher = fetcher

    def execute(self, number:str):
        try:
            patent = self.fetcher.fetch_by_number(number)
            return patent
        except Exception as e:
            return e
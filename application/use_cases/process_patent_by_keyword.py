from application.services.patent_fetcher import PatentFetcher


class ProcessPatentByKeyword:
    def __init__(self, fetcher:PatentFetcher):
        self.fetcher = fetcher

    def execute(self, title:str = "", abstract:str = ""):
        try:
            patent = self.fetcher.fetch_by_keyword(title, abstract)
            return patent
        except Exception as e:
            return e
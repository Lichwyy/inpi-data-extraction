from infrastructure.inpi.inpi_client import INPIClient
from infrastructure.parsers.inpi_parser import INPIParser
from infrastructure.inpi.inpi_search import INPISearch


class ProcessPatentByKeyword:
    def __init__(self, client:INPIClient, parser:INPIParser, inpi_search:INPISearch):
        self.client = client
        self.parser = parser
        self.inpi_search = inpi_search


    def execute(self, title:str = "", abstract:str = ""):

        html_app_code = self.inpi_search.advanced_search(title=title, abstract=abstract)

        app_code = self.parser.parser_app_code(html_app_code)

        patent_text_data = self.inpi_search.search_detail(app_code)

        patent = self.parser.parser_detail(patent_text_data)

        return patent
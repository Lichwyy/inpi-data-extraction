from infrastructure.parsers.inpi_parser import INPIParser
from infrastructure.inpi.inpi_search import INPISearch


class ProcessAppCode:
    def __init__(self, parser:INPIParser, inpi_search:INPISearch):
        self.parser = parser
        self.inpi_search = inpi_search


    def execute(self, app_code:str):
        patent_text_data = self.inpi_search.search_detail(app_code)

        patent = self.parser.parser_detail(patent_text_data)

        return patent
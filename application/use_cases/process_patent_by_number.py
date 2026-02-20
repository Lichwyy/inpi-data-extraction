from infrastructure.parsers.inpi_parser import INPIParser
from infrastructure.inpi.inpi_search import INPISearch

class ProcessPatentByNumber:
    def __init__(self, parser:INPIParser, inpi_search:INPISearch):
        self.parser = parser
        self.inpi_search = inpi_search
    

    def execute(self, number:str):
        
        html_app_code = self.inpi_search.basic_search(number)
                
        app_code = self.parser.parser_app_code(html_app_code)
        
        patent_text_data = self.inpi_search.search_detail(app_code)

        patent = self.parser.parser_detail(patent_text_data)

        return patent
from infrastructure.parsers.inpi_parser import INPIParser
from domain.models import Patent
class PatentParser():

    def __init__(self, inpi_parser:INPIParser):
        self.inpi_parser = inpi_parser

    def parse_app_code(self, html:str) -> list[any]:
        return self.inpi_parser.find_app_code(html)
    
    def parse_detail(self, html:str) -> Patent:
        return self.inpi_parser.parser_detail(html)
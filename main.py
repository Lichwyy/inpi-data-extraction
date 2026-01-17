from correto.inpi_client import INPIClient
from correto.inpi_detail_service import INPIDetailService
from correto.inpi_parser import INPIParser
from correto.inpi_search import INPISearch
from utils.file_manager import FileManager
from pathlib import Path

def reauthenticate(response, inpi_search, number):
    if cliente.expired_session(response):
        cliente.authenticate()
        inpi_search.search_by_number(number)


if __name__ == "__main__":
    cliente = INPIClient()
    inpisearch = INPISearch(cliente)
    inpidetail = INPIDetailService(cliente)
    parser = INPIParser()
    filemanager = FileManager()
    

    contador = 0
    numeros = filemanager.read_lines(Path(__file__).resolve().parent / "patents_ids" / "patents_ids.txt")
    for n in numeros:
        html_cod_pedido = inpisearch.search_by_number(n)
        reauthenticate(html_cod_pedido, inpisearch, n)
        cod_pedido = parser.parser_cod_pedido(html_cod_pedido)
        dados_patentes = inpidetail.get_data(cod_pedido)
        patentes = parser.parser_detail(dados_patentes)
        
from infrastructure.inpi.inpi_client import INPIClient
from infrastructure.inpi.inpi_detail_service import INPIDetailService
from infrastructure.parsers.inpi_parser import INPIParser
from infrastructure.inpi.inpi_search import INPISearch
from utils.file_manager import FileManager
from pathlib import Path

# Estarei movendo o que não for do main para os UseCases 

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
        cliente.reauthenticate(html_cod_pedido, inpisearch, n)
        cod_pedido = parser.parser_cod_pedido(html_cod_pedido)
        dados_patentes = inpidetail.get_data(cod_pedido)
        patentes = parser.parser_detail(dados_patentes)
        print(patentes.title, " | ", patentes.application_number, " | ", patentes.publication_number, " | ", patentes
              .abstract)
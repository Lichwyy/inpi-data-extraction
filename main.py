from infrastructure.inpi.inpi_client import INPIClient
from infrastructure.parsers.inpi_parser import INPIParser
from infrastructure.inpi.inpi_search import INPISearch
from application.use_cases.process_patent_by_number import ProcessPatentByNumber
from application.use_cases.process_patents_by_number_batch import ProcessPatentNumberBatch
import requests


if __name__ == "__main__":

    client = INPIClient()
    inpisearch = INPISearch(client)
    parser = INPIParser()
    response = inpisearch.advanced_search("luz", "energia")
    print(response)


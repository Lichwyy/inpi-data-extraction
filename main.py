from infrastructure.inpi.inpi_client import INPIClient
from infrastructure.parsers.inpi_parser import INPIParser
from infrastructure.inpi.inpi_search import INPISearch
from application.use_cases.process_patent_by_number import ProcessPatentByNumber
from application.use_cases.process_patent_by_keyword import ProcessPatentByKeyword
from application.use_cases.process_patents_by_number_batch import ProcessPatentNumberBatch
from application.services.patent_parser import PatentParser
from application.services.search_fetcher import PatentFetcher
from utils.random import print_obj
import requests
from datetime import datetime

if __name__ == "__main__":

    client = INPIClient()
    inpisearch = INPISearch(client)
    parser = INPIParser()
    data_agora = datetime.now()
    fetcher = PatentFetcher(inpisearch)
    pparser = PatentParser(parser)
    use_case = ProcessPatentByNumber(fetcher, pparser)
    use_case_batch = ProcessPatentNumberBatch(use_case)
    lista_patentes = use_case_batch.execute(("BR 11 2020 018787-9", "BR 20 2015 022990-4",
"BR 11 2016 026678-1"))
    for patente in lista_patentes:
        with open("exemplo.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{patente}  \n")
        print(patente)
    # patentes = use_case.execute("garrafa and plastica")
    # contador = 0
    # for p in patentes:
    #     contador += 1 
    #     print(contador)
    #     print(p.title)
    # teste = inpisearch.search_by_get("")
    # print(teste)
    # patente = use_case.execute("PI 1006846-5")
    # print(patente.title)
    # response = inpisearch.advanced_search(title="luz")
    # print((datetime.now()-data_agora).seconds)
    # response = inpisearch.search_page(2, title="luz")
    # print(response)
    # print((datetime.now()-data_agora).seconds)
    # resposne = inpisearch.search_page(3, title="luz and solar")
    # print(response)
    # print((datetime.now()-data_agora).seconds)
    # resposne = inpisearch.search_page(4, title="luz and solar")
    # print(response)
    # print((datetime.now()-data_agora).seconds)
    # resposne = inpisearch.search_page(5, title="luz and solar")
    # print(response)
    # print((datetime.now()-data_agora).seconds)
    # resposne = inpisearch.search_page(6, title="luz and solar")
    # print(response)
    # print((datetime.now()-data_agora).seconds)
    
    

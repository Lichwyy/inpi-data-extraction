from infrastructure.inpi.inpi_client import INPIClient
from infrastructure.parsers.inpi_parser import INPIParser
from infrastructure.inpi.inpi_search import INPISearch
from application.use_cases.process_patent_by_number import ProcessPatentByNumber
from application.use_cases.process_patents_by_number_batch import ProcessPatentNumberBatch

if __name__ == "__main__":

    client = INPIClient()
    inpisearch = INPISearch(client)
    parser = INPIParser()

    processor = ProcessPatentByNumber(parser, inpisearch)
    batcher = ProcessPatentNumberBatch(processor)
    numbers_list = ["BR 12 2020 018140-0",
                    "BR 11 2017 022028-8",
                    "BR 11 2013 018623-2"]
    results = batcher.execute(numbers=numbers_list)
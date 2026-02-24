from application.use_cases.process_patent_by_number import ProcessPatentByNumber

class ProcessPatentNumberBatch:
    def __init__(self, process_patent:ProcessPatentByNumber):
        self.process_patent = process_patent
    

    def execute(self, numbers:list[str]):
        for number in numbers:
            try:
                yield self.process_patent.execute(number)
            except Exception as e:
                yield {"number":number, "error": str(e)}
from infrastructure.inpi.inpi_client import INPIClient

class INPISearch:
    def __init__(self, client:INPIClient):
        self.client = client
    
    def search_by_number(self, numero:str):
        params = {
            "Action": "SearchBasico",
            "NumPedido": numero,
            "FormaPesquisa": "todasPalavras",
            "Coluna": "Titulo",
            "RegisterPerPage": "20"
        }
        r= self.client.session.get(self.client.base_url+"servlet/PatenteServletController",
                          params=params
                            )
        r.encoding = "ISO-8859-1"
        return r.text

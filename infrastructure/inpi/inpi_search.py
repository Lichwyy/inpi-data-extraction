from infrastructure.inpi.inpi_client import INPIClient
from time import sleep
class INPISearch:
    def __init__(self, client:INPIClient):
        self.client = client
        self.search_url = self.client.base_url+"servlet/PatenteServletController"


    def _request_with_retry(self, method, **kwargs):
        if method == "get":
                r = self.client.session.get(self.search_url, **kwargs)
                
        elif method == "post":
            r = self.client.session.post(self.search_url, **kwargs)
        r.encoding = "ISO-8859-1"
        
        if self.client.expired_session(r.text) or r.status_code == 504 or r.status_code == 502:
            sleep(2)
            self.client.refresh_session()
            sleep(2)
            self.client.authenticate()
            self.client.session.post(self.search_url)
            if method == "get":
                r = self.client.session.get(self.search_url, **kwargs)
                
            elif method == "post":
                r = self.client.session.post(self.search_url, **kwargs)
            r.encoding = "ISO-8859-1"

        return r.text
    

    def search_by_post(self, data):
        self.client.session.get(self.search_url)
        return self._request_with_retry(
            "post",
            data=data
        )

    def search_by_get(self, params):
        self.client.session.get(self.search_url)
        return self._request_with_retry(
            "get",
            params=params
        )
    
    def basic_search(self, number:str):
        params = {
            "Action": "SearchBasico",
            "NumPedido": number,
            "FormaPesquisa": "todasPalavras",
            "Coluna": "Titulo",
            "RegisterPerPage": "40"
        }
        return self.search_by_get(params)



    def advanced_search(self, title:str = "", abstract:str = ""):
        data = {
            "NumPedido": "",
            "ListaNumeroPatente": "",
            "NumPrioridade": "",
            "CodigoPct": "",
            "DataDeposito1": "",
            "DataDeposito2": "",
            "DataPrioridade1": "",
            "DataPrioridade2": "",
            "DataDepositoPCT1": "",
            "DataDepositoPCT2": "",
            "DataPublicacaoPCT1": "",
            "DataPublicacaoPCT2": "",
            "ClassificacaoIPC": "",
            "CatchWordIPC": "",
            "Titulo": title,
            "Resumo": abstract,
            "NomeDepositante": "",
            "CpfCnpjDepositante": "",
            "NomeInventor": "",
            "ListaFigura": "null",
            "RegisterPerPage": "30",
            "botao": " pesquisar » ",
            "Action": "SearchAvancado"
        }
        return self.search_by_post(data)
    
    
    def search_page(self, page:int, abstract:str = "", title:str = ""):
        params = {
            "Action": "nextPage",
            "Page": page,
            "Titulo": title,
            "Resumo": abstract
        }
        return self.search_by_get(params)

    def search_detail(self, codPedido:str):
        params = {
            "Action": "Detail",
            "CodPedido": codPedido
        }
        return self.search_by_get(params)
        

from infrastructure.inpi.inpi_client import INPIClient

class INPISearch:
    def __init__(self, client:INPIClient):
        self.client = client
        self.search_url = self.client.base_url+"servlet/PatenteServletController"


    def _request_with_retry(self, method, **kwargs):
        r = method(self.search_url, **kwargs)
        r.encoding = "ISO-8859-1"
        if self.client.expired_session(r.text):
            self.client.authenticate()
            r = method(self.search_url, **kwargs)
            r.encoding = "ISO-8859-1"

        return r.text
    

    def search_by_post(self, data):
        return self._request_with_retry(
            self.client.session.post,
            data=data
        )

    def search_by_get(self, params):
        return self._request_with_retry(
            self.client.session.get,
            params=params
        )
    
    def basic_search(self, number:str):
        params = {
            "Action": "SearchBasico",
            "NumPedido": number,
            "FormaPesquisa": "todasPalavras",
            "Coluna": "Titulo",
            "RegisterPerPage": "20"
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
            "RegisterPerPage": "20",
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
        

from correto.inpi_client import INPIClient

class INPIDetailService:
    def __init__(self, client:INPIClient):
        self.client = client
    
    def get_data(self, codPedido:str):
        params = {
            "Action": "Detail",
            "CodPedido": codPedido
        }
        r= self.client.session.get(self.client.base_url+"servlet/PatenteServletController",
                          params=params
                            )
        r.encoding = "ISO-8859-1"
        return r.text



class InpiSearchParser:

    def extract_app_codes(self, html:str)->list[str]:
        pass

    def has_next_page(self, html:str) -> bool:
        pass 
        # se tiver isso na pagina é porque é uma pagina legitima "<a href='/pePI/servlet/PatenteServletController?Action=detail&CodPedido"

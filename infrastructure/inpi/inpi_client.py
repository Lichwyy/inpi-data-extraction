import requests
from config.settings import PASSWORD_INPI, LOGIN_INPI

class INPIClient:
    def __init__(self):
        self.session = requests.Session()
        self.login = LOGIN_INPI
        self.password = PASSWORD_INPI
        self.base_url = "https://busca.inpi.gov.br/pePI/"
    
    def authenticate(self):
        self.session.get(self.base_url)
        self.session.post(self.base_url+"servlet/LoginController",
                          data=
                          {
                              "T_Login": self.login,
                                "T_Senha": self.password,
                                "action": "login",
                                "Usuario": ""
                                }
                            )
    def expired_session(self, response):
        return "anonimamente" in response
    
    def reauthenticate(self, response, inpi_search, number):
        if self.expired_session(response):
            self.authenticate()
            inpi_search.basic_search(number)

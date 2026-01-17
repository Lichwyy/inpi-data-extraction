import requests
import os
from dotenv import load_dotenv

load_dotenv()

class INPIClient:
    def __init__(self):
        self.session = requests.Session()
        self.login = os.getenv("login")
        self.password = os.getenv("pass")
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
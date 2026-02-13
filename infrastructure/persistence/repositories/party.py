from domain.models import Party
from sqlalchemy.orm import Session

class PartyRepository():
    def __init__(self, session: Session):
        self.session = session

    def insert(self, party:Party): #Tipo isso aí
        self.session.add(party)
        self.session.commit()
        self.session.close()
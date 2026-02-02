from sqlalchemy import create_engine, text
from config.settings import DATABASE_URL

class SessionContext():
    def __init__(self):
        self.database_url = DATABASE_URL
        self.engine = create_engine(
                        self.database_url,
                        pool_pre_ping=True,
                        future=True)

    def test_conn(self):
        with self.engine.connect() as connection:
            result = connection.execute(text('SELECT version();'))
            print(result.scalar())


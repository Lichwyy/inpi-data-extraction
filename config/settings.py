import os
from dotenv import load_dotenv

load_dotenv()

# inpi
LOGIN_INPI = os.getenv("LOGIN_INPI")
PASSWORD_INPI = os.getenv("PASSWORD_INPI")

# database
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_USER = "postgres"
DB_HOST = "test.c1g6k0gsugpn.us-east-2.rds.amazonaws.com"
DB_PORT = "5432"
DB_NAME = "postgres"
SSL_MODE = "require"
SSL_ROOT_CERT = "/certs/global-bundle.pem"

DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    f"?sslmode={SSL_MODE}&sslrootcert={SSL_ROOT_CERT}"
)
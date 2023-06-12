import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

ELEPHANTSQL_DATABASE = os.environ.get("ELEPHANTSQL_DATABASE")
ELEPHANTSQL_USERNAME = os.environ.get("ELEPHANTSQL_USERNAME")
ELEPHANTSQL_PASSWORD = os.environ.get("ELEPHANTSQL_PASSWORD")
ELEPHANTSQL_HOST = os.environ.get("ELEPHANTSQL_HOST")
ELEPHANTSQL_PORT = os.environ.get("ELEPHANTSQL_PORT")
ELEPHANTSQL_API_TOKEN = os.environ.get("ELEPHANTSQL_API_TOKEN")

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    database=ELEPHANTSQL_DATABASE,
    user=ELEPHANTSQL_USERNAME,
    password=ELEPHANTSQL_PASSWORD,
    host=ELEPHANTSQL_HOST,
    port=ELEPHANTSQL_PORT,
)

# Create a cursor object to interact with the database
cur = conn.cursor()

# Enter the COPY mode and execute the COPY command
COPY_QUERY = """
COPY stocks (ticker, name, currency, exchange)
FROM STDIN WITH (FORMAT csv, DELIMITER ',', HEADER)
"""

cur.copy_expert(COPY_QUERY, file=open("..\..\download\12data_stocks.csv", "r"))

# Commit the changes and close the cursor and connection
conn.commit()
cur.close()
conn.close()

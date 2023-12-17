import os
from sqlalchemy import create_engine
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO
import requests
import logging
import time
import random


def main():
    # database connection settings
    db_username = os.environ.get("DB_USER")
    db_password = os.environ.get("DB_PASS")
    db_host = os.environ.get("DB_HOST")
    db_port = os.environ.get("DB_PORT")
    db_name = os.environ.get("DB_NAME")

    # SQLAlchemy engine for PostgreSQL
    engine = create_engine(
        f"postgresql+psycopg2://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
    )
    with engine.connect() as conn:
        query = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"
        tables = pd.read_sql(query, conn)

    all_urls = []
    for table in tables["table_name"]:
        query = f'SELECT "URL" FROM "{table}" WHERE "URL" IS NOT NULL'
        urls = pd.read_sql(query, engine)
        all_urls.extend(urls["URL"].tolist())

    for url in all_urls[67:68]:
        response = requests.get(url)
        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")

        # tables = soup.find(
        #     "pre", "csv_box-WAS-game-basic"
        # )  # Finds all table tags
        csv_ = soup.find("pre", id=f"csv_box-{url[-8:-5]}-game-basic")
        print(csv_)
        # logging.warning(len(tables))
        # dataframes = []
        # for table in tables:
        #     # Convert each table to a DataFrame
        #     try:
        #         df = pd.DataFrame(
        #             pd.read_html(StringIO(str(table)))[0],
        #         )
        #         print(df.columns)
        #     except ValueError as ve:
        #         logging.warning(f"{ve}")
        # time.sleep(random.randint(1, 10))


if __name__ == "__main__":
    main()

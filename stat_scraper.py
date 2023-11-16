import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
import psycopg2
from psycopg2 import sql
import logging

user = os.getenv('DB_USER')
password = os.getenv('DB_PASS')
years = range(1991, 2023)

# connection parameters
db_params = {
    "dbname": "NBA",
    "user": user,
    "password": password,
    "host": "localhost"
}

# logging.warning(f"{user}, {password}")

def connect_db(params):
    """Connect to the postgresql db server"""
    conn = psycopg2.connect(**params)
    return conn

def create_table(conn):
    """Create tables in the postgresql db"""
    commands = (
        """
        CREATE TABLE IF NOT EXISTS games (
            game_id SERIAL PRIMARY KEY,
            season VARCHAR(255),
            date DATE,
            home_team VARCHAR(255),
            away_team VARCHAR(255),
            home_score INT,
            away_score INT
        )
        """,
    )
    cur = conn.cursor()
    for command in commands:
        cur.execute(command)
    cur.close()
    conn.commit()

def scrape_nba_season(season):
    url = f"https://www.basketball-reference.com/leagues/NBA_{season}_games.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all("a")
    standings_pages = [f"https://www.basketball-reference.com{l['href']}" for l in links]

    return standings_pages


standings_pages = scrape_nba_season(years[0])

logging.warning(f'{standings_pages}')

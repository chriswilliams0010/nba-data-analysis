#!/usr/bin/env python3

import os
from bs4 import BeautifulSoup
import pandas as pd
import psycopg2
from psycopg2 import sql
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging

user = os.getenv("DB_USER")
password = os.getenv("DB_PASS")
years = range(2022, 2023)
DATA_DIR = "data"
STANDINGS_DIR = os.path.join(DATA_DIR, "standings")
SCORES_DIR = os.path.join(DATA_DIR, "scores")

# connection parameters
db_params = {"dbname": "NBA", "user": user, "password": password, "host": "localhost"}


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


def get_html(url, selector=None, sleep=5, retries=3):
    html = None
    for i in range(1, retries + 1):
        time.sleep(sleep * i)
        try:
            driver = webdriver.Safari()

            driver.get(url)
            logging.warning(driver.title)

            time.sleep(sleep)

        except Exception as e:
            logging.warning(f"Timeout error on {url}: {e}")
            continue
        finally:
            driver.quit()
        break
    return html


def scrape_nba_season(season):
    url = f"https://www.basketball-reference.com/leagues/NBA_{season}_games.html"
    html = get_html(url)

    soup = BeautifulSoup(html)
    links = soup.find_all("a")
    standings_pages = [
        f"https://www.basketball-reference.com{l['href']}" for l in links
    ]

    for url in standings_pages:
        save_path = os.path.join(STANDINGS_DIR, url.split("/")[-1])
        if os.path.exists(save_path):
            continue

        html = get_html(url, "#all_schedule")
        with open(save_path, "w+") as f:
            f.write(html)


def scrape_game(standings_file):
    with open(standings_file, "r") as f:
        html = f.read()

    soup = BeautifulSoup(html)
    links = soup.find_all("a")
    hrefs = [link.get("href") for link in links]
    box_scores = [
        f"https://www.basketball-reference.com{l}"
        for l in hrefs
        if l and "boxscore" in l and ".html" in l
    ]

    for url in box_scores:
        save_path = os.path.join(SCORES_DIR, url.split("/")[-1])
        logging.warning(save_path)
        if os.path.exists(save_path):
            continue

        html = get_html(url, "#content")
        if not html:
            continue
        with open(save_path, "w+") as f:
            f.write(html)


def main():
    standings_files = os.listdir(STANDINGS_DIR)
    for year in years:
        scrape_nba_season(year)

    for year in years:
        files = [s for s in standings_files if str(year) in s]

        for f in files:
            filepath = os.path.join(STANDINGS_DIR, f)

            scrape_game(filepath)


if __name__ == "__main__":
    main()

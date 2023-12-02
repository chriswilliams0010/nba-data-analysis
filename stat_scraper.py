import requests
import time
import logging

seasons = list(range(1950, 2024))
months = [
    "november",
    "december",
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
]

base_url = "https://www.basketball-reference.com/"

# loop through seasons
for season in seasons:
    data = False
    url = base_url.format(season)
    try:
        data = requests.get(url)
        logging.warning(f"html successful for {url}")
    except Exception as e:
        logging.warning(f"An exception occured when accessing {url}: {e}")
    if data:
        with open(f"./data/leagues/NBA_{season}.html", "w+") as f:
            f.write(data.text)
            logging.warning(f"./data/leagues/NBA_{season}.html written")
    time.sleep(5)


for season in seasons:
    for month in months:
        data_players = False
        url = base_url + f"leagues/NBA_{season}_games-{month}.html"
        try:
            data_players = requests.get(url)
            logging.warning(f"html successful for {url}")
        except:
            logging.warning(f"An exception occured when accessing {url}: {e}")
        if data_players:
            with open(f"./data/players/{season}.html", "w+") as f:
                f.write(data_players.text)
        time.sleep(5)

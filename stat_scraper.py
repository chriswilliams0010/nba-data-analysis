import requests
import time

seasons = list(range(1950, 2024))
months = ["november", "december", "january", "february", "march", "april", "may", "june"]

base_url = "https://www.basketball-reference.com/"

# loop through seasons
for season in seasons:
    url = base_url.format(season)
    data = requests.get(url)

    with open(f"./data/leagues/NBA_{season}.html", "w+") as f:
        f.write(data.text)

    time.sleep(5)

for season in seasons:
    for month in months:
        url = base_url + f"leagues/NBA_{season}_games-{month}.html"
        data_players = requests.get(url)

        with open(f"./data/players/{season}.html", "w+") as f:
            f.write(data_players.text)
        time.sleep(5)

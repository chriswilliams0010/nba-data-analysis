import os
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO
from sqlalchemy import create_engine
import logging

# dict mapping teams to their 3-letter identifier
cities = {
    "Anderson Packers": "AND",
    "Atlanta Hawks": "ATL",
    "Baltimore Bullets": "BLB",
    "Boston Celtics": "BOS",
    "Buffalo Braves": "BUF",
    "Charlotte Bobcats": "CHA",
    "Charlotte Hornets": "CHH",
    "Chicago Bulls": "CHI",
    "Chicago Packers": "CHP",
    "Chicago Stags": "CHS",
    "Chicago Zephyrs": "CHZ",
    "Cincinnati Royals": "CIN",
    "Cleveland Cavaliers": "CLE",
    "Dallas Mavericks": "DAL",
    "Denver Nuggets": "DEN",
    "Detroit Pistons": "DET",
    "Fort Wayne Pistons": "FTW",
    "Golden State Warriors": "GSW",
    "Houston Rockets": "HOU",
    "Indiana Pacers": "IND",
    "Indianapolis Olympians": "INO",
    "Kansas City Kings": "KCK",
    "Kansas City-Omaha Kings": "KCO",
    "Los Angeles Clippers": "LAC",
    "Los Angeles Lakers": "LAL",
    "Memphis Grizzlies": "MEM",
    "Miami Heat": "MIA",
    "Milwaukee Bucks": "MIL",
    "Milwaukee Hawks": "MLH",
    "Minneapolis Lakers": "MNL",
    "Minnesota Timberwolves": "MIN",
    "New Orleans Jazz": "NOJ",
    "New Orleans Hornets": "NOH",
    "New Orleans Pelicans": "NOP",
    "New Orleans/Oklahoma City Hornets": "NOK",
    "New Jersey Nets": "NJN",
    "New York Knicks": "NYK",
    "New York Nets": "NYN",
    "Oklahoma City Thunder": "OKC",
    "Orlando Magic": "ORL",
    "Philadelphia 76ers": "PHI",
    "Philadelphia Warriors": "PHW",
    "Phoenix Suns": "PHO",
    "Portland Trail Blazers": "POR",
    "Rochester Royals": "ROC",
    "Sacramento Kings": "SAC",
    "San Antonio Spurs": "SAS",
    "San Diego Clippers": "SDC",
    "San Diego Rockets": "SDR",
    "San Francisco Warriors": "SFW",
    "Seattle SuperSonics": "SEA",
    "Sheboygan Red Skins": "SHE",
    "St. Louis Bombers": "STB",
    "St. Louis Hawks": "STL",
    "Syracuse Nationals": "SYR",
    "Toronto Raptors": "TOR",
    "Tri-Cities Blackhawks": "TRI",
    "Utah Jazz": "UTA",
    "Washington Bullets": "WSB",
    "Washington Capitols": "WSC",
    "Washington Wizards": "WAS",
    "Waterloo Hawks": "WAT",
    "Vancouver Grizzlies": "VAN",
}


# function to take html file and extract the schedule table
def schedule_table(filepath):
    base_url = "https://www.basketball-reference.com"
    try:
        with open(filepath) as f:
            data = f.read()
        df = pd.DataFrame(
            pd.read_html(
                StringIO(str(BeautifulSoup(data, "html.parser").find(id="schedule")))
            )[0],
        )
 
        # create column indicating playoff games, remove row with "Playoffs" in first date row
        playoff_index = df[df["Date"] == "Playoffs"].index.min()
        df["Playoffs"] = 0
        if pd.notna(playoff_index):
            df.loc[playoff_index:, "Playoffs"] = 1
            df = df[df["Date"] != "Playoffs"]
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce").dt.strftime("%Y%m%d")
        # build url for boxscore, store in column
        df["URL"] = df.apply(
            lambda row: f"{base_url}/boxscores/{str(row['Date'])}0{cities.get(str(row['Home/Neutral']), '')}.html",
            axis=1,
        )

    except Exception as e:
        logging.warning(f"{filepath} not accessed: {e}")
        df = pd.DataFrame()
    return df


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

    # scrape the boxscore for each game
    dir_path = r"./data/players/"
    for filename in os.listdir(dir_path):
        table_name = os.path.splitext(filename)[0].replace("-", "_")
        file_path = os.path.join(dir_path, filename)
        df = schedule_table(file_path)
        print(df)
        # upload dataframe to postgresql database
        # Here, if_exists='append' is used to add data to an existing table or create a new one if it doesn't exist
        df.to_sql(table_name, engine, if_exists="append", index=False)

    print("Upload complete!")


if __name__ == "__main__":
    main()

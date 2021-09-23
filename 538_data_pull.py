"""
Pull all historical sports prediction data from 538
"""

# Check out inpredictable.com

import pandas as pd
import datetime as dt

spi_hist_url = "https://projects.fivethirtyeight.com/soccer-api/club/spi_matches.csv"
# spi_latest_url = "https://projects.fivethirtyeight.com/soccer-api/club/spi_matches_latest.csv"

mlb_hist_url = "https://projects.fivethirtyeight.com/mlb-api/mlb_elo.csv"
# mlb_latest_url = "https://projects.fivethirtyeight.com/mlb-api/mlb_elo_latest.csv"

nfl_hist_url = "https://projects.fivethirtyeight.com/nfl-api/nfl_elo.csv"
# nfl_recent_url = "https://projects.fivethirtyeight.com/nfl-api/nfl_elo_latest.csv"

wnba_hist_url = "https://projects.fivethirtyeight.com/wnba-api/wnba_elo.csv"
# wnba_latest_url = 'https://projects.fivethirtyeight.com/wnba-api/wnba_elo_latest.csv'

nba_hist_url = "https://projects.fivethirtyeight.com/nba-model/nba_elo.csv"
# nba_latest_url = 'https://projects.fivethirtyeight.com/nba-model/nba_elo_latest.csv'

spi_data = pd.read_csv(spi_url)

spi_data.shape

lookup_date = dt.date.today().strftime("%Y-%m-%d")

matches_today = spi_data[spi_data["date"] == lookup_date]

print(matches_today[["league", "team1", "team2"]])

for idx, match in matches_today.iterrows():
    league = match["league"]
    match_day = match["date"]
    home_team = match["team1"]
    away_team = match["team2"]
    home_odds = match["prob1"]
    away_odds = match["prob2"]
    draw_odds = match["probtie"]

    print(
        f"On: {match_day} in {league}\n"
        f"{home_team} win probability: {home_odds}\n"
        f"{away_team} win probability: {away_odds}\n"
        f"Draw: {draw_odds}\n"
    )

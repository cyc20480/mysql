from nba_api.stats.static import teams, players
import pandas as pd

from sqlalchemy import create_engine

nba_players = players.get_players()
nba_teams = teams.get_teams()

# print(nba_teams)

nba_teams_df = pd.DataFrame(nba_teams)
nba_players_df = pd.DataFrame(nba_players)

print(nba_players_df)

# for teamName in nba_teams:
#     print(teamName['full_name'])

engine = create_engine("mysql+pymysql://root:12345@localhost:3306/pydb?charset=utf8mb4")
engine.connect()

# nba_teams_df.to_sql(name='nba_teams', con=engine, if_exists='append', index=False)
nba_players_df.to_sql(name='nba_plyers', con=engine, if_exists='append', index=False)
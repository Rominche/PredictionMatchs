import sqlite3
import configparser
import csv
from src.ExtractData_PlayerAttributes import team_overall
from src.ExtractDataLastTenGames import last_ten_games
from src.ExtractData_Between2Teams import teams_historical
from src.ExtractData_BettingOdds import betting_odds
from src.ExtractData_Resultats import matchResultat

config = configparser.ConfigParser()
config.read('../config/config.ini')
path = config.get('DEFAULT', 'PATH')

sqlite_connection = False

try:
    sqlite_connection = sqlite3.connect(path)
    cursor = sqlite_connection.cursor()
    print("Database created and Successfully Connected to SQLite")

    listMatchs = cursor.execute("select id from Match where season='2015/2016' and id<1689").fetchall()

    with open('data2015_2016.csv', 'w', newline='') as csvfile:
        for i in listMatchs:
            home_team, away_team = team_overall(cursor, i[0])
            homeWinPercentage, homeDrawPercentage, homeLossPercentage, \
            awayWinPercentage, awayDrawPercentage, awayLossPercentage = last_ten_games(i[0], cursor)
            homeWin, awayWin, matchNul = teams_historical(i[0], cursor)
            home_win, draw, away_win = betting_odds(i[0], cursor)
            result = matchResultat(i[0], cursor)

            spamwriter = csv.writer(csvfile, delimiter=' ')
            spamwriter.writerow([i[0], home_team, away_team, homeWinPercentage, homeDrawPercentage, homeLossPercentage,
                                 awayWinPercentage, awayDrawPercentage, awayLossPercentage, homeWin, awayWin, matchNul,
                                 home_win, draw, away_win, result])

    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("The SQLite connection is closed")

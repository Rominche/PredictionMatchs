import sqlite3
import configparser

sqliteConnection = False

config = configparser.ConfigParser()
config.read('../config/config.ini')
path = config.get('DEFAULT', 'PATH')

try:
    sqliteConnection = sqlite3.connect(path)
    sqliteConnection.text_factory = sqlite3.OptimizedUnicode
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")

    homeTeamId = cursor.execute("select away_team_api_id from 'Match' where id=9993;").fetchall()[0][0]
    awayTeamId = cursor.execute("select away_team_api_id from 'Match' where id=7947;").fetchall()[0][0]
    dateMatch = cursor.execute("select date from 'Match' where id=1489;").fetchall()[0][0]

    matchTeamsResult = cursor.execute("select match_api_id, home_team_goal, away_team_goal from Match "
                                      + "where (home_team_api_id=" + str(9905) + " and away_team_api_id=" + str(8722) +
                                      ")" + "or (home_team_api_id=" + str(8722) + " and away_team_api_id=" + str(9905)
                                      + ")" + " order by date asc;").fetchall()
    if len(matchTeamsResult) > 5:
        matchTeamsResult = matchTeamsResult[-5:]
        print(matchTeamsResult)
    else:
        print(matchTeamsResult)

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")

import sqlite3
import configparser

sqliteConnection = False

config = configparser.ConfigParser()
config.read('../config/config.ini')
path = config.get('DEFAULT', 'PATH')

try:
    sqliteConnection = sqlite3.connect(path)
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")


    def team_overall(id):

        match_id = "from Match where id=" + str(id)
        date = cursor.execute("select date " + match_id).fetchall()[0][0]

        list_home_player = cursor.execute("select home_player_1, home_player_2, home_player_3,"
                                          " home_player_4, home_player_5, home_player_6, home_player_7,"
                                          " home_player_8, home_player_9, home_player_10, home_player_11 "
                                          + match_id).fetchall()[0]

        list_away_player = cursor.execute("select away_player_1, away_player_2, away_player_3,"
                                          " away_player_4, away_player_5, away_player_6, away_player_7,"
                                          " away_player_8, away_player_9, away_player_10, away_player_11 "
                                          + match_id).fetchall()[0]

        home_overall = 0
        for i in list_home_player:
            player_overall = cursor.execute("select overall_rating "
                                            "from Player_Attributes "
                                            "where player_api_id=" + str(i)
                                            + " and date<'" + date
                                            + "' ORDER BY date DESC").fetchall()[0][0]
            home_overall += player_overall

        home_overall /= len(list_home_player)

        away_overall = 0
        for i in list_away_player:
            player_overall = cursor.execute("select overall_rating "
                                            "from Player_Attributes "
                                            "where player_api_id=" + str(i)
                                            + " and date<'" + date
                                            + "' ORDER BY date DESC").fetchall()[0][0]
            away_overall += player_overall

        away_overall /= len(list_away_player)

        print(home_overall)
        print(away_overall)

        cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")

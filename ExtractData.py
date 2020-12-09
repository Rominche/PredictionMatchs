import sqlite3

sqliteConnection = False

try:
    sqliteConnection = sqlite3.connect('C:\\Users\\Victor\\Documents\\Cours\\I3\\S9\\IA\\Projet\\database.sqlite')
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite\n")

    homeTeamId = cursor.execute("select home_team_api_id from Match where id=1489;").fetchall()[0][0]
    awayTeamId = cursor.execute("select away_team_api_id from Match where id=1489;").fetchall()[0][0]
    dateMatch = cursor.execute("select date from Match where id=1489;").fetchall()[0][0]

    homeTeamDraw = cursor.execute("select count(*) from Match where home_team_api_id=" + str(homeTeamId)
                                  + " and date<'" + dateMatch + "' and home_team_goal==away_team_goal").fetchall()[0][0]
    homeTeamVictory = cursor.execute("select count(*) from Match where home_team_api_id=" + str(homeTeamId)
                                     + " and date<'" + dateMatch + "' and home_team_goal>away_team_goal").fetchall()[0][
        0]
    homeTeamLose = cursor.execute("select count(*) from Match where home_team_api_id=" + str(homeTeamId)
                                  + " and date<'" + dateMatch + "' and home_team_goal<away_team_goal").fetchall()[0][0]

    nbMatchs = homeTeamDraw + homeTeamLose + homeTeamVictory
    print("Sur " + str(nbMatchs) + " précédents :")
    print("{0:.2f}".format(homeTeamVictory*100/nbMatchs) + "% V, " + "{0:.2f}".format(homeTeamDraw*100/nbMatchs) + "% N, " +
          "{0:.2f}".format(homeTeamLose*100/nbMatchs) + "% D\n")

    awayTeamDraw = cursor.execute("select count(*) from Match where away_team_api_id=" + str(awayTeamId)
                                  + " and date<'" + dateMatch + "' and home_team_goal==away_team_goal").fetchall()[0][0]
    awayTeamLose = cursor.execute("select count(*) from Match where away_team_api_id=" + str(awayTeamId)
                                  + " and date<'" + dateMatch + "' and home_team_goal>away_team_goal").fetchall()[0][
        0]
    awayTeamVictory = cursor.execute("select count(*) from Match where away_team_api_id=" + str(awayTeamId)
                                     + " and date<'" + dateMatch + "' and home_team_goal<away_team_goal").fetchall()[0][
        0]

    nbMatchs = awayTeamDraw + awayTeamLose + awayTeamVictory
    print("Sur " + str(awayTeamDraw + awayTeamLose + awayTeamVictory) + " précédents :")
    print("{0:.2f}".format(awayTeamVictory*100/nbMatchs) + "% V, " + "{0:.2f}".format(awayTeamDraw*100/nbMatchs) +
          "% N, " + "{0:.2f}".format(awayTeamLose*100/nbMatchs) + "% D\n")
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")

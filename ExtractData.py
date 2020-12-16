import sqlite3

sqliteConnection = False

try:
    sqliteConnection = sqlite3.connect('C:\\Users\\Victor\\Documents\\Cours\\I3\\S9\\IA\\Projet\\database.sqlite')
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite\n")

    # Get data on the game
    homeTeamId = cursor.execute("select home_team_api_id from Match where id=1489;").fetchall()[0][0]
    awayTeamId = cursor.execute("select away_team_api_id from Match where id=1489;").fetchall()[0][0]
    gameDate = cursor.execute("select date from Match where id=1489;").fetchall()[0][0]

    # HOME TEAM

    # Get first date of last 10 games
    previousGamesDates = cursor.execute("select date from Match where (home_team_api_id=" + str(homeTeamId)
                                        + " or away_team_api_id=" + str(homeTeamId)
                                        + ") and date<'" + gameDate + "' order by date asc").fetchall()
    if len(previousGamesDates) > 10:
        lastTenGamesDates = previousGamesDates[-10:][0][0]
    else:
        lastTenGamesDates = previousGamesDates[0][0]

    # Get last 10 results
    homeTeamDraw = cursor.execute("select count(*) from Match where (home_team_api_id=" + str(homeTeamId)
                                  + " or away_team_api_id=" + str(homeTeamId)
                                  + ") and date<'" + gameDate + "' and date>='" + lastTenGamesDates
                                  + "' and home_team_goal=away_team_goal").fetchall()[0][0]
    homeTeamWin = cursor.execute("select count(*) from Match where ((home_team_api_id=" + str(homeTeamId)
                                 + " and home_team_goal>away_team_goal) or (away_team_api_id=" + str(homeTeamId)
                                 + " and home_team_goal<away_team_goal)) and date<'" + gameDate + "' and date>='"
                                 + lastTenGamesDates + "'").fetchall()[0][0]
    homeTeamLoss = cursor.execute("select count(*) from Match where ((home_team_api_id=" + str(homeTeamId)
                                  + " and home_team_goal<away_team_goal) or (away_team_api_id=" + str(homeTeamId)
                                  + " and home_team_goal>away_team_goal)) and date<'" + gameDate + "' and date>='"
                                  + lastTenGamesDates + "'").fetchall()[0][0]

    # Form on last 10 games
    nbGames = homeTeamDraw + homeTeamLoss + homeTeamWin
    homeWinPercentage = int(homeTeamWin * 100 / nbGames)
    homeDrawPercentage = int(homeTeamDraw * 100 / nbGames)
    homeLossPercentage = int(homeTeamLoss * 100 / nbGames)
    print("Home team last " + str(nbGames) + " games :")
    print(str(homeWinPercentage) + "% W, " + str(homeDrawPercentage) + "% D, " +
          str(homeLossPercentage) + "% L\n")

    # AWAY TEAM

    # Get first date of last 10 games
    previousGamesDates = cursor.execute("select date from Match where (home_team_api_id=" + str(awayTeamId)
                                        + " or away_team_api_id=" + str(awayTeamId)
                                        + ") and date<'" + gameDate + "' order by date asc").fetchall()

    if len(previousGamesDates) > 10:
        lastTenGamesDates = previousGamesDates[-10:][0][0]
    else:
        lastTenGamesDates = previousGamesDates[0][0]

    # Get last 10 results
    awayTeamDraw = cursor.execute("select count(*) from Match where (home_team_api_id=" + str(awayTeamId)
                                  + " or away_team_api_id=" + str(awayTeamId)
                                  + ") and date<'" + gameDate + "' and date>='" + lastTenGamesDates
                                  + "' and home_team_goal=away_team_goal").fetchall()[0][0]
    awayTeamLose = cursor.execute("select count(*) from Match where ((home_team_api_id=" + str(awayTeamId)
                                  + " and home_team_goal<away_team_goal) or (away_team_api_id=" + str(awayTeamId)
                                  + " and home_team_goal>away_team_goal)) and date<'" + gameDate + "' and date>='"
                                  + lastTenGamesDates + "'").fetchall()[0][0]
    awayTeamVictory = cursor.execute("select count(*) from Match where ((home_team_api_id=" + str(awayTeamId)
                                     + " and home_team_goal>away_team_goal) or (away_team_api_id=" + str(awayTeamId)
                                     + " and home_team_goal<away_team_goal)) and date<'" + gameDate + "' and date>='"
                                     + lastTenGamesDates + "'").fetchall()[0][0]

    # Form on last 10 games
    nbGames = awayTeamDraw + awayTeamLose + awayTeamVictory
    awayWinPercentage = int(awayTeamVictory * 100 / nbGames)
    awayDrawPercentage = int(awayTeamDraw * 100 / nbGames)
    awayLossPercentage = int(awayTeamLose * 100 / nbGames)

    print("Away team last " + str(nbGames) + " games :")
    print(str(awayWinPercentage) + "% W, " + str(awayDrawPercentage) +
          "% D, " + str(awayLossPercentage) + "% L\n")

    # Probabilities
    print("Probability of home team victory : " +
          str(int((homeWinPercentage + awayLossPercentage) / 2)) + "%")
    print("Probability of draw : " +
          str(int((homeDrawPercentage + awayDrawPercentage) / 2)) + "%")
    print("Probability of away team victory : " +
          str(int((homeLossPercentage + awayWinPercentage) / 2)) + "%\n")

    homeOdd = 100/int((homeWinPercentage + awayLossPercentage) / 2)
    drawOdd = 100 / int((homeDrawPercentage + awayDrawPercentage) / 2)
    awayOdd = 100 / int((homeLossPercentage + awayWinPercentage) / 2)
    print("Odds :")
    print(str('{:.2f}'.format(homeOdd)) + " " + str('{:.2f}'.format(drawOdd))
                                                    + " " + str('{:.2f}'.format(awayOdd)))

    # Close connection
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("\nThe SQLite connection is closed")

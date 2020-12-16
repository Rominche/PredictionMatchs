def last_ten_games(match_id, cursor):

    # Get data on the game
    homeTeamId = cursor.execute("select home_team_api_id from Match where id=" + str(match_id) + ";").fetchall()[0][
        0]
    awayTeamId = cursor.execute("select away_team_api_id from Match where id=" + str(match_id) + ";").fetchall()[0][
        0]
    gameDate = cursor.execute("select date from Match where id=" + str(match_id) + ";").fetchall()[0][0]

    # HOME TEAM

    # Get first date of last 10 games
    previousGamesDates = cursor.execute("select date from Match where (home_team_api_id=" + str(homeTeamId)
                                        + " or away_team_api_id=" + str(homeTeamId)
                                        + ") and date<'" + gameDate + "' order by date asc").fetchall()
    if len(previousGamesDates) > 10:
        lastTenGamesDates = previousGamesDates[-10:][0][0]
    elif len(previousGamesDates) > 0:
        lastTenGamesDates = previousGamesDates[0][0]

    if len(previousGamesDates) != 0:
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
        homeWinPercentage = '{:.2f}'.format(homeTeamWin / nbGames)
        homeDrawPercentage = '{:.2f}'.format(homeTeamDraw / nbGames)
        homeLossPercentage = '{:.2f}'.format(homeTeamLoss / nbGames)

    else:
        homeWinPercentage = 0.33
        homeDrawPercentage = 0.33
        homeLossPercentage = 0.33

    # print("Home team last " + str(nbGames) + " games :")
    # print(str(homeWinPercentage) + "% W, " + str(homeDrawPercentage) + "% D, " +
    #       str(homeLossPercentage) + "% L\n")

    # AWAY TEAM

    # Get first date of last 10 games
    previousGamesDates = cursor.execute("select date from Match where (home_team_api_id=" + str(awayTeamId)
                                        + " or away_team_api_id=" + str(awayTeamId)
                                        + ") and date<'" + gameDate + "' order by date asc").fetchall()

    if len(previousGamesDates) > 10:
        lastTenGamesDates = previousGamesDates[-10:][0][0]
    elif len(previousGamesDates) > 0:
        lastTenGamesDates = previousGamesDates[0][0]

    if len(previousGamesDates) != 0:
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
                                         + " and home_team_goal<away_team_goal)) and date<'" + gameDate
                                         + "' and date>='" + lastTenGamesDates + "'").fetchall()[0][0]

        # Form on last 10 games
        nbGames = awayTeamDraw + awayTeamLose + awayTeamVictory
        awayWinPercentage = '{:.2f}'.format(awayTeamVictory / nbGames)
        awayDrawPercentage = '{:.2f}'.format(awayTeamDraw / nbGames)
        awayLossPercentage = '{:.2f}'.format(awayTeamLose / nbGames)

    else:
        awayWinPercentage = 0.33
        awayDrawPercentage = 0.33
        awayLossPercentage = 0.33

    # print("Away team last " + str(nbGames) + " games :")
    # print(str(awayWinPercentage) + "% W, " + str(awayDrawPercentage) +
    #       "% D, " + str(awayLossPercentage) + "% L\n")

    return homeWinPercentage, homeDrawPercentage, homeLossPercentage, awayWinPercentage, awayDrawPercentage, \
           awayLossPercentage


# Probabilities
# print("Probability of home team victory : " +
#       str(int((homeWinPercentage + awayLossPercentage) / 2)) + "%")
# print("Probability of draw : " +
#       str(int((homeDrawPercentage + awayDrawPercentage) / 2)) + "%")
# print("Probability of away team victory : " +
#       str(int((homeLossPercentage + awayWinPercentage) / 2)) + "%\n")

# homeOdd = 100 / int((homeWinPercentage + awayLossPercentage) / 2)
# drawOdd = 100 / int((homeDrawPercentage + awayDrawPercentage) / 2)
# awayOdd = 100 / int((homeLossPercentage + awayWinPercentage) / 2)
# print("Odds :")
# print(str('{:.2f}'.format(homeOdd)) + " " + str('{:.2f}'.format(drawOdd))
#      + " " + str('{:.2f}'.format(awayOdd)))

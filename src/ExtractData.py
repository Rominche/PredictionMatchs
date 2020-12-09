import sqlite3
import configparser

sqliteConnection = False

config=configparser.ConfigParser()
config.read('../config/config.ini')
path = config.get('DEFAULT','PATH')

try:
    sqliteConnection = sqlite3.connect(path)
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite\n")

    # Selection des données du match
    homeTeamId = cursor.execute("select home_team_api_id from Match where id=1489;").fetchall()[0][0]
    awayTeamId = cursor.execute("select away_team_api_id from Match where id=1489;").fetchall()[0][0]
    dateMatch = cursor.execute("select date from Match where id=1489;").fetchall()[0][0]

    # EQUIPE A DOMICILE

    # Récupération de la première date des 10 derniers matchs
    datesMatch = cursor.execute("select date from Match where (home_team_api_id=" + str(homeTeamId)
                                + " or away_team_api_id=" + str(homeTeamId)
                                + ") and date<'" + dateMatch + "' order by date asc").fetchall()
    if len(datesMatch) > 10:
        dateAvantDixMatchs = datesMatch[-10:][0][0]
    else:
        dateAvantDixMatchs = datesMatch[0][0]
    print(dateAvantDixMatchs)

    # Récupération des 10 derniers résultats
    homeTeamDraw = cursor.execute("select count(*) from Match where (home_team_api_id=" + str(homeTeamId)
                                  + " or away_team_api_id=" + str(homeTeamId)
                                  + ") and date<'" + dateMatch + "' and date>='" + dateAvantDixMatchs
                                  + "' and home_team_goal==away_team_goal").fetchall()[0][0]
    homeTeamVictory = cursor.execute("select count(*) from Match where (home_team_api_id=" + str(homeTeamId)
                                     + " or away_team_api_id=" + str(homeTeamId)
                                     + ") and date<'" + dateMatch + "' and date>='" + dateAvantDixMatchs
                                     + "' and home_team_goal>away_team_goal").fetchall()[0][
        0]
    homeTeamLose = cursor.execute("select count(*) from Match where (home_team_api_id=" + str(homeTeamId)
                                  + " or away_team_api_id=" + str(homeTeamId)
                                  + ") and date<'" + dateMatch + "' and date>='" + dateAvantDixMatchs
                                  + "' and home_team_goal<away_team_goal").fetchall()[0][0]

    # Calcul de la forme sur les 10 derniers matchs
    nbMatchs = homeTeamDraw + homeTeamLose + homeTeamVictory
    pourcentageVictoiresH = int(homeTeamVictory * 100 / nbMatchs)
    pourcentageNulsH = int(homeTeamDraw * 100 / nbMatchs)
    pourcentageDefaitesH = int(homeTeamLose * 100 / nbMatchs)
    print("Sur " + str(nbMatchs) + " précédents :")
    print(str(pourcentageVictoiresH) + "% V, " + str(pourcentageNulsH) + "% N, " +
          str(pourcentageDefaitesH) + "% D\n")

    # EQUIPE A L'EXTERIEUR

    # Récupération de la première date des 10 derniers matchs
    datesMatch = cursor.execute("select date from Match where (home_team_api_id=" + str(awayTeamId)
                                + " or away_team_api_id=" + str(awayTeamId)
                                + ") and date<'" + dateMatch + "' order by date asc").fetchall()

    if len(datesMatch) > 10:
        dateAvantDixMatchs = datesMatch[-10:][0][0]
    else:
        dateAvantDixMatchs = datesMatch[0][0]

    # Récupération des 10 derniers résultats
    awayTeamDraw = cursor.execute("select count(*) from Match where (home_team_api_id=" + str(awayTeamId)
                                  + " or away_team_api_id=" + str(awayTeamId)
                                  + ") and date<'" + dateMatch + "' and date>='" + dateAvantDixMatchs
                                  + "' and home_team_goal==away_team_goal").fetchall()[0][0]
    awayTeamLose = cursor.execute("select count(*) from Match where (home_team_api_id=" + str(awayTeamId)
                                  + " or away_team_api_id=" + str(awayTeamId)
                                  + ") and date<'" + dateMatch + "' and date>='" + dateAvantDixMatchs
                                  + "' and home_team_goal>away_team_goal").fetchall()[0][
        0]
    awayTeamVictory = cursor.execute("select count(*) from Match where (home_team_api_id=" + str(awayTeamId)
                                     + " or away_team_api_id=" + str(awayTeamId)
                                     + ") and date<'" + dateMatch + "' and date>='" + dateAvantDixMatchs
                                     + "' and home_team_goal<away_team_goal").fetchall()[0][
        0]

    # Calcul de la forme sur les 10 derniers matchs
    nbMatchs = awayTeamDraw + awayTeamLose + awayTeamVictory
    pourcentageVictoiresA = int(awayTeamVictory * 100 / nbMatchs)
    pourcentageNulsA = int(awayTeamDraw * 100 / nbMatchs)
    pourcentageDefaitesA = int(awayTeamLose * 100 / nbMatchs)

    print("Sur " + str(awayTeamDraw + awayTeamLose + awayTeamVictory) + " précédents :")
    print(str(pourcentageVictoiresA) + "% V, " + str(pourcentageNulsA) +
          "% N, " + str(pourcentageDefaitesA) + "% D\n")

    # Calcul des probabilités de victoire
    print("Probabilité de victoire de l'équipe à domicile : " +
          str(int((pourcentageVictoiresH + pourcentageDefaitesA) / 2)) + "%")
    print("Probabilité de nul : " +
          str(int((pourcentageNulsA + pourcentageNulsH) / 2)) + "%")
    print("Probabilité de victoire de l'équipe à l'extérieur : " +
          str(int((pourcentageDefaitesH + pourcentageVictoiresA) / 2)) + "%")
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("\nThe SQLite connection is closed")

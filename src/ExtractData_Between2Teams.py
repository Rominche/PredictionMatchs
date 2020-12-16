import sqlite3
import configparser


def teams_historical(matchToPredict, cursor):

    homeWin = 0
    awayWin = 0
    matchNul = 0

    sqliteConnection.text_factory = sqlite3.OptimizedUnicode
    print("Database created and Successfully Connected to SQLite")

    homeTeamId = cursor.execute("select home_team_api_id from 'Match' where id=" + str(matchToPredict) +";").fetchall()[0][0]
    awayTeamId = cursor.execute("select away_team_api_id from 'Match' where id=" + str(matchToPredict) + ";").fetchall()[0][0]

    matchTeamsResult = cursor.execute("select match_api_id,home_team_api_id, home_team_goal,away_team_api_id, away_team_goal from Match where (home_team_api_id="+ str(homeTeamId) +" and away_team_api_id="+ str(awayTeamId) +")"
                                      "or (home_team_api_id="+ str(awayTeamId) +" and away_team_api_id="+ str(homeTeamId) +") order by date asc;").fetchall()
    if len(matchTeamsResult)>5 :
        matchTeamsResult = matchTeamsResult[-5:]
        print(matchTeamsResult)
    else :
        print(matchTeamsResult)

    for match in matchTeamsResult:
        if match[2]>match[4]:
            if match[1] == homeTeamId:
                homeWin += 1
            else:
                awayWin +=1
        elif match[2]<match[4]:
            if match[1] == homeTeamId:
                awayWin += 1
            else:
                homeWin += 1
        else:
            matchNul += 1

    print("team1 : " + str(homeTeamId) + " à gagné "+ str(homeWin) +", team2 : " + str(awayTeamId) + " à gagné "+ str(awayWin) + ", match nul : " + str(matchNul))

    return homeWin, awayWin, matchNul
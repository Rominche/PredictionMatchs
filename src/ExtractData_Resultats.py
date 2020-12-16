def matchResultat(match_id, cursor):

    goal_list  = cursor.execute("select home_team_goal, away_team_goal from 'Match' where id =" + str(match_id) + ";").fetchall()

    if goal_list[0][0] > goal_list[0][1]:
        resultat = 1
    elif goal_list [0][0] < goal_list[0][1]:
        resultat = 0
    else:
        resultat = 2

    return resultat
def team_overall(cursor, id_match):

    home_overall = 0
    away_overall = 0

    match_id = "from Match where id=" + str(id_match)
    date = cursor.execute("select date " + match_id).fetchall()[0][0]

    list_home_player = cursor.execute("select home_player_1, home_player_2, home_player_3,"
                                      " home_player_4, home_player_5, home_player_6, home_player_7,"
                                      " home_player_8, home_player_9, home_player_10, home_player_11 "
                                      + match_id).fetchall()[0]

    list_away_player = cursor.execute("select away_player_1, away_player_2, away_player_3,"
                                      " away_player_4, away_player_5, away_player_6, away_player_7,"
                                      " away_player_8, away_player_9, away_player_10, away_player_11 "
                                      + match_id).fetchall()[0]

    for i in list_home_player:
        if i is not None:
            player_overall = cursor.execute("select overall_rating "
                                            "from Player_Attributes "
                                            "where player_api_id=" + str(i)
                                            + " and date<'" + date
                                            + "' ORDER BY date DESC").fetchall()[0][0]
        else:
            player_overall = 60
        home_overall += player_overall

    home_overall /= len(list_home_player)

    for i in list_away_player:
        if i is not None:
            player_overall = cursor.execute("select overall_rating "
                                            "from Player_Attributes "
                                            "where player_api_id=" + str(i)
                                            + " and date<'" + date
                                            + "' ORDER BY date DESC").fetchall()[0][0]
        else:
            player_overall = 60
        away_overall += player_overall

    away_overall /= len(list_away_player)

    return '{:.2f}'.format(home_overall), '{:.2f}'.format(away_overall)


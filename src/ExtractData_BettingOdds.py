def betting_odds(match_id, cursor):
    home_win = 0
    draw = 0
    away_win = 0
    count = 0

    # B365
    a = cursor.execute("select B365H from Match where id=" + str(match_id)).fetchall()[0][0]
    if a is not None:
        count += 1
        home_win += a
        draw += cursor.execute("select B365D from Match where id=" + str(match_id)).fetchall()[0][0]
        away_win += cursor.execute("select B365A from Match where id=" + str(match_id)).fetchall()[0][0]

    # BW
    a = cursor.execute("select BWH from Match where id=" + str(match_id)).fetchall()[0][0]
    if a is not None:
        count += 1
        home_win += a
        draw += cursor.execute("select BWD from Match where id=" + str(match_id)).fetchall()[0][0]
        away_win += cursor.execute("select BWA from Match where id=" + str(match_id)).fetchall()[0][0]

    # IW
    a = cursor.execute("select IWH from Match where id=" + str(match_id)).fetchall()[0][0]
    if a is not None:
        count += 1
        home_win += a
        draw += cursor.execute("select IWD from Match where id=" + str(match_id)).fetchall()[0][0]
        away_win += cursor.execute("select IWA from Match where id=" + str(match_id)).fetchall()[0][0]

    # LB
    a = cursor.execute("select LBH from Match where id=" + str(match_id)).fetchall()[0][0]
    if a is not None:
        count += 1
        home_win += a
        draw += cursor.execute("select LBD from Match where id=" + str(match_id)).fetchall()[0][0]
        away_win += cursor.execute("select LBA from Match where id=" + str(match_id)).fetchall()[0][0]

    # PS
    a = cursor.execute("select PSH from Match where id=" + str(match_id)).fetchall()[0][0]
    if a is not None:
        count += 1
        home_win += a
        draw += cursor.execute("select PSD from Match where id=" + str(match_id)).fetchall()[0][0]
        away_win += cursor.execute("select PSA from Match where id=" + str(match_id)).fetchall()[0][0]

    # WH
    a = cursor.execute("select WHH from Match where id=" + str(match_id)).fetchall()[0][0]
    if a is not None:
        count += 1
        home_win += a
        draw += cursor.execute("select WHD from Match where id=" + str(match_id)).fetchall()[0][0]
        away_win += cursor.execute("select WHA from Match where id=" + str(match_id)).fetchall()[0][0]

    # SJ
    a = cursor.execute("select SJH from Match where id=" + str(match_id)).fetchall()[0][0]
    if a is not None:
        count += 1
        home_win += a
        draw += cursor.execute("select SJD from Match where id=" + str(match_id)).fetchall()[0][0]
        away_win += cursor.execute("select SJA from Match where id=" + str(match_id)).fetchall()[0][0]

    # VC
    a = cursor.execute("select VCH from Match where id=" + str(match_id)).fetchall()[0][0]
    if a is not None:
        count += 1
        home_win += a
        draw += cursor.execute("select VCD from Match where id=" + str(match_id)).fetchall()[0][0]
        away_win += cursor.execute("select VCA from Match where id=" + str(match_id)).fetchall()[0][0]

    # GB
    a = cursor.execute("select GBH from Match where id=" + str(match_id)).fetchall()[0][0]
    if a is not None:
        count += 1
        home_win += a
        draw += cursor.execute("select GBD from Match where id=" + str(match_id)).fetchall()[0][0]
        away_win += cursor.execute("select GBA from Match where id=" + str(match_id)).fetchall()[0][0]

    # BS
    a = cursor.execute("select BSH from Match where id=" + str(match_id)).fetchall()[0][0]
    if a is not None:
        count += 1
        home_win += a
        draw += cursor.execute("select BSD from Match where id=" + str(match_id)).fetchall()[0][0]
        away_win += cursor.execute("select BSA from Match where id=" + str(match_id)).fetchall()[0][0]

    if count == 0:
        return 0, 0, 0
    return '{:.2f}'.format(home_win/count), '{:.2f}'.format(draw/count), '{:.2f}'.format(away_win/count)


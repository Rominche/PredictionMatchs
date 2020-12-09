import sqlite3

sqliteConnection = False

try:
    sqliteConnection = sqlite3.connect('D:\\Users\\emely\\Documents\\Cours\\Eseo\\I3\\IA\\database\\database.sqlite')
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")

    homeTeamId = cursor.execute("select home_team_api_id from Match where id=1489;").fetchall()[0][0]
    awayTeamId = cursor.execute("select away_team_api_id from Match where id=1489;").fetchall()[0][0]
    dateMatch = cursor.execute("select date from Match where id=1489;").fetchall()[0][0]

    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")

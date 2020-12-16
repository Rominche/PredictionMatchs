import sqlite3
import configparser

sqliteConnection = False

config=configparser.ConfigParser()
config.read('../config/config.ini')
path = config.get('DEFAULT','PATH')

try:
    sqliteConnection = sqlite3.connect(path)
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")

    teamId = "from Team_Attributes where team_api_id = 10260 and date = '2015-09-10 00:00:00'"
    buildUpPlaySpeed = cursor.execute("select buildUpPlaySpeed "+teamId).fetchall()[0][0]
    buildUpPlayDribbling = cursor.execute("select buildUpPlayDribbling "+teamId).fetchall()[0][0]
    buildUpPlayPassing = cursor.execute("select buildUpPlayPassing "+teamId).fetchall()[0][0]
    chanceCreationPassing = cursor.execute("select chanceCreationPassing "+teamId).fetchall()[0][0]
    chanceCreationCrossing = cursor.execute("select chanceCreationCrossing "+teamId).fetchall()[0][0]
    chanceCreationShooting = cursor.execute("select chanceCreationShooting "+teamId).fetchall()[0][0]
    defencePressure = cursor.execute("select defencePressure "+teamId).fetchall()[0][0]
    defenceAggression = cursor.execute("select defenceAggression "+teamId).fetchall()[0][0]
    defenceTeamWidth = cursor.execute("select defenceTeamWidth "+teamId).fetchall()[0][0]

    teamOverall = (buildUpPlaySpeed \
                  + buildUpPlayDribbling \
                  + buildUpPlayPassing \
                  + chanceCreationPassing \
                  + chanceCreationCrossing \
                  + chanceCreationShooting \
                  + defencePressure \
                  + defenceAggression \
                  + defenceTeamWidth) / 9

    print(teamOverall)

    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")

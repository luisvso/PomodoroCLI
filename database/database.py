import sqlite3

def connectionDB():
    #Define the connection with the database
    connection = sqlite3.connect("pomodoroStore.bd")
    cursor = connection.cursor()

    return cursor

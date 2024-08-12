import sqlite3
import db.config as config


def connectToDB():
    return sqlite3.connect(config.db + ".db")

def conectionClose(connection):
    connection.cursor().close()
    connection.close()

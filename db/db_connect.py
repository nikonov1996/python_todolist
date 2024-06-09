from mysql.connector import connect, Error
import db.config as config


def connectToDB():
    return connect(
        host=config.host,
        port=config.port,
        user=config.user,
        password=config.password,
        database=config.db
    )

def conection():
    return connect(
        host=config.host,
        port=config.port,
        user=config.user,
        password=config.password
    )

def conectionClose(connection):
    connection.cursor().close()
    connection.close()

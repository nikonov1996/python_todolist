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


# with connection.cursor() as cursor:
#     cursor.execute(create_db_query)
#     result = cursor.fetchall()
#     for row in result:
#         print(row)

def conectionClose(connection):
    connection.cursor().close()
    connection.close()

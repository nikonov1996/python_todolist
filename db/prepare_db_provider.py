import db.config as db_config
from faker import Faker
from db.db_connect import connectToDB, conectionClose
fake = Faker("ru_RU")

delete_db_query = f"DROP DATABASE IF EXISTS {db_config.db};"
create_db_query = f"CREATE table IF NOT EXISTS {db_config.db};"

create_tbl_query = f"""
CREATE TABLE IF NOT EXISTS {db_config.todo_table} 
(id integer PRIMARY KEY,
title text NOT NULL,
content text,
creation_date DATETIME NOT NULL)
"""

insert_default_data_query = f"""
INSERT INTO {db_config.todo_table} (title,content,creation_date) VALUES 
("Заметка для {fake.name()}","{fake.text()}","{fake.date()}"),
("Заметка для {fake.name()}","{fake.text()}","{fake.date()}"),
("Заметка для {fake.name()}","{fake.text()}","{fake.date()}"),
("Заметка для {fake.name()}","{fake.text()}","{fake.date()}"),
("Заметка для {fake.name()}","{fake.text()}","{fake.date()}"),
("Заметка для {fake.name()}","{fake.text()}","{fake.date()}"),
("Заметка для {fake.name()}","{fake.text()}","{fake.date()}"),
("Заметка для {fake.name()}","{fake.text()}","{fake.date()}"),
("Заметка для {fake.name()}","{fake.text()}","{fake.date()}"),
("Заметка для {fake.name()}","{fake.text()}","{fake.date()}"),
("Заметка для {fake.name()}","{fake.text()}","{fake.date()}")
"""


def prepareDB():
    connection = connectToDB()
    cursor = connection.cursor()
    cursor.execute(create_tbl_query)
    connection.commit()
    if not checkTblEmpty():
        cursor.execute(insert_default_data_query)
        connection.commit()
    conectionClose(connection)

def checkTblEmpty():
    select_full_todolist_query = f"select * from {db_config.todo_table}"
    connection = connectToDB()
    cursor = connection.cursor()
    cursor.execute(select_full_todolist_query)
    result = cursor.fetchall()
    return len(result) > 1

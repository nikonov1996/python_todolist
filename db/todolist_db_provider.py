import datetime
import db.config as config

from db.db_connect import connectToDB, conectionClose


def get_todo_list():
    select_full_todolist_query = f"select * from {config.todo_table}"
    connection = connectToDB()
    cursor = connection.cursor()
    cursor.execute(select_full_todolist_query)
    result = cursor.fetchall()
    conectionClose(connection)
    return result


def get_todo_by_id(todo_id):
    get_todo_by_id_query = f"select * from {config.todo_table} where id='{todo_id}'"
    connection = connectToDB()
    cursor = connection.cursor()
    cursor.execute(get_todo_by_id_query)
    result = cursor.fetchone()
    conectionClose(connection)
    return result


def add_new_todo(title, content):
    add_todo_query = f"insert into {config.todo_table} (title,content,creation_date) values ({title}{content}{datetime.datetime.now()})"
    connection = connectToDB()
    cursor = connection.cursor()
    cursor.execute(add_todo_query)
    connection.commit()
    conectionClose(connection)


def update_todo_by_id(todo_id, content,title):
    up_todo_query = f"UPDATE {config.todo_table} SET content=\"{content}\",title=\"{title}\" where id='{todo_id}'"
    connection = connectToDB()
    cursor = connection.cursor()
    cursor.execute(up_todo_query)
    connection.commit()
    conectionClose(connection)

def delete_todo_by_id(todo_id):
    delete_todo_query = f"delete from {config.todo_table} where id='{todo_id}'"
    connection = connectToDB()
    cursor = connection.cursor()
    cursor.execute(delete_todo_query)
    connection.commit()
    conectionClose(connection)

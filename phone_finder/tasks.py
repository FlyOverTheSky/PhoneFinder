import psycopg2.errors

from phone_finder.celery import app
from phone_finder.settings import DB_DETAILS, TABLE_NAMES
from phone_finder.tables import create_tables, download_tables, delete_first_row, create_connection, update_tables, delete_tables


@app.task
def repeat_order_make():
    conn = create_connection(DB_DETAILS)
    download_tables(TABLE_NAMES)
    delete_first_row(TABLE_NAMES)
    try:
        delete_tables(conn, TABLE_NAMES)
    except psycopg2.errors.UndefinedTable:
        print('Первый запуск таски')
    create_tables(conn, TABLE_NAMES)
    update_tables(conn, TABLE_NAMES)
    conn.close()

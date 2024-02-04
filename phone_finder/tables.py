import csv
import psycopg2
import requests
import io
import os

from phone_finder.settings import DOWNLOAD_URLS, TABLE_NAMES, DB_DETAILS, CSVS_PATH


def download_tables(names: list) -> None:
    """Скачивает csv-файлы по DOWNLOAD_URLS."""
    for name in names:
        current_url = DOWNLOAD_URLS.get(name)
        response = requests.get(current_url, verify=False)
        temp_file_path = os.path.join(CSVS_PATH, f'{name}_temp.csv')
        with open(f'{temp_file_path}', 'wb+') as file:
            file.write(response.content)


def delete_first_row(names: list) -> None:
    """Костлявое решение для того, чтобы убрать заголовки таблицы."""
    for name in names:
        main_file_path = os.path.join(CSVS_PATH, f'{name}.csv')
        temp_file_path = os.path.join(CSVS_PATH, f'{name}_temp.csv')
        with (io.open(f'{temp_file_path}', 'r', newline='', encoding='utf-8') as file_input,
              io.open(f'{main_file_path}', 'w', newline='', encoding='utf-8') as file_output):
            reader = csv.reader(file_input)
            writer = csv.writer(file_output)
            next(reader)
            for row in reader:
                writer.writerow(row)
        os.remove(f'{temp_file_path}')


def create_connection(connection_details: dict) -> psycopg2.connect:
    """Возвращает connection"""
    try:
        connection = psycopg2.connect(**connection_details)
        print("Подключение к Postgres установлено")
        return connection
    except psycopg2.OperationalError as e:
        raise f"Возникла ошибка {e}"


def create_tables(connection: psycopg2.connect, names: list) -> None:
    """Создаёт таблицы."""
    connection.autocommit = True
    cursor = connection.cursor()
    for name in names:
        query = f'''CREATE TABLE IF NOT EXISTS "{name}"(
        "АВС/ DEF" varchar NOT NULL,
        От integer NOT NULL,
        До integer NOT NULL,
        Емкость integer NOT NULL,
        Оператор varchar NOT NULL,
        Регион varchar NOT NULL,
        ИНН varchar NOT NULL
        );'''
        cursor.execute(query)


def update_tables(connection: psycopg2.connect, names: list) -> None:
    """ Переносит данные из csv-файлов в БД."""
    connection.autocommit = True
    cursor = connection.cursor()
    for name in names:
        main_file_path = os.path.join(CSVS_PATH, f'{name}.csv')
        query = f'''
        COPY "{name}"("АВС/ DEF", От, До, Емкость, Оператор, Регион, ИНН)
        FROM '{main_file_path}'
        WITH (DELIMITER ';');'''
        cursor.execute(query)


if __name__ == '__main__':
    download_tables(TABLE_NAMES)
    delete_first_row(TABLE_NAMES)
    conn = create_connection(DB_DETAILS)
    create_tables(conn, TABLE_NAMES)
    update_tables(conn, TABLE_NAMES)
    conn.close()

from phone_finder.tables import create_connection
from phone_finder.settings import DB_DETAILS


def search_phone_details(phone_number: str) -> list:
    country = phone_number[0]
    numeration_zone = phone_number[1:4]
    number = int(phone_number[4:])
    table_name = f'{numeration_zone[0]}xx'

    connection = create_connection(DB_DETAILS)
    cursor = connection.cursor()
    find_query = f''' SELECT *
        FROM "{table_name}"
        WHERE "АВС/ DEF" LIKE '%{numeration_zone}'
        AND {number} BETWEEN "От" AND "До"
        ;'''

    cursor.execute(find_query)
    results = cursor.fetchall()
    return results
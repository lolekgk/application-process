from typing import List, Dict

from psycopg2 import sql
from psycopg2.extras import RealDictCursor

import database_common


@database_common.connection_handler
def get_mentors(cursor):
    query = """
        SELECT first_name, last_name, city
        FROM mentor
        ORDER BY first_name"""
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_mentors_by_last_name(cursor, last_name):
    query = f"""
        SELECT first_name, last_name, city
        FROM mentor
        ORDER BY last_name='{last_name}' DESC, first_name ASC"""
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_mentors_by_city(cursor, city):
    query = f"""
        SELECT first_name, last_name, city
        FROM mentor
        WHERE city='{city}'
        ORDER BY city='{city}'
        """
    cursor.execute(query)
    return cursor.fetchall()

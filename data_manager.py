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
    query = """
        SELECT first_name, last_name, city
        FROM mentor
        ORDER BY last_name=%(l_n)s DESC, first_name"""
    cursor.execute(query, {'l_n': last_name})
    return cursor.fetchall()


@database_common.connection_handler
def get_mentors_by_city(cursor, city):
    query = """
        SELECT first_name, last_name, city
        FROM mentor
        WHERE city=%(city)s
        ORDER BY city=%(city)s
        """
    cursor.execute(query, {'city': city})
    return cursor.fetchall()


@database_common.connection_handler
def get_applicants(cursor):
    query = """
        SELECT first_name, last_name, phone_number, email, application_code
        FROM applicant
        ORDER BY first_name
        """
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_applicant_data_by_name(cursor, applicant_name):
    query = """
        SELECT first_name, last_name, phone_number
        FROM applicant
        WHERE first_name=%s
        """
    cursor.execute(query, (applicant_name,))
    return cursor.fetchall()


@database_common.connection_handler
def get_applicant_data_by_email_ending(cursor, applicant_email_ending):
    query = """
        SELECT first_name, last_name, phone_number
        FROM applicant
        WHERE email LIKE '%%' || %(email)s || '%%'
        """
    cursor.execute(query, {'email': applicant_email_ending})
    return cursor.fetchall()


@database_common.connection_handler
def get_applicant_data_by_code(cursor, code):
    query = """
        SELECT first_name, last_name, phone_number
        FROM applicant
        WHERE application_code=%s
        """
    cursor.execute(query, (code,))
    return cursor.fetchall()


@database_common.connection_handler
def update_applicant_phone_number(cursor, new_phone_number, code):
    query = """
        UPDATE applicant
        SET phone_number = %(new_number)s
        WHERE application_code = %(application_code)s
        """
    cursor.execute(query, {'new_number': new_phone_number, 'application_code': code})


@database_common.connection_handler
def delete_applicant_data(cursor, code):
    query = """
        DELETE 
        FROM applicant
        WHERE application_code = %s
        """
    cursor.execute(query, (code,))


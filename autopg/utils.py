from psycopg2 import sql
from django.db import connection


def create_db_in_pg(dbname: str, username: str, password: str):
    with connection.cursor() as cur:
        cur.execute(sql.SQL(f"create user {{}} with password '{password}';").format(
            sql.Identifier(username)
        ))
        cur.execute(sql.SQL('create database {} owner {};').format(
            sql.Identifier(dbname), sql.Identifier(username)
        ))

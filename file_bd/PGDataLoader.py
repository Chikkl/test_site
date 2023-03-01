from file_bd.IDataLoader import IDataLoader
from file_bd.config import host, user_name, password, db_name
import psycopg2


class PGDataLoader(IDataLoader):
    def load_all_users(self) -> str:
        try:
            connection = psycopg2.connect(
                host=host,
                user=user_name,
                password=password,
                database=db_name
            )
            connection.autocommit = True

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT users_name FROM users"
                )
                return cursor.fetchall()

        except Exception as _ex:
            print("[INFO] Error while working with PostgreSQL", _ex)
        finally:
            if connection:
                connection.close()
                print("[INFO] PostgreSQL connection closed")

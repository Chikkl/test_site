from file_bd.IDataSaver import IDataSaver
from entity.User import User
import psycopg2
from file_bd.config import host, user_name, password, db_name


class PGDataSaver(IDataSaver):
    def save_user(self, user: User) -> None:
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
                    f"INSERT INTO users(users_name) VALUES ({user.name})"
                )
        except Exception as _ex:
            print("[INFO] Error while working with PostgreSQL", _ex)
        finally:
            if connection:
                connection.close()
                print("[INFO] PostgreSQL connection closed")

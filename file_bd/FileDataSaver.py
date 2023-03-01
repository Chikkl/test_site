from file_bd.IDataSaver import IDataSaver
from entity.User import User


class FileDataSaver(IDataSaver):
    def save_user(self, user: User) -> None:
        # with open("saved_users") as users_collection:
        users_collection = open("./saved_users", "a")
        users_collection.write(user.name + "\n")
        users_collection.close()
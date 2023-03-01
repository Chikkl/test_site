from file_bd.IDataLoader import IDataLoader


class FileDataLoader(IDataLoader):
    def load_all_users(self) -> str:
        with open("./saved_users", "r") as users_collection:
            return "\n".join(users_collection.readlines())

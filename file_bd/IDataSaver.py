from entity.User import User


class IDataSaver:
    def save_user(self, user: User) -> None:
        raise "Требуется реализация интерфейса"
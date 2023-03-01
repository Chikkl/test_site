from file_bd.IDataSaver import IDataSaver
from entity.User import User
from usecase.IUserCreator import IUserCreator


class SimpleUserCreator(IUserCreator):
    def __init__(self, data_saver):
        self.__IDataSaver: IDataSaver = data_saver

    def create(self, name: str):
        user = User(name)
        self.__IDataSaver.save_user(user)

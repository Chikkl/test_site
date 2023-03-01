from flask import Flask, request

from file_bd.PGDataLoader import PGDataLoader
from file_bd.PGDataSaver import PGDataSaver
from file_bd.IDataLoader import IDataLoader
from file_bd.IDataSaver import IDataSaver
from usecase.IUserCreator import IUserCreator
from usecase.SimpleUserCrator import SimpleUserCreator

app = Flask("hello")

if __name__ == "__main__":
    data_saver: IDataSaver = PGDataSaver()
    data_loader: IDataLoader = PGDataLoader()
    user_creator: IUserCreator = SimpleUserCreator(data_saver)


    @app.route('/add-user')
    def query_example():
        user_name = request.args.get('user-name')
        user_creator.create(user_name)

        return data_loader.load_all_users()

    @app.route("/users")
    def main_route():
        return data_loader.load_all_users()

    app.run()
from db.prepare_db_provider import prepareDB
from models.App import App

if __name__ == "__main__":
    prepareDB()
    app = App()
    app.open()
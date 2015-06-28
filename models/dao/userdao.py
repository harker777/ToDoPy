from gluon import current

class UserDao:
    db = current.db

    @staticmethod
    def getAllUsers():
        db = UserDao.db;
        return db(db.user.id > 0).select(db.user.ALL);
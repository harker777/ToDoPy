from gluon import current

class UserDao:
    @staticmethod
    def getAllUsers():
        db = current.db;
        return db().select(db.user.ALL);

    @staticmethod
    def getUsersProjects(id):
        db = current.db;
        return db(db.project.user_id==id).select(db.project.ALL);
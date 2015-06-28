from gluon import current

class UserDao:
    db = current.db

    @staticmethod
    def getAllUsers():
        db = UserDao.db;
        return db().select(db.user.ALL);

    def getUsersProjects(id):
        db = UserDao.db;
        return db(db.task.project_id=id).select(db.task.ALL);

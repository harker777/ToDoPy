from gluon import current

class TaskDao:
    db = current.db

    @staticmethod
    def getAllTasks():
        db = TaskDao.db;
        return db().select(db.task.ALL);

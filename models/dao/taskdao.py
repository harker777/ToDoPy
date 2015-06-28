from gluon import current

class TaskDao:
    db = current.db

    @staticmethod
    def getAllTasks():
        db = TaskDao.db;
        return db(db.task.id > 0).select(db.task.ALL);

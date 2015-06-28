from gluon import current

class TaskDao:
    @staticmethod
    def getAllTasks():
        db = current.db;
        return db().select(db.task.ALL);

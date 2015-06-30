from gluon import current

class TaskDao:
    @staticmethod
    def getAllTasks():
        db = current.db
        return db().select(db.task.ALL)

    @staticmethod
    def getTasksForProject(projectId):
        db = current.db
        return db(db.task.project_id == projectId).select(db.task.ALL)
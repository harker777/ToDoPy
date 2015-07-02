from gluon import current

class ProjectDao:
    @staticmethod
    def getAllProjects():
        db = current.db;
        return db().select(db.project.ALL);

    @staticmethod
    def getProjectById(id):
        db = current.db;
        return db(db.project.id == id).select(db.project.ALL)[0];

from gluon import current

class ProjectDao:
    @staticmethod
    def getAllProjects():
        db = current.db;
        return db().select(db.project.ALL);

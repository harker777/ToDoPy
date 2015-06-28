from gluon import current

class ProjectDao:
    db = current.db

    @staticmethod
    def getAllProjects():
        db = ProjectDao.db;
        return db().select(db.project.ALL);

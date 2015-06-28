from gluon import current

class ProjectDao:
    db = current.db

    @staticmethod
    def getAllProjects():
        db = ProjectDao.db;
        return db(db.project.id > 0).select(db.project.ALL);

from gluon import current

class TagDao:
    db = current.db

    @staticmethod
    def getAllTags():
        db = TagDao.db;
        return db().select(db.tag.ALL);

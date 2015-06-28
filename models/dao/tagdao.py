from gluon import current

class TagDao:
    db = current.db

    @staticmethod
    def getAllTags():
        db = TagDao.db;
        return db(db.tag.id > 0).select(db.tag.ALL);

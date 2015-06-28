from gluon import current

class TagDao:
    @staticmethod
    def getAllTags():
        db = current.db;
        return db().select(db.tag.ALL);

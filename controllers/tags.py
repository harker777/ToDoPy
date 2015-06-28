from applications.todo.models.dao.tagdao import TagDao

def index():
    rows = TagDao.getAllTags();#db(db.tag.id > 0).select(db.tag.ALL)
    return dict(tags = rows )


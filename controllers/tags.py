def index():
    rows = db(db.tag.id > 0).select(db.tag.ALL)
    return dict(projects = tags)

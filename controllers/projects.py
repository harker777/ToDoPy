def index():
    rows = db(db.project.id > 0).select(db.project.ALL)
    return dict(projects = rows)

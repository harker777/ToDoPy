def index():
    rows = db(db.task.id > 0).select(db.task.ALL)
    return dict(tasks = rows)


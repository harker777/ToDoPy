def index():
    rows = db(db.user.id > 0).select(db.user.ALL)
    return dict(users = rows)